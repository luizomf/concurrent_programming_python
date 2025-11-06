import math
import threading
import time

from prompt_toolkit.application import Application
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.key_binding import KeyBindings, KeyPressEvent
from prompt_toolkit.layout import (
    FormattedTextControl,
    Layout,
    VSplit,
    Window,
    WindowAlign,
)
from prompt_toolkit.layout.containers import HSplit

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.text_box import compose_box_chrs


class TimerThread(threading.Thread):
    def __init__(
        self,
        seconds: float,
        name: str,
        stopped_clr: str = "",
        paused_clr: str = "",
        running_clr: str = "",
        daemon: bool | None = None,  # noqa: FBT001
    ) -> None:
        super().__init__(
            group=None,
            name=name,
            daemon=daemon,
            context=None,
        )
        self._content = ""
        self._is_dead = False

        self._name = name
        self._remaining = max(0, seconds)
        self._current_clr: str = ""

        self._stopped_clr = stopped_clr
        self._paused_clr = paused_clr
        self._running_clr = running_clr

        self._stop_event = threading.Event()

        self._running_event = threading.Event()
        self._running_event.set()
        self._set_running_content()

    @property
    def content(self) -> str:
        return self._content

    def run(self) -> None:
        one_sec = 1
        one_ns = 1_000_000_000

        timeout_ns = one_ns
        loop_diff_ns = 0

        while not self._stop_event.is_set():
            if not self._running_event.is_set():
                self._running_event.wait(1)
                continue

            start_ns = time.monotonic_ns()
            timeout_ns = one_ns - loop_diff_ns
            timeout = timeout_ns / one_ns

            if self._remaining <= 0:
                break

            self._set_running_content()
            self._remaining -= one_sec

            self._stop_event.wait(timeout)

            loop_diff_ns = time.monotonic_ns() - start_ns - timeout_ns

        self._remaining = 0
        self.stop()

    def is_running(self) -> bool:
        return self._running_event.is_set()

    def stop(self) -> None:
        self.resume()
        self._stop_event.set()
        self._set_stopped_content()
        self._is_dead = True

    def pause(self) -> None:
        if self._is_dead:
            return
        self._running_event.clear()
        self._set_paused_content()

    def resume(self) -> None:
        if self._is_dead:
            return
        self._running_event.set()
        self._set_running_content()

    def toggle_pause(self) -> None:
        if self.is_running():
            return self.pause()
        return self.resume()

    def _set_paused_content(self) -> None:
        if self._is_dead:
            return
        self._current_clr = self._paused_clr
        self._content = f"{self.name}\n" + self._compose(self._remaining) + "Paused"

    def _set_running_content(self) -> None:
        if self._is_dead:
            return
        self._current_clr = self._running_clr
        self._content = f"{self.name}\n" + self._compose(self._remaining) + "Running"

    def _set_stopped_content(self) -> None:
        if self._is_dead:
            return
        self._current_clr = self._stopped_clr
        self._content = (
            f"{self.name}\n"
            + self._compose(self._remaining)
            + "The thread is dead, Jim."
        )

    def _compose(self, secs: float) -> str:
        if self._is_dead:
            return self._content

        c = self._current_clr
        return compose_box_chrs(fmt_time(secs), c, c, c, Ansi.res, "SM")


def fmt_time(seconds: float) -> str:
    h = math.trunc(seconds // 3600)
    m = math.trunc(seconds // 60 % 60)
    s = math.trunc(seconds % 60)

    return f"{h:02d}:{m:02d}:{s:02d}"


def make_timer_thread(
    seconds: int,
    name: str,
    key_pause: str,
    key_stop: str,
    kb: KeyBindings,
    running_clr: str = f"{Ansi.greb}{Ansi.bla}",
) -> TimerThread:
    timer = TimerThread(
        seconds=seconds,
        name=name,
        running_clr=running_clr,
        paused_clr=f"{Ansi.orab}{Ansi.bla}",
        stopped_clr=f"{Ansi.whib}{Ansi.bla}",
        daemon=True,
    )
    timer.start()

    @kb.add(key_pause)
    def _(_: KeyPressEvent) -> None:
        timer.toggle_pause()

    @kb.add(key_stop)
    def _(_: KeyPressEvent) -> None:
        timer.stop()

    return timer


if __name__ == "__main__":
    kb = KeyBindings()

    python_logo = compose_box_chrs(
        "&Python&%3.14%",
        res_clr=Ansi.res,
        chr_clr=f"{Ansi.blub}{Ansi.whi}",
        punc_clr=f"{Ansi.yelb}{Ansi.bla}",
        num_clr=f"{Ansi.yelb}{Ansi.bla}",
    )

    timer1 = make_timer_thread(
        seconds=86400,
        name="Timer 1",
        key_pause="1",
        key_stop="f1",
        kb=kb,
        running_clr=f"{Ansi.greb}{Ansi.bla}",
    )

    timer2 = make_timer_thread(
        seconds=3600,
        name="Timer 2",
        key_pause="2",
        key_stop="f2",
        kb=kb,
        running_clr=f"{Ansi.pinb}{Ansi.bla}",
    )

    timer3 = make_timer_thread(
        seconds=28000,
        name="Timer 3",
        key_pause="3",
        key_stop="f3",
        kb=kb,
        running_clr=f"{Ansi.cyab}{Ansi.bla}",
    )

    timer4 = make_timer_thread(
        seconds=60,
        name="Timer 4",
        key_pause="4",
        key_stop="f4",
        kb=kb,
        running_clr=f"{Ansi.purb}{Ansi.bla}",
    )

    row1 = HSplit(
        [
            Window(
                FormattedTextControl(text=ANSI("\n" + python_logo)),
                height=5,
                align=WindowAlign.CENTER,
            ),
            Window(
                FormattedTextControl(
                    text="Aqui você poderia adicionar o texto que desejar."
                ),
                height=2,
                align=WindowAlign.CENTER,
            ),
        ],
    )
    row2 = VSplit(
        [
            Window(
                FormattedTextControl(text=lambda: ANSI(timer1.content)),
                align=WindowAlign.CENTER,
            ),
            Window(
                FormattedTextControl(text=lambda: ANSI(timer2.content)),
                align=WindowAlign.CENTER,
            ),
        ],
    )
    row3 = VSplit(
        [
            Window(
                FormattedTextControl(text=lambda: ANSI(timer3.content)),
                align=WindowAlign.CENTER,
            ),
            Window(
                FormattedTextControl(text=lambda: ANSI(timer4.content)),
                align=WindowAlign.CENTER,
            ),
        ]
    )

    rows = [row1, row2, row3]
    layout = Layout(HSplit(rows))

    @kb.add("c-q")
    def _(event: KeyPressEvent) -> None:
        event.app.exit()

    app = Application(
        layout=layout, key_bindings=kb, full_screen=True, refresh_interval=1 / 4
    )
    app.run()
