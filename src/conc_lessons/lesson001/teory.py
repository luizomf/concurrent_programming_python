# ruff: noqa: E501, RUF001, W291
from collections.abc import Sequence

from conc_lessons.utils.ansi import (
    ac,
    acb,
    bi,
    cya,
    df,
    dii,
    hea,
    hi,
    hiy,
    i,
    pc,
    pcb,
    pin,
    pur,
    red,
    res,
    star,
    tc,
    tcb,
    yel,
)

teory_intro = f"""\
{hea}❯❯ Concorrência com Python {dii}❲muita teoria importante❳{res}
__L__
Essa aula será {hi} 99,99% {df} teórica. Vamos entender {bi}todas as partes{df} envolvidas 
em {ac}Concurrent Programming{df} com Python. {dii}(não é um tópico muito simples){df}
__L__
Esses são {bi}OS ASSUNTOS{df} que vão definir se você deve usar {acb} asyncio {df}, {tcb} threads {df},
{pcb} processos {df} ou outro tipo de concorrência.{df} 
__L__
Exemplos do que vamos entender:
__L__
{star} Como o seu código Python chega na CPU__L__
{star} Os personagens (processo, thread, SO, CPython)__L__
{star} O que é um processo e suas threads __L__
{star} Operações {acb} I/O-bound {df} e {pcb} CPU-bound {df} __L__
{star} Multitarefa Cooperativa (asyncio) e Multitarefa preemptiva (SO) __L__
{star} Asyncio e Threading no Python __L__
{star} GIL {red}♥ {df} {dii}(Global Interpreter Lock){df} __L__
{star} Paralelismo com Multiprocessing, Threads e Interpreters no Python __L__
{star} e muitos outros relacionados...
__L__
Então... Como uma visão geral, vamos começar conhecendo os personagens: 
{pur}Concorrência{df}, {pc}Processo{df}, {tc}Thread{df}, {cya}Python{df} e o {ac}Sistema Operacional{df}. 
"""

teory_non_concurrent_python = f"""\
{hea}❯❯ Python com e sem concorrência{df}
__L__
{bi}Em condições normais (sem processos ou threads adicionais), o python executa em 
um único {hi} processo {df}, como uma única {hi} thread {df} (Main Thread), em um 
único núcleo da CPU. 
__L__
Isso significa que o código é {bi}executado de forma sequencial{df}, linha após linha. 
__L__
Quando uma operação demora, ela atrasa todas as outras que vierem depois. 
__L__
É possível executar mais de uma operação de forma concorrente, seja de forma assíncrona, 
em threads ou em processos separados.
Este conceito é chamado de {hi} Concorrência {df} {dii}(Concurrent Programming){df}.
__L__
{hi} Concorrência {df} é a habilidade de um sistema em executar tarefas de forma de 
forma que possam progredir juntas para atingir um objetivo. Isso pode acontecer em 
tempo sobreposto ou em paralelo (quando a solução envolve múltiplos núcleos da CPU).
__L__
{hi} Concorrência {df} 🏃‍♀️ é um conceito amplo que envolve muitos padrões e termos, como 
assincronismo, paralelismo e multitarefas.
__L__
Em {hi} Python {df}, podemos aplicar concorrência com os módulos {acb} asyncio {df}, 
{tcb} threading {df}, {pcb} multiprocessing {df}, {hi} concurrent {df} e outros.
"""

teory_char_process = f"""\
{hea}❯❯ Processo (o contêiner){df}
__L__
{bi}Um processo representa um programa em execução no sistema operacional.{df}
__L__
É nele que ficam os {hi} recursos que o programa usa {df}, como o espaço de memória, 
descritores de arquivos, variáveis globais, call stack e as {tcb} threads {df}.
__L__
Um processo é isolado de outros processos. Isso é importante para segurança e 
vários outros fatores. Mas isso também dificulta a nossa vida 🤣.
__L__
Podemos trabalhar com concorrência usando vários {pcb} processos {df} de uma 
thread ou um único processo com várias {tcb} threads {df}.
__L__
Em Python, podemos criar um ou vários processos com os módulos: 
__L__
{star} {pur}concurrent.futures.ProcessPoolExecutor{df} (recomendado) __L__
{star} {pc}multiprocessing{df} (de forma manual)
__L__
{bi}Vamos falar de paralelismo e outros tipos de concorrência ainda neste vídeo.{df}
"""

