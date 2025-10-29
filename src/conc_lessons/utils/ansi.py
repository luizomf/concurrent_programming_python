"""Este módulo tem apenas códigos ANSI para estilo e cores."""

# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
# https://en.wikipedia.org/wiki/Box_Drawing
import re
import shutil
from typing import TYPE_CHECKING, Literal

from conc_lessons.utils.system_random import sysrand

if TYPE_CHECKING:
    from collections.abc import Sequence

MAX_COLOR_NO = 255

CSI = "\x1b["  # Control Sequence Introducer
ALT_ON = f"{CSI}?1049h"  # Alternative screen buffer ON/OFF
ALT_OFF = f"{CSI}?1049l"
CURSOR_ON = f"{CSI}?25h"  # Cursor ON/OFF
CURSOR_OFF = f"{CSI}?25l"
# Interessante: carriage return é o "puxar a alavanca" da máquina de escrever
# Ele volta o carro para o começo da linha.
LINE = "\n"  # Line Feed (Windows carriage return + line feed \r\n)

SAVE = f"{CSI}s"
RESTORE = f"{CSI}u"
HOME = f"{CSI}H"
EL = f"{CSI}K"  # limpa até o final da linha
CL = f"{CSI}J"  # limpa da linha para baixo

ANSI_ESCAPE = re.compile(r"\x1b\[([0-9;]*)[A-Za-z]")
PROGRESS_CLR = f"{CSI}38;5;33m"

PERCIVED_BRIGHTNESS = 130


async def visible_width(s: str) -> int:
    clean = ANSI_ESCAPE.sub("", s)
    return len(clean)


def term_size() -> tuple[int, int]:
    term_cols, term_rows = shutil.get_terminal_size()
    return term_cols, term_rows


def cup(row: int, col: int) -> str:  # posição do cursor
    return f"{CSI}{row};{col}H"


def el() -> str:  # limpa até o fim da linha
    return EL


def cl() -> str:  # limpa da linha para baixo
    return CL


def csr(top: str, bottom: str) -> str:
    return f"{CSI}{top};{bottom}r"


def reset_csr() -> str:
    return f"{CSI}r"


def write(*args: object) -> None:
    print(*args, end="", sep="", flush=True)


def clear() -> None:
    write("\033[H\033[2J")


def ln() -> None:
    write(LINE)


def perceived_brightness(r: int, g: int, b: int) -> float:
    """Calcula o brilho percebido de uma cor RGB.

    Modelo HSP (Highly Sensitive Poo / Human perception), que tenta aproximar o
    modo como o olho humano percebe a luminosidade.

    Fórmula:
        brightness = sqrt(0.241*R^2 + 0.691*G^2 + 0.068*B^2)

    - R, G, B devem estar no intervalo 0-255.
    - O resultado será um número de 0 a 255.
      Quanto maior, mais clara a cor parece ao olho humano.

    Exemplo:
        >>> perceived_brightness(255, 255, 255)  # branco
        255.0
        >>> perceived_brightness(0, 0, 0)        # preto
        0.0
        >>> perceived_brightness(255, 0, 0)      # vermelho
        123.0
        >>> perceived_brightness(0, 255, 0)      # verde
        210.1

    Observação:
        Essa fórmula foi a mais simples que encontrei e funcionou. Pode não
        ser muito precisa para outros casos (faça testes).
    """
    return (0.241 * r * r + 0.691 * g * g + 0.068 * b * b) ** 0.5


res = f"{CSI}0m"  # reset all
resf = f"{CSI}39m"  # reset foreground
resb = f"{CSI}49m"  # reset background

b = f"{CSI}1m"  # bold
bres = f"{CSI}22m"  # reset bold
di = f"{CSI}2m"  # dim
dires = f"{CSI}22m"  # reset dim
i = f"{CSI}3m"  # italic
ires = f"{CSI}23m"  # reset italic
u = f"{CSI}4m"  # underline
ures = f"{CSI}24m"  # reset underline
inv = f"{CSI}7m"  # inverse
invres = f"{CSI}27m"  # reset inverse
hide = f"{CSI}8m"  # hide
hideres = f"{CSI}28m"  # reset hide
st = f"{CSI}9m"  # strike
stres = f"{CSI}29m"  # reset strike

