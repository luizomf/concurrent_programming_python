import threading
import time

from conc_lessons.utils.base import get_perftime
from conc_lessons.utils.prints import Print
from conc_lessons.utils.system_random import rndint


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

        self._result: list[str] = []
        self._exception: BaseException | None = None

    def run(self) -> None:
        try:
            self._check_seconds()
            seconds = self._seconds
            while seconds > 0:
                result = f"{self.name}{seconds}"
                Print.result(" ", result)
                self._result.append(result)
                seconds -= 1
                time.sleep(1)
        except ValueError as err:
            self._exception = err

    @property
    def result(self) -> list[str]:
        return self._result

    @property
    def exception(self) -> BaseException | None:
        return self._exception

    def _check_seconds(self) -> None:
        max_seconds = 20
        if self._seconds >= max_seconds:
            msg = f"Seconds must be less than or equal to {max_seconds}"
            raise ValueError(msg)


if __name__ == "__main__":
    start_time = time.perf_counter()

    threads_dict = {
        i: MyThread(
            seconds=rndint(0, 2),
            name=f"Thread{i}_",
        )
        for i in range(1, 10)
    }
    threads = list(threads_dict.values())

    for t in threads:
        t.start()

    while any(t.is_alive() for t in threads):
        time.sleep(1 / 60)

    Print.header("Results or Errors")

    results = []
    errors = []
    for t in threads_dict.values():
        if t.exception is not None:
            errors.append(t.exception)

        if t.result:
            results.append(t.result)

    print("\x1b[38;5;2m", end="", flush=True)
    Print.pprint(results)
    print("\x1b[38;5;1m", end="", flush=True)
    Print.pprint(errors)
    print("\x1b[0m", end="", flush=True)

    get_perftime(start_time)

    Print.ln()