teory_char_threads = f"""\
{hea}❯❯ Threads (o fio da meada){df}
__L__
{hi} Threads {df} representam as sequências de instruções do código compilado 
que a CPU executa. Você pode imaginá-las como um contexto de execução que pode 
ser pausado e restaurado pelo SO {dii}(explico mais à frente no vídeo){df}.
__L__
As {bi}threads têm acesso aos recursos do processo em que estão{df}, como memória 
e arquivos abertos. Isso as torna mais leves para serem criadas e gerenciadas do 
que processos {dii}(embora ainda exista um pequeno custo){df}.
__L__
Pelo mesmo motivo acima, a comunicação entre {tcb} threads {df} é bem mais fácil 
do que a comunicação entre processos {dii}(que são isolados, como vimos){df}
__L__
Você pode criar novas threads com os módulos: 
__L__
{star} {pur}concurrent.futures.ThreadPoolExecutor{df} (recomendado) __L__
{star} {tc}threading{df} (de forma manual, mas em alto nível) __L__
{star} {cya}_thread{df} (de forma manual, mas em baixo nível) 
__L__
{bi}Vamos falar dos tipos de concorrência com threads ainda neste vídeo.{df}
"""

teory_char_threads_graph = f"""\
{hea}❯❯ Exemplo em diagrama ASCII {df}
__L__{cya}
  ╭──────╮            ╭─────────────╮                      ╭─ contêiner ─╮
  │  SO  │─ executa ─▶│  Programas  │─ representados por ─▶│  Processos  │─╮
  ╰──────╯            ╰─────────────╯                      ╰─────────────╯ │
  ╭─ job ─╮                                ╭──context──╮                   │
  │  CPU  │◀─ que executam sequências na ◀─│  Threads  │◀──── que têm ─────╯
  ╰───────╯                                ╰───────────╯

  {dii}Exemplo supercial da execução de um programa.
  Um programa pode criar threads adicionais quando precisa fazer trabalhos 
  de forma concorrente.{df}
"""

teory_diff_python = f"""\
{hea}❯❯ O Python é compilado e interpretado ao mesmo tempo{df}
__L__
Em {bi}Python{df}, este processo é {bi}diferente de linguagens compiladas{df}. 
__L__
Quando você executa um {hiy} código Python {df}, o SO cria um {bi}processo{df} com os recursos 
necessários para o programa. 
__L__
Em seguida, uma {bi}thread{df} é ligada este processo, com o contexto de execução onde 
o código vai rodar.
__L__
Assim que você pressiona {hi} Enter ⏎ {df}, o Python compila seu código para 
{hi} bytecode {df}, que então será lido pelo interpretador. 
__L__
O {bi}binário do Python{df} inclui:
__L__
{star} um parser (faz o parsing da Abstract syntax tree da linguagem) __L__
{star} um compilador (compila *.py para bytecode) __L__
{star} o interpretador (é o que você acha que é o Python) __L__
{star} a API em C (nome auto explicativo)__L__ 
{star} a biblioteca padrão (que você usa em todo código)__L__ 
{star} e outras partes que cuidam do ciclo de execução
__L__
Daqui em diante, quem assume é o {hi} C {df} (por isso CPython), a thread e a CPU. 
"""

teory_diff_python_bytecode = f"""\
{hea}❯❯ Exemplo do bytecode (módulo dis){df}
__L__{yel}
{yel}   ┌─── arquivo: module.py ────────────────────────────────────┐   {df}
{yel}   │                                                           │   {df} 
{yel}   │ 0. def func() -> None:                                    │   {df}
{yel}   │ 1.   print("Hello world!")                                │{yel}──┐{df}   
{yel}   │                                                           │{yel}  │{df}   
{yel}   └───────────────────────────────────────────────────────────┘{yel}  │{df}   
{pin}   ┏═══ Terminal ══════════════════════════════════════════════┓{yel}  │{df}   
{pin}   ┃                                                           ┃{yel}◀─┘{df}   
{pin}   ┃ otavio@local:~$ python module.py                          ┃{pin}──┐{df}   
{pin}   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{pin}  │{df}   
{cya}   ┌─── dis.dis(func) ─────────────────────────────────────────┐{pin}  │{df}   
{cya}   │ 4           RESUME                   0                    │{pin}  │{df}   
{cya}   │                                                           │{pin}  │{df}   
{cya}   │ 5           LOAD_GLOBAL              1 (print + NULL)     │{pin}  │{df}   
{cya}   │             LOAD_CONST               0 ('Hello world!')   │{pin}◀─┘{df}   
{cya}   │             CALL                     1                    │   {df}
{cya}   │             POP_TOP                                       │   {df}
{cya}   │             LOAD_CONST               1 (None)             │   {df}
{cya}   │             RETURN_VALUE                                  │   {df}
{cya}   └───────────────────────────────────────────────────────────┘   {df}
{df}
"""

