import threading
import time

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.base import (
    get_perftime,
    run_simulated_io,
)
from conc_lessons.utils.constants import BUSY_WAIT_TIME
from conc_lessons.utils.prints import Print


def custom_hook(exc: threading.ExceptHookArgs) -> None:
    Print.error(" ", repr(exc.exc_value), tag=" Custom Hook ")


# Último recurso
threading.excepthook = custom_hook


if __name__ == "__main__":
    start_time = time.perf_counter()  # Marca o tempo de início da execução

    t1 = threading.Thread(
        target=run_simulated_io, args=("Work 1", 1, Ansi.pin), name="thread1"
    )
    t2 = threading.Thread(
        target=run_simulated_io, args=("Work 2", 1, Ansi.yel), name="thread2"
    )
    t3 = threading.Thread(
        target=run_simulated_io, args=("Work 3", 1, Ansi.gre), name="thread3"
    )

    curr_thread = threading.current_thread()
    Print.header(f"Thread atual: {curr_thread.name}")
    Print.purple(f"O que está rodando na {curr_thread.name}")

    temp_threads = [t1, t2, t3]
    temp_threads.extend(
        [
            threading.Thread(
                target=run_simulated_io,
                args=(f"Work {i}", 1, Ansi.rand_fg()),
                name=f"thread{i}",
            )
            for i in range(4, 16)
        ]
    )

    while temp_threads:
        for t in temp_threads:
            if t.ident is None:
                t.start()

            if not t.is_alive():
                temp_threads.remove(t)

        time.sleep(BUSY_WAIT_TIME)

    get_perftime(start_time)

    Print.ln()
