#
# Time.monotonic e time.monotonic_ns - Gerencie Tempo Corretamente
#
import math
import threading
import time

from conc_lessons.utils.base import get_perftime
from conc_lessons.utils.prints import Print


class MyThread(threading.Thread):
    def __init__(
        self,
        seconds: float,
        name: str,
        daemon: bool | None = None,  # noqa: FBT001
    ) -> None:
        super().__init__(
            group=None,
            name=name,
            daemon=daemon,
            context=None,
        )
        self._name = name
        self._seconds = seconds

        self._stop_event = threading.Event()

        self._running_event = threading.Event()
        self._running_event.set()

    def run(self) -> None:
        remaining = self._seconds

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

            # AQUI VIRIA O SEU CÓDIGO
            Print.purple(f"{fmt_time(remaining)}")

            if remaining <= 0:
                break

            self._stop_event.wait(timeout)

            remaining -= one_sec
            loop_diff_ns = time.monotonic_ns() - start_ns - timeout_ns

        self._stop_event.set()

    def stop(self) -> None:
        self._stop_event.set()

    def pause(self) -> None:
        self._running_event.clear()

    def resume(self) -> None:
        self._running_event.set()

    def toggle_pause(self) -> None:
        if self._running_event.is_set():
            return self._running_event.clear()
        return self._running_event.set()


def fmt_time(seconds: float) -> str:
    h = math.trunc(seconds // 3600)
    m = math.trunc(seconds // 60 % 60)
    s = math.trunc(seconds % 60)

    return f"{h:02d}:{m:02d}:{s:02d}"


if __name__ == "__main__":
    from datetime import datetime, timedelta

    start_time = time.perf_counter()

    Print.header("MainThread")

    seconds = 600
    t1 = MyThread(seconds=seconds, name="Thread1")

    start_date = datetime.now()  # noqa: DTZ005
    expected_end_date = start_date + timedelta(seconds=seconds)
    t1.start()

    t1.join()  # Bloqueia (nada para baixo será executado)
    end_date = datetime.now()  # noqa: DTZ005

    Print.ln()
    Print.purple(f"{start_date=:%d/%m/%Y %H:%M:%S}")
    Print.purple(f"{end_date=:%d/%m/%Y %H:%M:%S}")
    Print.purple(f"{expected_end_date=:%d/%m/%Y %H:%M:%S}")

    get_perftime(start_time)
    Print.ln()