blab = f"{CSI}48;5;232m"  # black background
bla = f"{CSI}38;5;232m"  # black foreground
whib = f"{CSI}48;5;8m"  # white background
whi = f"{CSI}38;5;255m"  # white foreground
redb = f"{CSI}48;5;204m"  # red background
red = f"{CSI}38;5;204m"  # red foreground
purb = f"{CSI}48;5;93m"  # purple background
pur = f"{CSI}38;5;141m"  # purple foreground
pinb = f"{CSI}48;5;219m"  # pink background
pin = f"{CSI}38;5;219m"  # pink foreground
blub = f"{CSI}48;5;27m"  # blue background
blu = f"{CSI}38;5;69m"  # blue foreground
cyab = f"{CSI}48;5;117m"  # cyan background
cya = f"{CSI}38;5;117m"  # cyan foreground
greb = f"{CSI}48;5;120m"  # green background
gre = f"{CSI}38;5;120m"  # green foreground
orab = f"{CSI}48;5;202m"  # orange background
ora = f"{CSI}38;5;214m"  # orange foreground
yelb = f"{CSI}48;5;222m"  # yellow background
yel = f"{CSI}38;5;222m"  # yellow foreground

# 256 cores costuma ser compatível com a maioria dos terminals modernos
CLRS256: list[str] = [
    f"{CSI}38;5;{i}m" if i <= MAX_COLOR_NO else f"{CSI}38;5;{15}m"
    for i in [
        *range(2, 8),
        *range(10, 16),
        *range(17, 232),
        *range(232, 1031),
    ]
]
CLRS256BG: list[str] = [redb, purb, pinb, blub, cyab, greb, orab, yelb]


# ⚠️ True Color (24bit) ou TC, costuma NÃO SER COMPATÍVEL com vários terminais.
CLRSTC: list[str] = [
    f"{CSI}38;2;{r};{g};{b}m"
    for r in range(0, 256, 8)
    for g in range(0, 256, 8)
    for b in range(0, 256, 8)
    if perceived_brightness(r, g, b) > PERCIVED_BRIGHTNESS
]

fg = f"{CSI}38;5;15m"  # foreground
bg = f"{CSI}49m"  # background (I'm using reset background)


ui = f"{u}{i}"  # underline italic
bi = f"{b}{i}"  # bold italic

bui = f"{b}{ui}"  # bold underline italic

dii = f"{di}{i}"  # dim italic
dibi = f"{di}{bi}"  # dim bold italic

fgb = f"{fg}{b}"  # foreground bold
hi = f"{cyab}{bla}{b}"  # highlight
hiy = f"{yelb}{bla}{b}"  # highlight
df = f"{res}{fg}{bg}"  # try to reset to default colors
star = f"{cya}✱{fg}"  # asterisk for lists
ac = f"{gre}"  # asyncio color (termos sobre asyncio)
acb = f"{greb}{bla}{b}"  # asyncio bg color (termos sobre asyncio)
pc = f"{pin}"  # process color (termos sobre processos)
pcb = f"{pinb}{bla}{b}"  # process bg color (termos sobre processos)
tc = f"{yel}"  # threads color (termos sobre threads)
tcb = f"{yelb}{bla}{b}"  # threads bg color (termos sobre threads)
hea = f"{cya}{bi}"  # Titles


fg = f"{CSI}38;5;15m"  # foreground
bg = f"{CSI}49m"  # background (I'm using reset background)


ui = f"{u}{i}"  # underline italic
bi = f"{b}{i}"  # bold italic

bui = f"{b}{ui}"  # bold underline italic

dii = f"{di}{i}"  # dim italic
dibi = f"{di}{bi}"  # dim bold italic

