import resource
import time
from concurrent.futures import (
    Future,
    InterpreterPoolExecutor,  # paralelismo com interpretadores
    ProcessPoolExecutor,  # paralelismo com processos
    ThreadPoolExecutor,  # paralelismo com threads
    as_completed,
)

before = resource.getrusage(resource.RUSAGE_SELF)

MAX_WORKERS = 4
NUM_JOBS = 20
NUM_LOOPS = 10


def dummy_cpu_bound(ident: int = 0, loops: int = 1) -> str:
    for _ in range(loops):
        for i in range(5_000):
            for j in range(5_000):
                _ = i * j
    return f"dummy_cpu_bound({ident}, Loops={loops})"


def get_elapsed_time(start: float, name: str) -> float:
    elapsed = time.perf_counter() - start
    print()
    print(f"[{name: <14}] took {elapsed:.2f} seconds to run")
    print()
    return elapsed


def print_completed(futures: list[Future[str]], name: str) -> None:
    futures_as_completed = as_completed(futures)

    for future_completed in futures_as_completed:
        print(f"[{name: <14}]", future_completed.result())


def get_result(futures: list[Future[str]], name: str) -> None:
    print(f"[{name: <14}]")
    print(f"{[future.result() for future in futures]}")
    print()


def run_threads(name: str) -> None:
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        start = time.perf_counter()
        futures = [
            executor.submit(dummy_cpu_bound, ident, NUM_LOOPS)
            for ident in range(NUM_JOBS)
        ]
        print_completed(futures, name)

    get_elapsed_time(start, name)
    get_result(futures, name)


def run_interpreters(name: str) -> None:
    with InterpreterPoolExecutor(max_workers=MAX_WORKERS) as executor:
        start = time.perf_counter()
        futures = [
            executor.submit(dummy_cpu_bound, ident, NUM_LOOPS)
            for ident in range(NUM_JOBS)
        ]
        print_completed(futures, name)

    get_elapsed_time(start, name)
    get_result(futures, name)


def run_procs(name: str) -> None:
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        start = time.perf_counter()
        futures = [
            executor.submit(dummy_cpu_bound, ident, NUM_LOOPS)
            for ident in range(NUM_JOBS)
        ]
        print_completed(futures, name)

    get_elapsed_time(start, name)
    get_result(futures, name)


if __name__ == "__main__":
    print()
    run_threads("Threads")
    print()
    run_procs("Processes")
    print()
    run_interpreters("Interpreters")
    print()

    after = resource.getrusage(resource.RUSAGE_SELF)
    print("voluntary:", after.ru_nvcsw - before.ru_nvcsw)
    print("involuntary:", after.ru_nivcsw - before.ru_nivcsw)
