import threading
import time
from typing import TYPE_CHECKING

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.base import get_perftime, run_simulated_io
from conc_lessons.utils.prints import Print
from conc_lessons.utils.system_random import rndflt

if TYPE_CHECKING:
    from collections.abc import Callable


class MyThread[**P, R](threading.Thread):
    def __init__(
        self,
        target: Callable[P, R],
        name: str,
        daemon: bool | None = None,  # noqa: FBT001
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        super().__init__(
            group=None,
            target=target,
            name=name,
            args=args,
            kwargs=kwargs,
            daemon=daemon,
            context=None,
        )
        self._target = target
        self._name = name
        self._args = args
        self._kwargs = kwargs

        self._result: R | None = None
        self._exception: BaseException | None = None

    def run(self) -> None:
        try:
            if self._target is not None:
                self._result = self._target(*self._args, **self._kwargs)
        except RuntimeError as err:
            self._exception = err
        finally:
            del self._target, self._args, self._kwargs

    @property
    def result(self) -> R | None:
        return self._result

    @property
    def exception(self) -> BaseException | None:
        return self._exception


if __name__ == "__main__":
    start_time = time.perf_counter()

    threads_dict = {
        i: MyThread(
            target=run_simulated_io,
            name=f"Thread{i}",
            ident=f"Thread{i}",
            nap_time=rndflt(0, 5),
            clr=Ansi.rand_fg(),
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

        if t.result is not None:
            results.append(t.result)

    Print.result(" ", results)
    Print.error(" ", errors)

    get_perftime(start_time)

    Print.ln()
