#
# Timer Thread em Python - Criando um timer estiloso
#
# - Ver a classe threading.Timer -> Ok
# - Trocar _seconds to _remaining -> Ok
# - Adicionar cores: current, stopped, paused e running -> Ok
# - Adicionar _content e property content para obter os valores da thread -> Ok
# - O método stop garante que não está pausado -> Ok
# - Criar método compose para criar a text box -> Ok
# - Criar métodos _set para running, stopped e paused -> Ok
# - Usar métodos próprios para stop, is running, pause, etc... -> Ok
#
import math
import threading
import time

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.base import get_perftime
from conc_lessons.utils.prints import Print
from conc_lessons.utils.text_box import compose_box_chrs


class MyThread(threading.Thread):
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
        self.resume()  # Evitar "deadlock" (ficar preso no pause)
        self._stop_event.set()
        self._set_stopped_content()

    def pause(self) -> None:
        self._running_event.clear()
        self._set_paused_content()

    def resume(self) -> None:
        self._running_event.set()
        self._set_running_content()

    def toggle_pause(self) -> None:
        if self.is_running():
            return self.pause()
        return self.resume()

    def _set_paused_content(self) -> None:
        self._current_clr = self._paused_clr
        self._content = self._compose(self._remaining)

    def _set_running_content(self) -> None:
        self._current_clr = self._running_clr
        self._content = self._compose(self._remaining)

    def _set_stopped_content(self) -> None:
        self._current_clr = self._stopped_clr
        self._content = self._compose(self._remaining)

    def _compose(self, secs: float) -> str:
        c = self._current_clr
        return compose_box_chrs(fmt_time(secs), c, c, c, Ansi.res, "SM")


def fmt_time(seconds: float) -> str:
    h = math.trunc(seconds // 3600)
    m = math.trunc(seconds // 60 % 60)
    s = math.trunc(seconds % 60)

    return f"{h:02d}:{m:02d}:{s:02d}"


if __name__ == "__main__":
    start_time = time.perf_counter()

    Print.header("MainThread")

    seconds = 20
    t1 = MyThread(
        seconds=seconds,
        name="Thread1",
        running_clr="\x1b[48;5;46m\x1b[38;5;0m",
        stopped_clr="\x1b[48;5;255m\x1b[38;5;0m",
        paused_clr="\x1b[48;5;249m\x1b[38;5;0m",
    )
    t1.start()

    pause_seconds = 5
    threading.Timer(pause_seconds, t1.pause).start()
    threading.Timer(pause_seconds + pause_seconds, t1.resume).start()

    # Interface gráfica
    stop_time = time.monotonic() + seconds + pause_seconds + 1
    while time.monotonic() <= stop_time:
        print("\x1b[H\x1b[2J", end="", flush=True)
        print(t1.content)
        time.sleep(1 / 2)

    t1.join()  # Bloqueia (nada para baixo será executado)

    get_perftime(start_time)
    Print.ln()
