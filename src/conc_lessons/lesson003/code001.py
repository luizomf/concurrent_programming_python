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
# Algumas recomendações da Doc:
#
# - não é aconselhável sobrescrever outros métodos além do __init__ e run().
# - O __init__ deve ser chamado com argumentos nomeados
# - O método start deve ser chamado apenas uma vez para preparar tudo antes do run
# - `ident` da thread é None se ela ainda não foi iniciada
# - O método `is_alive` retorna `True` um pouco antes e depois do método run.

# Mudar a tipagem e usar ParamSpec no target
# Herança sem target sobrescrevendo run().
# threading.Event - Iniciar, pausar e parar a thread
# Finalmente criaremos o timer e sua interface
#

if __name__ == "__main__":
    pass
