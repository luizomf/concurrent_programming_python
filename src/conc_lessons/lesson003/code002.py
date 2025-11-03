import threading
from typing import TYPE_CHECKING

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.base import run_simulated_io
from conc_lessons.utils.prints import Print

if TYPE_CHECKING:
    from collections.abc import Callable


#
# Mudar a tipagem e usar ParamSpec no target
#
class MyThread[**P, R](threading.Thread):
    def __init__(
        self,
        target: Callable[P, R],
        name: str | None = None,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None:
        super().__init__(
            group=None,
            target=target,
            name=name,
            args=args,
            kwargs=None,
            daemon=None,
            context=None,
        )
        self._target = target
        self._name = name
        self._args = args
        self._kwargs = kwargs

        # Para obter o resultado da execução da thread
        self.result: str | None = None
        self.exception: BaseException | None = None

    def run(self) -> None:
        self.result = "O resultado da execução da thread"

        try:
            if self._target is not None:
                self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs


if __name__ == "__main__":
    t1 = MyThread(target=run_simulated_io, ident="Thread 1", nap_time=1, clr=Ansi.pin)
    t1.start()

    Print.clr("Essa é a MainThread", clr=Ansi.cya)

    t1.join()

    Print.clr(f"Aqui o resultado: {t1.result=}", clr=Ansi.cya)

    Print.ln()
