from random import SystemRandom

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