teory_diff_python_graph = f"""\
{hea}❯❯ O fluxo do seu código em ASCII {df}
__L__{cya}
  ╭─ module.py ──╮                 ╭── *.pyc ───╮             ╭ python3.14t ╮
  │  seu código  │─ compilado p/ ─▶│  bytecode  │─ lido por ─▶│   CPython   │─╮
  ╰──────────────╯                 ╰────────────╯             ╰─────────────╯ │
  ╭ Core1 ╮  ╭─ TID 321 ─╮                     ╭─ PID 1234 ─╮                 │
  │  CPU  │◀─│  threads  │◀─ com contexto em ──│  Processo  │◀── que está em ─╯
  ╰───────╯  ╰───────────╯                     ╰────────────╯

  {dii} Exemplo supercial da execução do Python{df}
__L__ 
"""

teory_chars_summary = f"""\
{hea}❯❯ Um breve resumo sobre tudo o que falamos {df}
__L__ 
O Python não roda o seu código especificamente, mas {tcb} bytecode {df}.
__L__
O {acb} bytecode {df} é o seu código compilado de uma forma que o Interpretador entenda. 
Isso envolve parsing, compilação e bastante {bi}C{df}.
__L__
Quem gerencia essa comunicação entre {bi}bytecode{df}, {bi}threads{df} e {bi}CPU{df} é o {hi} CPython {df}.
Essa é a implementação mais comum do {bi}interpretador Python{df}, mas existem outras. 
__L__
O {bi}sistema operacional{df} gerencia os {pcb} processos {df} e as {tcb} threads {df} reais.
__L__
Você pode criar mais processos e/ou threads quando precisar de concorrência. Mas, 
isso terá um custo adicional em recursos.
Os módulos para isso podem ser: {tcb} threading {df}, {pcb} multiprocessing {df} e {hi} concurrent.futures {df}.
__L__
Além disso, é possível fazer concorrência via API do C, com "subinterpreters" (3.14) e 
{hi} asyncio {df} {dii}(vou falar sobre asyncio adiante){df}.
__L__
Agora que conhecemos o Python melhor, podemos falar dos problemas que são resolvidos 
com concorrência.
"""

teory_concurrency_bounds = f"""\
{hea}❯❯ Termos e problemas que podemos resolver com concorrência{df} 
__L__
Os {bi}termos{df} mais comuns relacionados aos problemas que podem ser resolvidos 
com {bi}concorrência{df} são: 
__L__
{star} {bi}I/O-bound{df} __L__
{star} {bi}CPU-bound{df}
__L__
O {hi} bound {df} significa {i}❝limitado por❞{df}, então {i}❝essa thread é limitada por I/O❞{df}
ou {i}❝essa thread é limitada por CPU❞{df}.
__L__
Existem outros termos, como {hi} GPU-bound {df}, {hi} Memory-bound {df} e outros. 
Mas, é muito mais importante saber o {hi} fator limitante {df} do que o nome do problema.
"""

teory_io_bound = f"""\
{hea}❯❯ {hi} I/O-bound {df} e Multitarefas {acb} cooperativa {df} e {tcb} preemptiva {df}
__L__
{bi}I/O{df} quer dizer {bi}Entrada e Saída{df}, então {hi} I/O-bound {df} está relacionado com 
limitações na entrada e saída de dados.
__L__
Se a velocidade de entrada e saída é {bi}menor que a velocidade de processamento{df} 
dizemos que a tarefa é {hi} I/O-bound {df}.
__L__
Em outras palavras: enquanto os dados não chegam, a CPU não tem o que fazer.
__L__
Alguns exemplos de tarefas {hi} I/O-bound {df}:
__L__
{star} Ler e escrever em arquivos (depende do disco) __L__
{star} Aguardar algo da rede (internet, base de dados, APIs e outras) __L__
{star} A função sleep também é I/O-bound
"""