fgb = f"{fg}{b}"  # foreground bold
hi = f"{cyab}{bla}{b}"  # highlight
hiy = f"{yelb}{bla}{b}"  # highlight
df = f"{res}{fg}{bg}"  # try to reset to default colors
star = f"{cya}✱{fg}"  # asterisk for lists
ac = f"{gre}"  # asyncio color (termos sobre asyncio)
acb = f"{greb}{bla}{b}"  # asyncio bg color (termos sobre asyncio)
pc = f"{pin}"  # process color (termos sobre processos)
pcb = f"{pinb}{bla}{b}"  # process bg color (termos sobre processos)
tc = f"{yel}"  # threads color (termos sobre threads)
tcb = f"{yelb}{bla}{b}"  # threads bg color (termos sobre threads)
hea = f"{cya}{bi}"  # Titles


class Ansi:
    csi = CSI  # Control Sequence Introducer
    res = res  #  Reset all
    resf = resf  # Reset foreground
    resb = resb  # Reset Background

    b = b  # bold
    bres = bres  # reset bold
    di = di  # dim
    dires = dires  # reset dim
    i = i  # italic
    ires = ires  # reset italic
    u = u  # underline
    ures = ures  # reset underline
    inv = inv  # inverse
    invres = invres  # reset inverse
    hide = hide  # hide
    hideres = hideres  # reset hide
    st = st  # strike
    stres = stres  # reset strike

    blab = blab  # black background
    bla = bla  # black foreground
    whib = whib  # white background
    whi = whi  # white foreground
    redb = redb  # red background
    red = red  # red foreground
    purb = purb  # purple background
    pur = pur  # purple foreground
    pinb = pinb  # pink background
    pin = pin  # pink foreground
    blub = blub  # blue background
    blu = blu  # blue foreground
    cyab = cyab  # cyan background
    cya = cya  # cyan foreground
    greb = greb  # green background
    gre = gre  # green foreground
    orab = orab  # orange background
    ora = ora  # orange foreground
    yelb = yelb  # yellow background
    yel = yel  # yellow foreground

    fg = fg  # default foreground
    bg = bg  # reset background

    ui = ui  # underline italic
    bi = bi  # bold italic

    bui = bui  # bold underline italic

    dii = dii  # dim italic
    dibi = dibi  # dim bold italic

    fgb = fgb  # default foreground bold
    hi = hi  # highlight
    hiy = hiy  # highlight yellow
    df = df  # default colors
    star = star  # unicode asterisk
    ac = ac  # asyncio foreground
    acb = acb  # asyncio background
    pc = pc  # process foreground
    pcb = pcb  # process background
    tc = tc  # thread foreground
    tcb = tcb  # thread background
    hea = hea  # Headers (titles)

    @staticmethod
    def foreground(clr_number: int) -> str:
        return f"{CSI}38;5;{clr_number}m"

    @staticmethod
    def rand_fg(*, true_color: bool = True) -> str:
        if true_color:
            return Ansi.bg_to_fg(sysrand.choice(CLRSTC))
        return Ansi.bg_to_fg(sysrand.choice(CLRS256))

    @staticmethod
    def rand_bg(*, true_color: bool = True) -> str:
        if true_color:
            return Ansi.fg_to_bg(sysrand.choice(CLRSTC))
        return Ansi.fg_to_bg(sysrand.choice(CLRS256))

    @staticmethod
    def bg_to_fg(clr: str) -> str:
        return clr.replace("[48;", "[38;")

    @staticmethod
    def fg_to_bg(clr: str) -> str:
        return clr.replace("[38;", "[48;")

    @staticmethod
    def background(clr_number: int) -> str:
        return f"{CSI}48;5;{clr_number}m"

    @staticmethod
    def style(
        styles: Sequence[Literal["b", "u", "i", "st", "di", "inv", "hide"]],
    ) -> str:
        return "".join([getattr(Ansi, s) for s in styles])


if __name__ == "__main__":
    pass
