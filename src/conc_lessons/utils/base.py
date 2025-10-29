# Código repetitivo que vou usar durando as aulas

import logging
import sys
import threading
import time
from functools import partial
from random import SystemRandom
from typing import TYPE_CHECKING, Final

import pynput

if TYPE_CHECKING:
    from collections.abc import Callable


from conc_lessons.utils.ansi import (
    b,
    bi,
    bla,
    cya,
    gre,
    greb,
    pur,
    purb,
    red,
    redb,
    res,
)

# LOGGING CONFIGS
# Caso queira aprender mais:
# https://www.youtube.com/playlist?list=PLbIBj8vQhvm28qR-yvWP3JELGelWxsxaI

LOG_LEVEL = logging.DEBUG
# Você pode comentar isso se quiser (root level)
logging.getLogger().setLevel(LOG_LEVEL)

# Nosso logger (GERAL)
logger = logging.getLogger("conc_lessons")
logger.setLevel(LOG_LEVEL)

logger_formatter = logging.Formatter(fmt="%(message)s")
logger_stream_handler = logging.StreamHandler(stream=sys.stdout)
logger_stream_handler.terminator = ""  # Remove a quebra de linha padrão

logger_stream_handler.setFormatter(logger_formatter)
logger.addHandler(logger_stream_handler)

# Usado para evitar uso de 100% de CPU em loops apertados
BUSY_WAIT_TIME = 1 / 100

# TODOS OS VALORES COM MIN E MAX SÃO ALEATÓRIOS.
# Se você configurar um valor igual para ambos, este valor será fixo.

MIN_NAP: Final[float] = 1.00
MAX_NAP: Final[float] = 1.00

MAX_WORKERS: Final[int] = 4
MIN_JOBS: Final[int] = 8
MAX_JOBS: Final[int] = 8

# A largura das tags coloridas - Só para estilo
TAG_COLUMN_WIDTH = 20

# Random do sistema
sysrand = SystemRandom()


def rndflt(min_: float = 0, max_: float = 1) -> float:
    """Float aleatório, bom para números quebrados ou muito pequenos (uniform)

    Args:
        min_ (float, optional): Menor número possível. Default 0.
        max_ (float, optional): Maior número possível I/O. Default 1.

    Returns:
        float: Um valor aleatório entre min_ e max_.
    """
    return sysrand.uniform(min_, max_)


def rndint(min_: int = 0, max_: int = 1) -> int:
    """int aleatório, bom para números inteiros (randint)

    Args:
        min_ (int, optional): Menor número possível. Default 0.
        max_ (int, optional): Maior número possível I/O. Default 1.

    Returns:
        int: Um valor aleatório entre min_ e max_.
    """
    return sysrand.randint(min_, max_)


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

    if ident.endswith("4"):
        m = f"Simulated error for {ident}"
        error = RuntimeError(m)

        print_error(f" {name} ", repr(error), tag=f"{ident} Error")

        raise error

    print_clr(
        " I/O-bound task starting...",
        f"({name})",
        f"(Sleep {nap_time:.2f}s)",
        clr=clr,
        tag=f" {ident: >2} {'START:': <7} ",
    )

    time.sleep(nap_time)  # simula trabalho

    print_clr(
        " I/O-bound task ending...",
        f"{name}",
        f"(Sleep {nap_time:.2f}s)",
        clr=clr,
        tag=f" {ident: >2} {'END:': <7} ",
    )

    return ident


