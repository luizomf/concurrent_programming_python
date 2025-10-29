from typing import Final

# Usado para evitar uso de 100% de CPU em loops apertados.
# Loop apertado é um loop muito rápido como whiles True da vida (em resumo).
BUSY_WAIT_TIME = 1 / 100

# TODOS OS VALORES COM MIN E MAX SÃO ALEATÓRIOS.
# Se você configurar um valor igual para ambos, este valor será fixo.

MIN_NAP: Final[float] = 1.00
MAX_NAP: Final[float] = 1.00

# Quantidade mínima e máxima de funções que devem ser executadas em concorrência
# Isso deverá ser limitado por "MAX_WORKERS" por vez.
# Ex.: se temos min 5 max 10, podemos obter um valor aleatório 8.
# Se MAX_WORKERS for 2, significa que faremos 2 trabalhos por vez.
# Quando um finaliza, outro entra para ser executado. Assim garantimos que não
# vamos usar todos os recursos do servidor ou computador e evitamos falhas.
MIN_JOBS: Final[int] = 8
MAX_JOBS: Final[int] = 8

# Esse MAX é diferente, isso  significa a quantidade máxima de workers:
# Pode ser para threads ou processos diferentes.
MAX_WORKERS: Final[int] = 4
