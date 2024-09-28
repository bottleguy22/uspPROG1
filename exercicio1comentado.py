#https://www.geeksforgeeks.org/matrix-multiplication-in-numpy/
#curso de matplotlib https://www.youtube.com/watch?v=3Xc3CA655Y4
#stackoverflow pra tirar dúvida ou achar soluções para dúvidas https://stackoverflow.co/


import numpy as np  #lib para trabalhar com matrizes e números
import time  #lib para medir o tempo que as operações demoram
import matplotlib.pyplot as plt  #lib para fazer gráficos
import random  #lib para gerar números inteiros aleatórios

#Função para realizar a combinação linear de vetores/matrizes
def combinacao_linear(m, n):
    vetor_vazio = np.zeros((m, n), dtype=np.float64)  #Cria uma matriz cheia de zeros com o formato m por n
    vet1 = np.random.rand(m, n)  #Gera uma matriz de tamanho m por n com números aleatórios
    vet2 = np.random.rand(m, n)  #Gera outra matriz do mesmo tamanho com números aleatórios
    al = random.randint(1, 10)  #Escolhe um número aleatório entre 1 e 10
    be = random.randint(1, 10)  #Escolhe outro número aleatório entre 1 e 10
    
    tinicial = time.time()  #Guarda o tempo no começo da operação
    vetor_vazio += al * vet1 + be * vet2  #Faz a combinação linear: multiplica vet1 por al e vet2 por be, depois soma os dois
    tfinal = time.time()  #Guarda o tempo no final da operação
    
    return tfinal - tinicial  #Retorna o tempo total gasto na combinação linear



#Função para multiplicar uma matriz por ela mesma várias vezes (elevar à potência)
def multiplicacao_matrizes(a):
    matriz_1 = np.random.rand(a, a)  #Gera uma matriz quadrada (mesmo número de linhas e colunas) com valores aleatórios
    
    tempoinicio = time.time()  #Guarda o tempo no início da operação
    m_saida = np.linalg.matrix_power(matriz_1, a)  #Eleva a matriz à potência a usando uma função própria do NumPy
    tempofinal = time.time()  #Guarda o tempo no final da operação
    
    return tempofinal - tempoinicio  #Retorna o tempo total gasto na potenciação



#Função para calcular c = αa + βb, uma combinação linear entre dois vetores a e b
def calc_c(alpha, beta, a, b):
    return alpha * a + beta * b  #Multiplica a por alpha e b por beta, depois soma os dois



#Função para calcular a potência m de uma matriz, de forma direta
def calc_matrix_power(A, m):
    return np.linalg.matrix_power(A, m)  #Utiliza uma função própria do NumPy para elevar a matriz à potência m