def print_clr(
    *args: object,
    sep: str = " ",
    end: str = "\n",
    tag: str = "",
    tagclrbg: str = "",
    tagclrfg: str = "",
    clr: str = "",
) -> None:
    """O print com adição de um argumento para cor e tag (para facilitar).

    Args:
        args (object): Argumentos posicionais para exibir
        sep (str): Um separador para mais de um argumento. Default " "
        end (str): Adicionado ao final do print. Default ""
        tag (str): Adiciona uma tag colorida no início do print
        tagclrbg (str): Cor de fundo para a tag (se não informado, usa clr)
        tagclrfg (str): Cor do texto para tag (se não informado, usa preto)
        clr (str): String com a cor ANSI do foreground (se torna background na tag)
    """
    clrs = f"{res}{clr}"
    tag = tag.strip()

    if tag:
        tagclrbg = tagclrbg if tagclrbg else clr.replace("38", "48")
        tagclrfg = tagclrfg if tagclrfg else bla
        tag = f"{tag.strip()[: TAG_COLUMN_WIDTH - 2]: ^{TAG_COLUMN_WIDTH}}"
        tag = f"{res}{b}{tagclrbg}{tagclrfg}{tag}{res}"
    logger.debug(f"{tag}{clrs}{sep.join(map(str, args))}{res}{end}")  # noqa: G004


def make_partial_print(
    *args: object,
    sep: str = " ",
    end: str = "\n",
    tag: str = "",
    tagclrbg: str = "",
    tagclrfg: str = "",
    clr: str = "",
) -> partial[None]:
    return partial(
        print_clr,
        *args,
        sep=sep,
        end=end,
        tag=tag,
        clr=clr,
        tagclrbg=tagclrbg,
        tagclrfg=tagclrfg,
    )


inline_print = make_partial_print(sep="", end="")
print_result = make_partial_print(
    sep="", clr=gre, tagclrfg=bla, tagclrbg=greb, tag=" Success: "
)
print_title = make_partial_print("\n", end="\n\n", sep="", clr=f"{bi}")
print_wait = make_partial_print(
    sep="", clr=pur, tagclrbg=purb, tagclrfg=bla, tag=" Waiting: "
)
print_error = make_partial_print(
    sep="", clr=red, tagclrbg=redb, tagclrfg=bla, tag=" Error: "
)
print_ln = make_partial_print("\n", end="")


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
        print_ln()
        inline_print(
            f" Execution took {elapsed:.4f} seconds.",
            clr=f"{cya}",
            tag="TIME:",
        )
        print_ln()
        print_ln()

    return elapsed


class PynputHotkeys:
    """Classe para facilitar a criação de hotkeys do Pynput

    ```python
    Exemplo:

    def say_my_name(name: str) -> None:
        print(name)

    hotkeys = PynputHotkeys()
    hotkeys.add_hotkey("<ctrl>+<alt>+i", event.set)
    hotkeys.add_hotkey("<ctrl>+<alt>+n", say_my_name, name="Heisenberg")

    listener = keyboard.GlobalHotKeys(hotkeys.hotkeys)
    listener.start()
    ```
    """

    def __init__(self) -> None:
        """Use add_hotkey para criar novas hotkeys"""
        self.hotkeys: dict[str, Callable[..., None]] = {}

    def add_hotkey[**P, R](
        self, key: str, cb: Callable[P, R], *args: P.args, **kwargs: P.kwargs
    ) -> None:
        """Adiciona novas hotkeys com tipagem e callback

        Args:
            key (str): combinação de teclas, como em <ctrl>+<alt>+i
            cb (callable): callback que será executado ao pressionar as teclas
            args: os argumentos posicionais para o callback
            kwargs: os argumentos nomeados para o callback
        """
        self.hotkeys[key] = PynputHotkeys.create_hotkey_cb(cb, *args, **kwargs)

    @staticmethod
    def create_hotkey_cb[**P, R](
        cb: Callable[P, R], *args: P.args, **kwargs: P.kwargs
    ) -> Callable[..., None]:
        """Wrapper para o callback para permitir a passagem de argumentos"""

        def on_activate() -> None:
            cb(*args, **kwargs)

        return on_activate


def start_pynput(pynput_hotkeys: PynputHotkeys) -> pynput.keyboard.GlobalHotKeys:
    listener = pynput.keyboard.GlobalHotKeys(pynput_hotkeys.hotkeys, suppress=True)
    listener.start()
    return listener