teory_io_bound_graph = f"""\
{hea}❯❯ Problema que pode ser resolvido com concorrência {df}
__L__{cya}
                          ┏━━━━━━ Python ━━━━━━┓
                          ┃ █  Seu programa  █ ┃
                          ┗━━━━━━━━━━━━━━━━━━━━┛
                            I/O     I/O    I/O
                             │       ┊      ┊
                             │  aguardando  ┊
           ┌───── REQUEST ───┘       ┊      └┄┄ aguardando ┄┄┐
           ▼                         ✕                       ✕
  ┏━━━━━ SERVER ━━━━━┓     ┌┈┈┈┈┈ tarefa ┈┈┈┈┈┐     ┌┈┈┈┈┈ tarefa ┈┈┈┈┈┐
  ┃ █  PREPARANDO  █ ┃     ┊ ╳   INTERFACE  ╳ ┊     ┊ ╳     API      ╳ ┊
  ┃ █   RESPONSE   █ ┃     ┊ ╳    TRAVADA   ╳ ┊     ┊ ╳ NÃO RESPONDE ╳ ┊
  ┗━━━ executando ━━━┛     └┈┈┈ aguardando ┈┈┈┘     └┈┈┈ aguardando ┈┈┈┘

  {df}
  {dii}Na ilustração, ao aguardar a resposta de uma requisição para um servidor, 
  nenhuma outra tarefa poderia ser executada sem concorrência.{df}
"""

teory_python_io_modules = f"""\
{hea}❯❯ asyncio e threading são soluções para I/O-Bound {df}
__L__
Em Python, podemos usar os módulos {acb} asyncio {df} e/ou {tcb} threading {df} 
para solucionar problemas I/O-bound. Cada um tem seus pontos fortes e fracos.
__L__ 
Quando digo {tc}threading{df}, estou me referindo ao módulo do Python mesmo. Mas, 
na maioria das vezes, uso {pur}concurrent.futures.ThreadPoolExecutor{df}.
__L__ 
Vou usar o nome {tc}threading{df} como qualquer módulo Python para threads.
"""

teory_threads = f"""\
{hea}❯❯ Threads em mais detalhes {df}
__L__
Múltiplas {tcb} Threads {df} podem estar ligadas a um único processo e trabalharem 
em conjunto para um objetivo. Isso permite resolver vários tipos de concorrência. 
__L__
Threads têm benefícios interessantes, se comparadas à criação de novos processos:
__L__
{star} Estão ligadas e compartilham recursos com o processo. Então são mais leves. __L__
{star} Sua comunicação é infinitamente mais fácil do que entre processos. __L__
{star} ⚠️⚠️ Conseguem trabalhar em paralelo em múltiplos núcleos da CPU  __L__
{star} Também podem trabalhar em multitarefas em um único núcleo 
__L__
Apesar de muito mais leves que processos, {bi}threads{df} também tem custo para o sistema. 
Por isso, criar threads {bi}onde não é necessário{df} deixa o {hi} código mais lento {df}.
__L__
Os Sistemas operacionais modernos são preemptivos. Então, fazem troca de contexto entre 
threads periodicamente. Isso tem custo, já que é necessário salvar e restaurar o 
contexto a cada troca {dii}(em inglês, context switch){df}.
__L__
Esse tipo de concorrência é chamado de {tcb} Multitarefa Preemptiva {df} e permite que 
um sistema execute 10 programas, em 2 núcleos da CPU, como se executassem ao mesmo tempo.
"""

teory_asyncio = f"""\
{hea}❯❯ asyncio em mais detalhes {df}
__L__
{acb} asyncio {df}, tem o {bi}comportamento cooperativo{df}, onde o desenvolvedor escolhe 
o momento para ceder o controle. Esse tipo de comportamento é chamado de 
{acb} Multitarefa Cooperativa {df} e alcança concorrência de forma inteligente.
__L__
Ao invés de múltiplas {bi}threads{df} (como vimos), {acb} asyncio {df}, roda em
uma {bi}única thread{df}. Da mesma forma que um script Python sem concorrência.
__L__
A concorrência acontece entre um {acb} Event Loop {df} (loop de eventos) e {bi}corrotinas{df}. 
__L__
Para quem conhece Python, corrotinas são funções criadas com {hi} async def {df}. 
Elas podem ceder o controle de volta para o Event Loop quando estão ocupadas.
__L__
Isso permite que, {bi}ao realizar operações I/O-bound{df}, uma corrotina ceda o 
controle para que o loop {bi}execute outra corrotina{df} que estiver pronta.
__L__
Isso é inteligente por não gerar overhead de criação de threads ou processos, nem 
trocas de contexto. {dii}(ocorre troca de contexto da thread única apenas){df}.
"""

