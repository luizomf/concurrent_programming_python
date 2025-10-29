# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
# https://en.wikipedia.org/wiki/Box_Drawing
import re
import shutil

MAX_COLOR_NO = 255

CSI = "\x1b["  # Control Sequence Introducer
ALT_ON = f"{CSI}?1049h"  # Alternative screen buffer ON/OFF
ALT_OFF = f"{CSI}?1049l"
CURSOR_ON = f"{CSI}?25h"  # Cursor ON/OFF
CURSOR_OFF = f"{CSI}?25l"
# Interessante: carriage return é o "puxar a alavanca" da máquina de escrever
# Ele volta o carro para o começo da linha.
LINE = "\n"  # Line Feed (Windows carriage return + line feed \r\n)

SAVE = f"{CSI}s"
RESTORE = f"{CSI}u"
HOME = f"{CSI}H"
EL = f"{CSI}K"  # limpa até o final da linha
CL = f"{CSI}J"  # limpa da linha para baixo

ANSI_ESCAPE = re.compile(r"\x1b\[([0-9;]*)[A-Za-z]")
PROGRESS_CLR = f"{CSI}38;5;33m"


async def visible_width(s: str) -> int:
    clean = ANSI_ESCAPE.sub("", s)
    return len(clean)


def term_size() -> tuple[int, int]:
    term_cols, term_rows = shutil.get_terminal_size()
    return term_cols, term_rows


def cup(row: int, col: int) -> str:  # posição do cursor
    return f"{CSI}{row};{col}H"


def el() -> str:  # limpa até o fim da linha
    return EL


def cl() -> str:  # limpa da linha para baixo
    return CL


def csr(top: str, bottom: str) -> str:
    return f"{CSI}{top};{bottom}r"


def reset_csr() -> str:
    return f"{CSI}r"


def write(*args: object) -> None:
    print(*args, end="", sep="", flush=True)


def clear() -> None:
    write("\033[H\033[2J")


def ln() -> None:
    write(LINE)


res = f"{CSI}0m"  # reset all
resf = f"{CSI}39m"  # reset foreground
resb = f"{CSI}49m"  # reset background

b = f"{CSI}1m"  # bold
bres = f"{CSI}22m"  # reset bold
di = f"{CSI}2m"  # dim
dires = f"{CSI}22m"  # reset dim
i = f"{CSI}3m"  # italic
ires = f"{CSI}23m"  # reset italic
u = f"{CSI}4m"  # underline
ures = f"{CSI}24m"  # reset underline
inv = f"{CSI}7m"  # inverse
invres = f"{CSI}27m"  # reset inverse
hide = f"{CSI}8m"  # hide
hideres = f"{CSI}28m"  # reset hide
st = f"{CSI}9m"  # strike
stres = f"{CSI}29m"  # reset strike

blab = f"{CSI}48;5;232m"  # black background
bla = f"{CSI}38;5;232m"  # black foreground
whib = f"{CSI}48;5;8m"  # white background
whi = f"{CSI}38;5;255m"  # white foreground
redb = f"{CSI}48;5;204m"  # red background
red = f"{CSI}38;5;204m"  # red foreground
purb = f"{CSI}48;5;93m"  # purple background
pur = f"{CSI}38;5;141m"  # purple foreground
pinb = f"{CSI}48;5;219m"  # pink background
pin = f"{CSI}38;5;219m"  # pink foreground
blub = f"{CSI}48;5;27m"  # blue background
blu = f"{CSI}38;5;69m"  # blue foreground
cyab = f"{CSI}48;5;117m"  # cyan background
cya = f"{CSI}38;5;117m"  # cyan foreground
greb = f"{CSI}48;5;120m"  # green background
gre = f"{CSI}38;5;120m"  # green foreground
orab = f"{CSI}48;5;202m"  # orange background
ora = f"{CSI}38;5;214m"  # orange foreground
yelb = f"{CSI}48;5;222m"  # yellow background
yel = f"{CSI}38;5;222m"  # yellow foreground

CLRS: list[str] = [
    f"{CSI}38;5;{i}m" if i <= MAX_COLOR_NO else f"{CSI}38;5;{15}m"
    for i in [
        *range(2, 8),
        *range(10, 16),
        *range(28, 52),
        *range(67, 232),
        *range(232, 1031),
    ]
]
CLRSBG: list[str] = [redb, purb, pinb, blub, cyab, greb, orab, yelb]

fg = f"{CSI}38;5;15m"  # foreground
bg = f"{CSI}49m"  # background (I'm using reset background)


ui = f"{u}{i}"  # underline italic
bi = f"{b}{i}"  # bold italic

bui = f"{b}{ui}"  # bold underline italic

dii = f"{di}{i}"  # dim italic
dibi = f"{di}{bi}"  # dim bold italic

fgb = f"{fg}{b}"  # foreground bold
hi = f"{cyab}{bla}{b}"  # highlight
hiy = f"{yelb}{bla}{b}"  # highlight
df = f"{res}{fg}{bg}"  # try to reset to default colors
star = f"{cya}✱{fg}"  # asterisk for lists
ac = f"{gre}"  # asyncio color (termos sobre asyncio)
acb = f"{greb}{bla}{b}"  # asyncio bg color (termos sobre asyncio)
pc = f"{pin}"  # process color (termos sobre processos)
pcb = f"{pinb}{bla}{b}"  # process bg color (termos sobre processos)
tc = f"{yel}"  # threads color (termos sobre threads)
tcb = f"{yelb}{bla}{b}"  # threads bg color (termos sobre threads)
hea = f"{cya}{bi}"  # Titles


if __name__ == "__main__":
    import time

    # write(ALT_ON)

    def write_header() -> None:
        write(cup(1, 1), "Teste de cabeçalho", el())
        ln()
        write(cup(2, 1), term_size(), el())
        ln()
        write(f"{CSI}0J")

    write_header()

    for i in range(1000):
        rows, cols = term_size()

        if i % (cols - 3) == 0:
            write_header()

        print(f"Testing {i}", cols)
        time.sleep(0.3)

    # write(ALT_OFF)
