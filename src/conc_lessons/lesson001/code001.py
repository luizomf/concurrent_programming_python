import os
import threading
import time

start_time = time.perf_counter()  # Marca o tempo de início do script

# Quando usamos time.sleep(), o CPython informa ao sistema operacional:
# "pode usar a CPU para outra coisa por enquanto".
# Sistemas operacionais modernos usam algo chamado *preempção*, ou seja,
# as threads não ficam realmente "paradas". O SO faz um *context switch*:
# ele salva o estado atual da thread e passa a CPU para outra tarefa.
#
# Quando o tempo de sleep termina, a thread entra numa fila com estado "pronta".
# O *scheduler* (agendador do SO) verifica as threads prontas e decide qual
# delas volta a executar, restaurando o contexto salvo anteriormente.
# Esse processo tem um custo (menor que criar um processo novo, mas ainda assim
# não é de graça, então nunca diga que sleep não faz nada 🤣).
time.sleep(1)  # ❌ I/O bound artificial de 1 segundo (vamos falar disso adiante)

# PIDs e TIDs
process_id = os.getpid()  # ID do processo atual
python_thread_id = threading.get_ident()  # ID da thread (interno do Python)
system_thread_id = threading.get_native_id()  # ID nativo da thread no SO

print("PID (Process ID):", process_id)
print("Python TID (Thread ID):", python_thread_id)
print("System TID (Thread ID):", system_thread_id)

time.sleep(1)  # Outro I/O bound e mais um context switch

end_time = time.perf_counter()  # Tempo final
elapsed_time = end_time - start_time

print(f"Seu código levou {elapsed_time:.2f} segundos para executar.")
# Saída esperada:
# PID (Process ID): 11419
# Python TID (Thread ID): 8323549184
# System TID (Thread ID): 3396994
# Seu código levou 2.01 segundos para executar.