teory_multitask_summary = f"""\
{hea}❯❯ asyncio e threads: um resumo sobre o que vimos{df}
__L__
{ac}asyncio{df} faz {bi}Multitarefa Cooperativa{df} e usa uma única thread. 
__L__
O próprio desenvolvedor decide o momento para pausar e/ou continuar.
__L__
Seu benefício também pode ser um problema. Se algo bloqueante for executado no 
{ac}Event Loop{df}, isso vai bloquear as outras corrotinas que estiverem prontas. 
__L__
Por isso, ou executamos tudo assíncrono (não bloqueante), ou movemos tudo o que for 
bloqueante para outra thread. {dii}(isso é bem simples de fazer){df}.
__L__
{tc}Threads{df} fazem {bi}Multitarefa Preemptiva{df} a nível de sistema operacional.
Ele decide quando pausar e/ou continuar usando seus critérios. O dev não decide isso.
__L__
Criar muitas {tcb} threads {df} mais a troca de contexto pode fazer uma tarefa ficar 
ainda mais lenta do que rodar o código sem concorrência. {dii}(precisamos testar){df}.
__L__
Outro fato que ainda não mencionei, mas faz {tc} TODA A DIFERENÇA {df}, é o GIL...
Vamos falar sobre isso na próxima tela 🔒...
"""

teory_the_gil = f"""\
{hea}❯❯ Threads são afetadas pelo {hi} GIL {df}{dii} (Global Interpreter Lock){df}.
__L__
{tcb} Nota: {df} {bi}desconsidere o GIL se você o desativar. (Python 3.14){df}
__L__
GIL é o Lock global do Python que {bi}não permite que threads do mesmo processo rodem 
ao mesmo tempo{df}.
__L__
Ele é um mecanismo de proteção do Python para evitar {dii}Race Conditions{df}.
__L__
Ironicamente, remover um lock global como o GIL, envolve a criação de outros locks 
de menor escopo em locais específicos. {bi}Isso deixará o Python mais lento.{df}
__L__
Tudo isso significa que, mesmo com várias threads, seu código pode se comportar 
como um código sem concorrência, mas com o peso das threads {dii}(que vimos antes){df}.
__L__
A boa notícia que é a solução veio no {hi} Python 3.14 {df} {dii}(já falo sobre isso){df}.
"""

teory_gil_analogy_one = f"""\
{hea}❯❯ Uma analogia para você entender o GIL (1/2){df}
__L__
Imagine as {hi} threads {df} como pessoas em uma festa.
__L__
A {hi} CPU {df} é o banheiro do local. 
__L__
Este banheiro é enorme e tem muitas cabines livres para diversas pessoas.
__L__
Só que a política da festa diz:
__L__
{hiy} PROIBIDO MAIS DE UMA PESSOA NO BANHEIRO {df}
__L__
Para garantir que a política será seguida, eles forçam que as {bi}pessoas levem 
a chave quando precisarem ir ao banheiro. E mais, também se tranquem por dentro{df}.
__L__
Uma pessoa só {hi} USA UMA CABIBE {df} e termina o serviço. 
__L__
Então, ela destranca a porta e pode sair.
__L__
Ao sair, ela olha para a fila e entrega a chave para a próxima pessoa (thread)
que estiver esperando para entrar.
"""

teory_gil_analogy_two = f"""\
{hea}❯❯ Uma analogia para você entender o GIL (2/2) {df}
__L__
O processo se repete para cada pessoa que entrar no banheiro.
__L__
Essa 🔑 chave da analogia, tem o comportamento do 🔒 GIL do Python. Percebe o 
desperdício de CPU, quando apenas uma thread pode usá-la por vez?
__L__
O Python {hi} libera o GIL {df} ao iniciar uma {bi}tarefa que vai aguardar por I/O{df}. 
Então, ele não seria um problema se usarmos {bi}threads em tarefas I/O-bound{df}.
Operações de I/O-bound, geralmente ocorrem em tempo sobreposto.
__L__
{bi}No paralelismo, o GIL SERIA UM PROBLEMA REAL{df} {dii}(adiante eu explico){df}.
__L__
{bi}Como tudo o que descrevi nesse texto todo, você precisa fazer testes.{df} 
"""

