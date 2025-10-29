from functools import partial

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.logger import LOGGER

# A largura das tags coloridas - Só para estilo
TAG_COLUMN_WIDTH = 20


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
    clrs = f"{Ansi.res}{clr}"
    tag = tag.strip()

    if tag:
        tagclrbg = tagclrbg if tagclrbg else clr.replace("38", "48")
        tagclrfg = tagclrfg if tagclrfg else Ansi.bla
        tag = f"{tag.strip()[: TAG_COLUMN_WIDTH - 2]: ^{TAG_COLUMN_WIDTH}}"
        tag = f"{Ansi.res}{Ansi.b}{tagclrbg}{tagclrfg}{tag}{Ansi.res}"
    LOGGER.debug(f"{tag}{clrs}{sep.join(map(str, args))}{Ansi.res}{end}")


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
    sep="", clr=Ansi.gre, tagclrfg=Ansi.bla, tagclrbg=Ansi.greb, tag=" Result: "
)
print_title = make_partial_print("\n", end="\n\n", sep="", clr=f"{Ansi.hea}")
print_wait = make_partial_print(
    sep="", clr=Ansi.pur, tagclrbg=Ansi.purb, tagclrfg=Ansi.bla, tag=" Waiting: "
)
print_error = make_partial_print(
    sep="", clr=Ansi.red, tagclrbg=Ansi.redb, tagclrfg=Ansi.bla, tag=" Error: "
)
print_ln = make_partial_print("\n", end="")


class Print:
    clr = make_partial_print()
    inline = make_partial_print(sep="", end="")

    header = make_partial_print("\n", end="\n\n", sep="", clr=f"{Ansi.hea}")

    result = make_partial_print(
        sep="", clr=Ansi.cya, tagclrfg=Ansi.bla, tagclrbg=Ansi.cyab, tag=" Result: "
    )

    wait = make_partial_print(
        sep="", clr=Ansi.pur, tagclrbg=Ansi.purb, tagclrfg=Ansi.bla, tag=" Waiting: "
    )
    ln = make_partial_print("\n", end="")

    error = make_partial_print(
        sep="", clr=Ansi.red, tagclrbg=Ansi.redb, tagclrfg=Ansi.bla, tag=" Error: "
    )
    warn = make_partial_print(
        sep="", clr=Ansi.yel, tagclrbg=Ansi.yelb, tagclrfg=Ansi.bla, tag=" Warning: "
    )
    success = make_partial_print(
        sep="", clr=Ansi.gre, tagclrbg=Ansi.greb, tagclrfg=Ansi.bla, tag=" Success: "
    )
    debug = make_partial_print(
        sep="", clr=Ansi.blu, tagclrbg=Ansi.blub, tagclrfg=Ansi.bla, tag=" Debug: "
    )

    black = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(15)}")
    blackb = make_partial_print(clr=f"{Ansi.foreground(15)}{Ansi.background(0)}")

    red = make_partial_print(clr=f"{Ansi.foreground(1)}")
    redb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(1)}")

    green = make_partial_print(clr=f"{Ansi.foreground(2)}")
    greenb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(2)}")

    yellow = make_partial_print(clr=f"{Ansi.foreground(3)}")
    yellowb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(3)}")

    blue = make_partial_print(clr=f"{Ansi.foreground(4)}")
    blueb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(4)}")

    purple = make_partial_print(clr=f"{Ansi.foreground(5)}")
    purpleb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(5)}")

    cyan = make_partial_print(clr=f"{Ansi.foreground(6)}")
    cyanb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(6)}")

    white = make_partial_print(clr=f"{Ansi.foreground(7)}")
    whiteb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.background(7)}")

    randf = make_partial_print(clr=f"{Ansi.rand_fg()}{Ansi.background(0)}")
    randb = make_partial_print(clr=f"{Ansi.foreground(0)}{Ansi.rand_bg()}")


if __name__ == "__main__":
    Print.header("ABC")

    Print.clr("ABC", clr=f"{Ansi.foreground(45)}{Ansi.style(['b', 'i'])}")
    Print.ln()

    Print.result(" ABC ")
    Print.wait(" ABC ")
    Print.error(" ABC ")
    Print.warn(" ABC ")
    Print.success(" ABC ")
    Print.debug(" ABC ")

    Print.black(" Black ")
    Print.blackb(" Black B ")

    Print.red(" Red ")
    Print.redb(" Red B ")

    Print.green(" Green ")
    Print.greenb(" Green B ")

    Print.yellow(" Yellow ")
    Print.yellowb(" Yellow B ")

    Print.blue(" Blue ")
    Print.blueb(" Blue B ")

    Print.purple(" Purple ")
    Print.purpleb(" Purple B ")

    Print.cyan(" Cyan ")
    Print.cyanb(" Cyan B ")

    Print.white(" White ")
    Print.whiteb(" White B ")

    Print.ln()
    Print.ln()
