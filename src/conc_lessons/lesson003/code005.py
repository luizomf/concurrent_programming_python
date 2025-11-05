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

        # True  ou False (padrão)
        # set()    clear()
        # is_set() <- conferir se o evento está como True
        # wait() <- bloqueia quando o evento está False
        # wait(timeout) <- bloqueia quando acabar o timeout

        self._running_event = threading.Event()
        self._running_event.set()  # True

    def run(self) -> None:
        seconds = self._seconds

        while not self._stop_event.is_set():
            if not self._running_event.is_set():
                Print.debug(" Thread pausada ", time.time())
                self._running_event.wait(1)  # bloqueia
                continue

            Print.purple(" Aguardando stop ", time.time())
            self._stop_event.wait(1)  # bloqueia

    def stop(self) -> None:
        Print.yellow(" Parando a thread ", self.name)
        self._stop_event.set()

    def pause(self) -> None:
        Print.cyan(" Pausando a thread ", self.name)
        self._running_event.clear()

    def resume(self) -> None:
        Print.green(" Continuando a thread ", self.name)
        self._running_event.set()

    def toggle_pause(self) -> None:
        if self._running_event.is_set():
            return self._running_event.clear()
        return self._running_event.set()


if __name__ == "__main__":
    start_time = time.perf_counter()

    Print.header("MainThread")
    t1 = MyThread(seconds=10, name="Thread1")
    t1.start()

    time.sleep(5)
    t1.pause()

    time.sleep(5)
    t1.resume()

    time.sleep(5)
    t1.toggle_pause()

    time.sleep(5)
    t1.toggle_pause()

    time.sleep(30)
    t1.stop()

    t1.join()  # Bloqueia (nada para baixo será executado)
    get_perftime(start_time)

    Print.ln()