teory_a_new_python = f"""\
{hea}❯❯ A NOTÍCIA QUE MUDA TUDO PARA AS THREADS {df}
__L__
O {bi}Python 3.14 permite desativar o GIL{df} (simples e direto assim).
__L__
Só essa única frase já desfaz muito do que falei antes (teoricamente).
__L__
Essa versão do Python foi lançada há poucas semanas e fiz poucos testes sem o GIL.
Tive resultados promissores nesses testes que fiz, mas ainda é cedo para opinar.
__L__
Não fosse essa notícia, {bi}neste ponto eu estaria te explicando o motivo de você 
ser obrigado a criar vários processos{df} ao fazer paralelismo em Python.
__L__
Por falar em nisso, vamos ver o que é {hi} paralelismo e tarefas CPU-bound {df}.
"""

teory_cpu_bound = f"""\
{hea}❯❯ CPU-bound e Paralelismo{df}
__L__
Se {bi}I/O-bound{df} é um tempo de espera inútil que pode ser gasto com outra tarefa,
{hi} CPU-bound {df} são tarefas que envolvem gargalo de CPU ou de núcleo de CPU.
__L__
Exemplos comuns de tarefas CPU-bound envolvem:
__L__
{star} Edição e renderização de vídeos __L__
{star} Machine learning __L__
{star} Simulações e previsões complexas __L__
{star} Cálculos científicos __L__
{star} Criptografia 
__L__
Temos duas formas possíveis para solucionar este problema: 
__L__
{star} Múltiplos {pcb} Processos single thread {df} __L__
{star} Múltiplas {tcb} Threads do mesmo processo {df} 
__L__
As duas soluções envolvem múltiplos núcleos de CPU.
"""

teory_cpu_bound_graph = f"""\
{hea}❯❯ Exemplo de gargalo em um único núcleo{df}
__L__ {cya}
                          ┏━━━━━━ Python ━━━━━━┓
                          ┃ █  Seu programa  █ ┃
                          ┗━━━━━━━━━━━━━━━━━━━━┛
                            CPU     CPU    CPU
                             │       ┊      ┊
                             │    ocioso    ┊
           ┌── executando  ──┘       ┊      └┄┄┄┄ ocioso ┄┄┄┄┐
           ▼                         ✕                       ✕
  ┏━━━━ Uso 100% ━━━━┓     ┌┈┈┈┈┈ Uso 0% ┈┈┈┈┈┐     ┌┈┈┈┈┈ Uso 0% ┈┈┈┈┈┐
  ┃ █ Renderizando █ ┃     ┊     .........    ┊     ┊     .........    ┊
  ┃ █    Vídeo     █ ┃     ┊                  ┊     ┊                  ┊
  ┗━━━ no limite ━━━━┛     └┈┈┈┈┈ livre ┈┈┈┈┈┈┘     └┈┈┈┈┈ livre ┈┈┈┈┈┈┘
  {df}
  {dii}No exemplo acima, ao executar uma tarefa em um único núcleo da CPU, o problema 
  fica claro.{df}
"""

teory_cpu_bound_hardware = f"""\
{hea}❯❯ Operações CPU-bound são limitadas pelo hardware{df}
__L__
O tempo de espera {hi} não é inútil {df}. Pode ocorrer algum desperdício, mas por 
estarem operando em carga máxima ou por erro do programador. 
O fato é que o limite é a própria CPU (ou núcleo da CPU).
__L__
Só é possível resolver este problema se a CPU tem mais núcleos disponíveis. Do 
contrário, só um upgrade mesmo.
__L__
O tipo de concorrência onde usa-se vários núcleos da CPU ao mesmo tempo é chamado 
de {hi} paralelismo {df}.

"""
teory_io_vs_cpu_bound = f"""\
{hea}❯❯ Tempo sobreposto e Paralelismo (I/O-bound e CPU-bound){df}
__L__
No {tcb} tempo sobreposto {df} das multitarefas Cooperativa e Preemptiva, uma thread 
pode executar enquanto outra está ocupada. Pode ocorrer no mesmo núcleo da CPU ou 
até em uma mesma thread. Os tempos se sobrepõe. {dii} (asyncio e threads){df}.
__L__
No {pcb} paralelismo {df}, uma thread pode ser executada ao mesmo tempo que a 
outra em núcleos diferentes da CPU. Ocorre com várias threads do mesmo processo 
ou vários processos single thread.

"""

