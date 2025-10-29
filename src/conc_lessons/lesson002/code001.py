# Um exemplo de código síncrono que você já conhece bem
import time

from conc_lessons.utils.ansi import gre, pin, yel
from conc_lessons.utils.base import (
    get_perftime,
    run_simulated_io,
)

if __name__ == "__main__":
    start_time = time.perf_counter()  # Marca o tempo de início da execução

    run_simulated_io("Work 1", 1, pin)  # 1 segundo
    run_simulated_io("Work 2", 1, yel)
    run_simulated_io("Work 3", 1, gre)

    # É natural que esse código leve aprox. 3 segundos para terminar
    get_perftime(start_time)
