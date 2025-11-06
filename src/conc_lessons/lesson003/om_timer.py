import math
import sys
import threading
import time

from prompt_toolkit import Application
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.layout import (
    FormattedTextControl,
    HSplit,
    Layout,
    VSplit,
    Window,
    WindowAlign,
)

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.text_box import compose_box_chrs


class TimerThread(threading.Thread):
    def __init__(
        self,
        seconds: int,
        timer_label: str = "",
        running_clr: str = "",
        paused_clr: str = "",
        stopped_clr: str = "",
        *,
        daemon: bool | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=daemon, name=name)
        self.timer_label = timer_label
        self.running_clr = running_clr  # Cor ao executar
        self.paused_clr = paused_clr  # Cor quando pausar
        self.stopped_clr = stopped_clr  # Cor quando terminar

        self._current_clr = self.running_clr
        self._res_clr = Ansi.res  # reset geral do ANSI
        self._seconds = seconds
        self._remaining = max(0, int(seconds))  # tempo restante
        self._content = ""

        self._run_event = threading.Event()  # Usado para play e pause
        self._run_event.set()  # Inicia executando

        self._stop_event = threading.Event()  # Usado para parar
        self._has_died = False  # Depois de matar a thread não poderemos mexer mais

    def stop(self) -> None:
        self._run_event.set()  # A Thread não pode estar dormindo
        self._stop_event.set()  # Marca para finalizar
        self._set_end_content()
        self._has_died = True

    def pause(self) -> None:
        self._run_event.clear()  # Pause
        self._set_paused_content()

    def resume(self) -> None:
        self._run_event.set()  # Executa
        self._set_running_content()

    def is_running(self) -> bool:
        return self._run_event.is_set()

    def toggle_run(self) -> bool:
        if self.is_running():
            self.pause()
        else:
            self.resume()
        return self.is_running()

    @property
    def content(self) -> str:
        return self._content  # o conteúdo que será renderizado

    def run(self) -> None:
        ns_per_sec = 1_000_000_000

        timeout_ns = ns_per_sec
        timeout = timeout_ns / ns_per_sec
        diff_time = 0

        if self.is_running():
            self._set_running_content()
        else:
            self._set_paused_content()

        while not self._stop_event.is_set():
            if not self.is_running():
                self._run_event.wait(1)
                continue

            timeout_ns = ns_per_sec - diff_time
            timeout = timeout_ns / ns_per_sec

            start_time = time.monotonic_ns()

            if self._remaining <= 0:
                break

            self._set_running_content()
            self._remaining -= 1
            self._stop_event.wait(timeout)

            end_time = time.monotonic_ns() - start_time
            diff_time = end_time - timeout_ns

        self.stop()

    def _compose(self, secs: float, append: str = "", prepend: str = "") -> str:
        if self._has_died:
            return self.content

        clr = self._current_clr
        box_chrs = compose_box_chrs(fmt_secs(secs), clr, clr, clr, self._res_clr)
        return f"{prepend}\n{box_chrs}{append}"

    def _set_running_content(self) -> None:
        self._current_clr = self.running_clr
        self._content = self._compose(self._remaining, "Running", self.timer_label)

    def _set_end_content(self) -> None:
        self._current_clr = self.stopped_clr
        self._content = self._compose(
            self._remaining, "The thread is dead, Jim.", self.timer_label
        )

    def _set_paused_content(self) -> None:
        self._current_clr = self.paused_clr
        self._content = self._compose(self._remaining, "Paused", self.timer_label)