teory_io_vs_cpu_bound_graph_a = f"""\
{hea}❯❯ Multitarefa preemptiva e Paralelismo com threads{df}
__L__
{tcb} Na esquerda: {df} {dii}CPU single core{df} {bi}não faz paralelismo{df}, faz {tc}{bi}PREEMPÇÃO{df}.
{pcb} Na direita: {df} {dii}CPU multi core{df} executa threads {pc}{bi}AO MESMO TEMPO{df} em {dii}cores{df} diferentes{df}.
__L__
{tc}  Multitarefa Preemptiva              {df}{pc}   Paralelismo (⚠️ GIL)
{tc}  (mesmo proc. e core, várias threads){df}{pc}   (mesmo proc., várias threads e cores)
{tc}  
{tc}  Core 1 / Proc. 1 / Thread 1         {df}{pc}    Core 1 / Proc. 1 / Thread 1
{tc}  ██░░░░░░░░████░░░░░░░░░░░██         {df}{pc}    █████████████████████
{tc}  Core 1 / Proc. 1 / Thread 2         {df}{pc}    Core 2 / Proc. 1 / Thread 2
{tc}  ░░██░░░░░█░░░░███░░░░██             {df}{pc}    ███████████████████████████
{tc}  Core 1 / Proc. 1 / Thread 3         {df}{pc}    Core 3 / Proc. 1 / Thread 3
{tc}  ░░░░░░██░░░░░░░░░░░██░░██           {df}{pc}    █████████████████████████
{tc}  Core 1 / Proc. 1 / Thread 4         {df}{pc}    Core 4 / Proc. 1 / Thread 4
{tc}  ░░░░██░░█░░░░░░░░██                 {df}{pc}    ███████████████████████
{tc}              ▼                       {df}{pc}                ▼
{tc}  ███████████████████████████         {df}{pc}    ███████████████████████████
{tc}  Percepção do usuário: tudo          {df}{pc}    Tudo realmente aconteceu ao
{tc}  aconteceu ao mesmo tempo            {df}{pc}    mesmo tempo.
{df}
"""

teory_io_vs_cpu_bound_graph_b = f"""\
{hea}❯❯ Multitarefa cooperativa e Paralelismo com múltiplos processos{df}
__L__
{acb} Na esquerda: {df} {dii}mesmo processo, core e thread{df}, código {ac}{bi}assíncrono{df} {dii}(concorrente){df}.
{pcb} Na direita: {df} {dii}múltiplos processos single-thread{df} executando {pc}{bi}AO MESMO TEMPO{df} {dii}(paralelismo){df}.
__L__
{ac}  Multitarefa Cooperativa             {df}{pc}   Paralelismo (✅ GIL)
{ac}  (mesmo proc., core e thread)        {df}{pc}   (vários procs. single thread)
{ac}  
{ac}  Core 1 / Proc. 1 / Thread 1         {df}{pc}    Core 1 / Proc. 1 / Main Thread
{ac}  ██░░░░░░░░████░░░░░░░░░░░██         {df}{pc}    █████████████████████
{ac}  Core 1 / Proc. 1 / Thread 1         {df}{pc}    Core 2 / Proc. 2 / Main Thread
{ac}  ░░██░░░░░█░░░░███░░░░██             {df}{pc}    ███████████████████████████
{ac}  Core 1 / Proc. 1 / Thread 1         {df}{pc}    Core 3 / Proc. 3 / Main Thread
{ac}  ░░░░░░██░░░░░░░░░░░██░░██           {df}{pc}    █████████████████████████
{ac}  Core 1 / Proc. 1 / Thread 1         {df}{pc}    Core 4 / Proc. 4 / Main Thread
{ac}  ░░░░██░░█░░░░░░░░██                 {df}{pc}    ███████████████████████
{ac}              ▼                       {df}{pc}                ▼
{ac}  ███████████████████████████         {df}{pc}    ███████████████████████████
{ac}  Percepção do usuário: tudo          {df}{pc}    Tudo realmente aconteceu ao
{ac}  aconteceu ao mesmo tempo            {df}{pc}    mesmo tempo.
{df}
"""
teory_io_vs_cpu_bound_graph_a = f"{cya}{teory_io_vs_cpu_bound_graph_a}"

