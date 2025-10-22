# ruff: noqa: TC003
import asyncio
import math
import re
import sys
import termios
import tty
from collections.abc import Sequence
from random import SystemRandom

from conc_lessons.lesson001.teory import concurrency_teory
from conc_lessons.utils.ansi import (
    ALT_OFF,
    ALT_ON,
    CURSOR_OFF,
    CURSOR_ON,
    PROGRESS_CLR,
    RESTORE,
    SAVE,
    blu,
    cl,
    cup,
    cya,
    el,
    gre,
    ln,
    pin,
    pur,
    res,
    term_size,
    write,
    yel,
)

LINE_BREAK = re.compile(r"__L__")

PAUSE_CHAR = "p"
QUIT_CHAR = "q"
SPEED = 0.03
PROGRESS_CHAR = "░"

sysrand = SystemRandom()


async def read_input(bye: asyncio.Event, pause: asyncio.Event) -> None:
    loop = asyncio.get_running_loop()

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    tty.setcbreak(fd)  # sem echo (macos/linux/unix em geral)

    try:
        reader = asyncio.StreamReader()
        protocol = asyncio.StreamReaderProtocol(reader)
        await loop.connect_read_pipe(lambda: protocol, sys.stdin)

        while not bye.is_set():
            ch = await reader.read(1)
            should_pause = pause.is_set()

            if ch == QUIT_CHAR.encode():
                pause.set()
                bye.set()
                break

            if ch == PAUSE_CHAR.encode() and should_pause:
                pause.clear()

            if ch == PAUSE_CHAR.encode() and not should_pause:
                pause.set()

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


async def write_words(line: str, bye: asyncio.Event) -> None:
    if bye.is_set():
        return

    for char in line.split(" "):
        if bye.is_set():
            break

        if char.strip():
            write(f"{RESTORE}{char} {SAVE}")
            await asyncio.sleep(SPEED)
        else:
            write(f"{RESTORE}{char} {SAVE}")


async def loop_lines(block: str, bye: asyncio.Event, pause: asyncio.Event) -> None:
    if bye.is_set():
        return

    write(cup(3, 1), f"{SAVE}", el())

    for line in LINE_BREAK.split(block):
        if bye.is_set():
            break

        await write_words(line, bye)

        if not bye.is_set() and line:
            pause.clear()

        await pause.wait()


async def write_face(line: int, offset: int, bye: asyncio.Event, clr: str) -> None:
    many_faces = [["(-.-)", "(o.o)"]]
    faces = sysrand.choice(many_faces)
    while not bye.is_set():
        width, _ = term_size()

        face = sysrand.choice(faces)

        write(cup(line, width - offset), f"{res}{clr}{face}{res}")
        await asyncio.sleep(sysrand.uniform(0, 2))


async def write_progress_no(curr_block: int, blocks: int, bye: asyncio.Event) -> None:
    if bye.is_set():
        return

    scrn_w, _ = term_size()
    half_scrn = math.floor(scrn_w / 2)

    txt = f"{curr_block: >2}/{blocks: >2}"

    txt_width = len(txt)
    half_txt_width = math.floor(txt_width / 2)
    row = 2
    col = int(half_scrn - half_txt_width)

    txt = txt.replace("/", f"{res}/{res}{yel}")
    write(cup(row, col), f"{res}❬{yel}{txt}{res}❭{res}")


async def write_progress(progress: int, bye: asyncio.Event) -> None:
    if bye.is_set():
        return

    write(cup(1, 1), res, PROGRESS_CLR, PROGRESS_CHAR * progress, res)


async def progress_bar(
    curr_blocks: asyncio.Queue[int], blocks_no: int, bye: asyncio.Event
) -> None:
    width, _ = term_size()
    curr_block = 1

    while not bye.is_set():
        width, _ = term_size()

        if not curr_blocks.empty():
            curr_block = curr_blocks.get_nowait()
            progress = round(width / blocks_no * curr_block)

            await write_progress(progress, bye)
            await write_progress_no(curr_block, blocks_no, bye)

            curr_blocks.task_done()
        else:
            await write_progress_no(curr_block, blocks_no, bye)

        await asyncio.sleep(SPEED)

        if curr_block == blocks_no:
            break


async def prepare_screen(bye: asyncio.Event) -> None:
    if bye.is_set():
        return

    write(cup(1, 1), res)
    ln()
    write(cup(2, 1), res)
    ln()
    write(cup(3, 1), res, cl())


async def text_writter(bye: asyncio.Event, pause: asyncio.Event) -> None:
    curr_block_q: asyncio.Queue[int] = asyncio.Queue()
    blocks: Sequence[str] = concurrency_teory
    blocks_no = len(blocks)

    progress_task = asyncio.create_task(progress_bar(curr_block_q, blocks_no, bye))

    for curr_block, text_block in enumerate(blocks, start=1):
        await curr_block_q.put(curr_block)
        await prepare_screen(bye)
        await loop_lines(text_block, bye, pause)

    curr_block_q.shutdown()
    await progress_task
    await bye.wait()


async def main() -> None:
    write(CURSOR_OFF)
    write(ALT_ON)

    bye = asyncio.Event()
    pause = asyncio.Event()
    pause.set()  # Já inicia rodando

    clrs = [pur, pin, cya, yel, blu, gre]  # cores carinhas
    faces_offset_clrs = zip(range(6, 44, 6), clrs, strict=False)  # offset carinhas

    writer_t = asyncio.create_task(text_writter(bye, pause))
    reader_t = asyncio.create_task(read_input(bye, pause))
    face_ts = [write_face(2, o, bye, c) for o, c in faces_offset_clrs]

    await asyncio.gather(reader_t, writer_t, *face_ts, return_exceptions=True)
    await bye.wait()

    write(ALT_OFF)
    write(CURSOR_ON)


if __name__ == "__main__":
    asyncio.run(main())

    write(ALT_OFF)
    write(CURSOR_ON)
