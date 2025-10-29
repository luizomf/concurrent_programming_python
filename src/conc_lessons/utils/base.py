# Apenas coisas para simulações de tasks I/O-bound ou CPU-bound

import threading
import time

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.prints import Print


def run_simulated_io(ident: str, nap_time: float = 1, clr: str = "") -> str:
    """Simula uma operação de I/O usando time.sleep.

    Args:
        ident (str): Identificador da execução (para facilitar log e print).
        nap_time (float, optional): Tempo de espera simulando I/O. Default 1 seg.
        clr (str, optional): Código ANSI de cor. Default é vazio.

    Raises:
        RuntimeError: Se `ident` terminar com 4, simula um erro de execução.

    Returns:
        str: O identificador da execução após completar a simulação.
    """
    curr_thread = threading.current_thread()
    name = curr_thread.name
    cl = ""

    if ident.endswith("4"):
        m = f"Simulated error for {ident}"
        error = RuntimeError(m)

        Print.clr(f" {name} ", repr(error), tag=f"{ident} Error")

        raise error

    Print.clr(
        " I/O-bound task starting...",
        f"({name})",
        f"(Sleep {nap_time:.2f}s)",
        clr=clr,
        tag=f" {ident: >2} {'START:': <7} ",
    )

    time.sleep(nap_time)  # simula trabalho

    Print.clr(
        " I/O-bound task ending...",
        f"{name}",
        f"(Sleep {nap_time:.2f}s)",
        clr=clr,
        tag=f" {ident: >2} {'END:': <7} ",
    )

    return ident


def get_perftime(start_time: float, *, verbose: bool = True) -> float:
    """Obtém o tempo de execução de start_time até a execução desta função.

    Args:
        start_time (float): Use time.perf_counter() para o início da execução
        verbose (bool): Exibe a mensagem na tela. Default True

    Returns:
        float: O tempo de execução em segundos.
    """
    end_time = time.perf_counter()  # Pega o tempo final da execução
    elapsed = end_time - start_time  # Calcula o tempo que levou para executar

    if verbose:
        Print.ln()
        Print.inline(
            f" Execution took {elapsed:.4f} seconds.",
            clr=f"{Ansi.cya}",
            tag="TIME:",
        )
        Print.ln()
        Print.ln()

    return elapsed
