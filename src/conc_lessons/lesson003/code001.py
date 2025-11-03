import threading
from typing import TYPE_CHECKING, Any

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.base import run_simulated_io
from conc_lessons.utils.prints import Print

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
#
# Criando Threads por herança
#
# Observação:
# @jairfsj -> Me passou nos comentários do vídeo anterior.
# A pronúncia de "daemon" é dimon com do de í.
# https://youtu.be/mDCJeoXvnhM?si=0quj4EFufqxh22gT
#
# Herança simples e tipagem
#
# Algumas recomendações da Doc:
#
# - não é aconselhável sobrescrever outros métodos além do __init__ e run().
# - O __init__ deve ser chamado com argumentos nomeados
# - O método start deve ser chamado apenas uma vez para preparar tudo antes do run
# - `ident` da thread é None se ela ainda não foi iniciada
# - O método `is_alive` retorna `True` um pouco antes e depois do método run.
#


class MyThread(threading.Thread):
    def __init__(
        self,
        target: Callable[..., object] | None = None,
        name: str | None = None,
        args: Iterable[Any] = (),
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

    def run(self) -> None:
        return super().run()


if __name__ == "__main__":
    t1 = MyThread(target=run_simulated_io, args=("Thread 1", 1, "\x1b[38;5;2m"))
    t1.start()

    Print.clr("Essa é a MainThread", clr=Ansi.cya)

    t1.join()
