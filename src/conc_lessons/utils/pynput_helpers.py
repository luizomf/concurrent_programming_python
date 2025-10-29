from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

import pynput


class PynputHotkeys:
    """Classe para facilitar a criação de hotkeys do Pynput"""

    def __init__(self) -> None:
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
        """Wrapper do callback das keys que permite argumentos com tipagem"""

        def on_activate() -> None:
            cb(*args, **kwargs)

        return on_activate


def start_pynput(pynput_hotkeys: PynputHotkeys) -> pynput.keyboard.GlobalHotKeys:
    """Helper para facilitar a criação de hotkeys do Pynput

    ```python
    Exemplo:
    hotkeys = PynputHotkeys()
    hotkeys.add_hotkey("<ctrl>+<alt>+i", lambda: print(123))

    listener = start_pynput()
    ```
    """
    listener = pynput.keyboard.GlobalHotKeys(pynput_hotkeys.hotkeys, suppress=True)
    listener.start()
    return listener