teory_parallelism = f"""\
{hea}❯❯ GIL e o paralelismo{df}
__L__
Nessa altura do vídeo, eu devo ter falado do GIL e paralelismo umas 5 vezes. 
__L__
Mas para oficializar: {bi}não tem como fazer paralelismo com threads do mesmo 
processo com o GIL ativo.{df}
__L__
A {bi}única opção{df} que eu tinha para {bi}paralelismo{df} no Python em versões 
anteriores era {hi} criando vários processos {df} ou usando outra implementação.
__L__
Se eu manter a {bi}main thread do processo{df} e criar vários processos 
o {hi} GIL não é um problema {df}, já que processos são isolados.
__L__
Isso funcionou assim por anos, mas o {bi}custo é enorme{df}.
"""

teory_proccess_pain = f"""\
{hea}❯❯ Qual o problema de vários processos?{df}
__L__
Vamos lembrar algumas coisas que falei nesse mesmo vídeo:
__L__
{star} Um {bi}processo é isolado{df} de outros processos do sistema. Tem como fazer
  comunicação entre processos (IPC), {bi}mas envolve muita complexidade{df}. A sincronização
  de dados em concorrência já é complexa por si só. Se a comunicação é entre processos, 
  {bi}nós estamos tratando de um dos assuntos mais complexo da programação{df}. __L__
{star} Um {bi}processo não é algo trivial para o sistema{df}. Se custa caro subir um único
  processo, imagine vários. __L__
{star} Se o Python vai rodar em outro processo, significa que eu {bi}preciso de outro
  interpretador{df} no outro processo. É quase o mesmo que eu recarregar a o
  programa do zero (outro custo). __L__
{star} Os {bi}dados precisam ser serializados{df}. Não é qualquer tipo de dado que pode
  usado com processos.
"""
teory_new_interpreters = f"""\
{hea}❯❯ Subinterpreters (concurrent interpreters){df}
__L__
Vou fazer uma menção honrosa aos {hi} Concurrent Interpreters {df} do Python 3.14.
__L__
Creio que esse não é o nome deles, mas estou usando este nome por estar usando 
{pur}concurrent.futures.InterpreterPoolExecutor{df} para subir vários interpretadores 
ao mesmo do Python de forma concorrente. 
__L__
Eles {hi} também fazem paralelismo {df} no Python e são bem promissores.
__L__
A documentação fala sobre eles como tendo todos os benefícios das threads mas com 
comportamento de processos. 
__L__
Tudo o que te expliquei sobre os processos, funciona de forma similar nos interpretadores. 
__L__
Eles são isolados e seguros como os processos. O comportamento de thread é pelo fato 
de {hi} eles rodarem no mesmo processo {df}. 
__L__
O único problema que percebi com os interpretadores até agora, é que eles {bi}ainda 
consomem muita memória{df}. Mas a documentação já indicou que estão trabalhando 
ativamente neste recurso.
__L__
Quem sabe eu consiga encaixar eles nesses vídeos sobre concorrência? Me ajuda aí!
"""
teory_end = f"""\
{hea}❯❯ E finalmente chegamos ao fim...{df}
__L__
Agora, terminando esse texto enorme que fui perceber. Escrevi um artigo inteiro 
só em comentários do Python. Inicialmente, achei que teríamos código 🤣.
__L__
Quando você for assistir ao vídeo, isso já deverá estar bem diferente. Pretendo 
usar asyncio para fazer uma espécie de slides e depois te mostrar o código.
__L__
Não sei se vai dar certo, mas vou manter isso aqui para a posteridade.
__L__
No mais... Obrigado por chegar até o final {red}s2{df}.
__L__
Fim...
"""

concurrency_teory: Sequence[str] = [
    teory_intro,
    teory_non_concurrent_python,
    teory_char_process,
    teory_char_threads,
    teory_char_threads_graph,
    teory_diff_python,
    teory_diff_python_bytecode,
    teory_diff_python_graph,
    teory_chars_summary,
    teory_concurrency_bounds,
    teory_io_bound,
    teory_io_bound_graph,
    teory_python_io_modules,
    teory_threads,
    teory_asyncio,
    teory_multitask_summary,
    teory_the_gil,
    teory_gil_analogy_one,
    teory_gil_analogy_two,
    teory_a_new_python,
    teory_cpu_bound,
    teory_cpu_bound_graph,
    teory_cpu_bound_hardware,
    teory_io_vs_cpu_bound,
    teory_io_vs_cpu_bound_graph_a,
    teory_io_vs_cpu_bound_graph_b,
    teory_parallelism,
    teory_proccess_pain,
    teory_new_interpreters,
    teory_end,
]