def fmt_secs(seconds: float) -> str:
    if seconds <= 0:
        return "00:00:00"

    h = math.trunc(seconds // 3600)
    m = math.trunc(seconds // 60 % 60)
    s = math.trunc(seconds % 60)

    return f"{h:02d}:{m:02d}:{s:02d}"


def make_thread(
    timer_name: str,
    seconds: int,
    key_bindings: KeyBindings,
    key: str | None = None,
    running_clr: str | None = None,
    paused_clr: str | None = None,
    stopped_clr: str | None = None,
) -> TimerThread:
    running_clr = running_clr or f"{Ansi.yelb}{Ansi.bla}"
    paused_clr = paused_clr or f"{Ansi.yelb}{Ansi.bla}"
    stopped_clr = stopped_clr or f"{Ansi.yelb}{Ansi.bla}"

    timer_thread = TimerThread(
        seconds=seconds,
        timer_label=timer_name,
        running_clr=running_clr,
        paused_clr=paused_clr,
        stopped_clr=stopped_clr,
    )
    timer_thread.start()

    if key is not None:

        @key_bindings.add(key)
        def _(_: KeyPressEvent) -> None:
            timer_thread.toggle_run()

        @key_bindings.add(f"f{key}")
        def _(_: KeyPressEvent) -> None:
            timer_thread.stop()

    return timer_thread


def make_header_content() -> str:
    gil_enabled = getattr(sys, "_is_gil_enabled", lambda: False)()

    yel = f"{Ansi.yelb}{Ansi.bla}"
    blu = f"{Ansi.blub}{Ansi.whi}"

    num_clr = yel if gil_enabled else blu
    chr_clr = blu if gil_enabled else yel
    python_txt = "&Python&%3.14%" if gil_enabled else "&NO&GIL&%3.14%"

    python_logo = compose_box_chrs(
        python_txt,
        res_clr=Ansi.res,
        chr_clr=f"{chr_clr}",
        punc_clr=f"{num_clr}",
        num_clr=f"{num_clr}",
    )
    header_content = f"\n{python_logo}\n"
    header_content += """
    O que você está vendo é apenas a combinação de caracteres que dão a impressão
    de números e letras. Além de threads Python para permitir concorrência.
     """.strip()

    return header_content


def make_text_control(text: str) -> ANSI:
    return ANSI(text)


def make_thread_task_control(thread: TimerThread) -> ANSI:
    return make_text_control(thread.content)


if __name__ == "__main__":
    kb = KeyBindings()

    threads: dict[str, TimerThread] = {
        "1": make_thread(
            timer_name="Timer 1",
            seconds=1200,
            key_bindings=kb,
            key="1",
            running_clr=f"{Ansi.pinb}{Ansi.bla}",
            paused_clr=f"{Ansi.orab}{Ansi.whi}",
            stopped_clr=f"{Ansi.whib}{Ansi.bla}",
        ),
        "2": make_thread(
            timer_name="Timer 2",
            seconds=1200,
            key_bindings=kb,
            key="2",
            running_clr=f"{Ansi.cyab}{Ansi.bla}",
            paused_clr=f"{Ansi.orab}{Ansi.whi}",
            stopped_clr=f"{Ansi.whib}{Ansi.bla}",
        ),
        "3": make_thread(
            timer_name="Timer 3",
            seconds=1200,
            key_bindings=kb,
            key="3",
            running_clr=f"{Ansi.purb}{Ansi.whi}",
            paused_clr=f"{Ansi.orab}{Ansi.whi}",
            stopped_clr=f"{Ansi.whib}{Ansi.bla}",
        ),
        "4": make_thread(
            timer_name="Timer 4",
            seconds=10,
            key_bindings=kb,
            key="4",
            running_clr=f"{Ansi.greb}{Ansi.bla}",
            paused_clr=f"{Ansi.orab}{Ansi.whi}",
            stopped_clr=f"{Ansi.whib}{Ansi.bla}",
        ),
    }

    # Finaliza o APP e para as threads
    @kb.add("c-q")
    def exit_(event: KeyPressEvent) -> None:
        for thread in threads.values():
            thread.stop()
        event.app.exit()

    win_align = WindowAlign.CENTER
    header = FormattedTextControl(lambda: make_text_control(make_header_content()))

    timer1 = FormattedTextControl(lambda: make_thread_task_control(threads["1"]))
    timer2 = FormattedTextControl(lambda: make_thread_task_control(threads["2"]))
    timer3 = FormattedTextControl(lambda: make_thread_task_control(threads["3"]))
    timer4 = FormattedTextControl(lambda: make_thread_task_control(threads["4"]))

    row1 = Window(header, align=win_align)
    row2 = VSplit([Window(timer1, align=win_align), Window(timer2, align=win_align)])
    row3 = VSplit([Window(timer3, align=win_align), Window(timer4, align=win_align)])

    root_container = HSplit([row1, row2, row3])
    layout = Layout(root_container)
    app = Application(layout, key_bindings=kb, full_screen=True, refresh_interval=1)

    app.output.show_cursor = lambda: None
    app.run(in_thread=True)
    print("\x1b[?25h", end="", flush=True)  # show cursor