#Função para medir o tempo de execução das operações e gerar gráficos comparando os tempos
def measure_and_plot():
    #Vetor com diferentes tamanhos para a combinação linear
    n_values_linear = [10**5, 10**6, 10**7, 10**8]  #Lista de diferentes tamanhos de vetores (em notação científica)
    
    #Vetor com diferentes tamanhos para as matrizes quadradas
    m_values_matriz = [500, 1000, 1500, 2000]  #Lista com tamanhos variados de matrizes quadradas
    m_values_power = [2, 3, 4]  #Lista com diferentes valores de potência

    #Mede o tempo que cada combinação linear leva para ser feita
    tempos_linear = [combinacao_linear(1, n) for n in n_values_linear]  #Chama a função para cada tamanho de vetor e guarda os tempos

    #Mede o tempo de potenciação de matrizes (elevar à potência)
    tempos_matriz = [multiplicacao_matrizes(m) for m in m_values_matriz]  #Chama a função para cada tamanho de matriz e guarda os tempos

    #Mede o tempo de c = αa + βb
    times_vec = []
    for n in n_values_linear:
        a = np.random.rand(n)  #Gera um vetor aleatório de tamanho n
        b = np.random.rand(n)  #Gera outro vetor aleatório do mesmo tamanho
        alpha = np.random.rand()  #Escolhe um valor aleatório para alpha
        beta = np.random.rand()  #Escolhe um valor aleatório para beta

        start_time = time.time()  #Guarda o tempo no início
        c = calc_c(alpha, beta, a, b)  #Calcula c = αa + βb
        end_time = time.time()  #Guarda o tempo no final

        times_vec.append(end_time - start_time)  #Guarda o tempo gasto na operação

    #estamos medindo o tempo necessário para calcular a potência de várias matrizes de diferentes tamanhos 
    # e guardando esses tempos em um dicionário.
 
    
    #aqui tem alguns detalhes DIFÍCEIS
    #O loop externo (for n in m_values_matriz) controla o tamanho das matrizes
    #O loop interno (for m in m_values_power) controla as potências para cada matriz
    #O loop externo percorre cada linha , e o loop interno percorre cada elemento dentro da linha
    #AQUI TEM QUE TESTAR VÁRIOS TAMANHOS DE MATRIZES e ELEVANDO A CADA POTENCIA (2,3,4)
    #O loop externo cuida dos diferentes tamanhos de matriz, e o loop interno cuida das potências para essas matrizes. 
    

    times_mat = {m: [] for m in m_values_power}  #cria algo como: {2: [], 3: [], 4: []} essas listas vão ser preenchidas com tempo
    for n in m_values_matriz: #aqui controla o tamanho dessa matriz, vai ter que gerar ela pra tamanho n em seguida

        A = np.random.rand(n, n)  #Gera uma matriz quadrada de tamanho n
        for m in m_values_power:
            start_time = time.time()  #Guarda o tempo no início
            Am = calc_matrix_power(A, m)  #Calcula A elevado à m
            end_time = time.time()  #Guarda o tempo no final

            times_mat[m].append(end_time - start_time)  #Guarda o tempo gasto na operação



#plotei em vermelho pra ficar diferente, facilita visualização

# Gráficos para combinação linear e c = αa + βb
    plt.figure(figsize=(12, 6))  #Define o tamanho da figura (janela) como 12 de largura e 6 de altura
    plt.subplot(1, 2, 1) #Cria o primeiro gráfico de uma janela dividida em 2 colunas
    plt.plot(n_values_linear, tempos_linear, marker='o', color='red')  
    plt.xlabel('Dimensão n')
    plt.ylabel('Tempo (s)')
    plt.grid(True)
    plt.title('Tempo para calcular combinação linear vs Dimensão n (Escala Linear)')
    
    plt.subplot(1, 2, 2)  #Cria o segundo gráfico da janela, na segunda coluna
    plt.loglog(n_values_linear, times_vec, marker='o', color='black') #gráfico de linha em escala log-log, com bolinhas azuis para os pontos
    plt.xlabel('Dimensão n')
    plt.ylabel('Tempo (s)')
    plt.grid(True)
    plt.title('Tempo para calcular c = αa + βb vs Dimensão n (Escala Log-Log)')
    plt.tight_layout()
    plt.show()

    # Gráfico para potenciação de matrizes
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(m_values_matriz, tempos_matriz, marker='o', color='red')
    plt.xlabel('Dimensão m')
    plt.ylabel('Tempo (s)') 
    plt.grid(True)     #Adiciona uma grade ao gráfico
    plt.title('Tempo para calcular A^a vs Dimensão m') #Define o título do gráfico

    plt.subplot(1, 2, 2)
    for m in m_values_power:
        plt.plot(m_values_matriz, times_mat[m], marker='o', label=f'm = {m}') #Desenha uma linha no gráfico para cada valor de m, com bolinhas nos pontos e uma legenda para identificar o valor de m
    plt.xlabel('Dimensão m') #Define o rótulo do eixo x como "Dimensão m"
    plt.ylabel('Tempo (s)')  #Define o rótulo do eixo y como "Tempo (s)"
    plt.title('Tempo para calcular A^m vs Dimensão m (Escala Log-Log)')
    plt.legend()      #Adiciona uma legenda ao gráfico para mostrar os valores de m
    plt.grid(True)    #Adiciona uma grade ao gráfico
    plt.show()        #Exibe os gráficos na tela

measure_and_plot()
