import numpy as np  # Para gerar os lançamentos dos dados e manipular arrays
import matplotlib.pyplot as plt  # Para plotar os histogramas

# Comentário:
# `numpy` nos permite gerar números aleatórios de forma eficiente.
# `matplotlib` será usada para criar o histograma com a função `plt.stairs`.

# Função para simular a soma de M dados em N lançamentos
def simular_dados(M, N):
    # Gerando N lançamentos de M dados com valores entre 1 e 6
    resultados = np.random.randint(1, 7, size=(N, M))
    
    # Calculando a soma S para cada lançamento
    somas = np.sum(resultados, axis=1)
    
    return somas


#np.random.randint(1, 7, size=(N, M))` gera uma matriz de N linhas e M colunas,
# onde cada valor é o resultado do lançamento de um dado (de 1 a 6).
# np.sum(resultados, axis=1)` soma os resultados de cada linha (ou seja, soma os M dados de cada lançamento).

# Função para plotar o histograma da soma dos dados
def plotar_histograma(somas, N, M):
    # Criando o histograma
    counts, bins = np.histogram(somas, bins=range(M, 6 * M + 2))

    # Plotando o histograma
    plt.stairs(counts, bins)
    plt.title(f'Histograma da soma de {M} dados em {N} lançamentos')
    plt.xlabel('Soma dos dados')
    plt.ylabel('Frequência')
    plt.show()

# Comentário:
# `np.histogram(somas, bins=range(M, 6 * M + 2))` calcula o histograma das somas.
# Os valores de bins vão de M (a menor soma possível) até 6 * M (a maior soma possível).
# `plt.stairs(counts, bins)` desenha o gráfico de barras do histograma.

# Definindo diferentes valores de N e M para testar
valores_N = [10**2, 10**3, 10**4]  # Diferentes números de lançamentos
valores_M = [2, 4, 8]  # Diferentes números de dados por lançamento

# Loop para testar todos os valores de N e M
for N in valores_N:
    for M in valores_M:
        somas = simular_dados(M, N)
        plotar_histograma(somas, N, M)

# Comentário:
# Estamos testando com valores de N que variam de 100 a 10.000 e M variando de 2 a 8 dados.
# A cada combinação, geramos as somas dos dados e plottamos o histograma correspondente.







import numpy as np
import matplotlib.pyplot as plt

#fazendo uma função com o algortimo de monte carlo para calcular o valor de PI;
def montecarlo(realizacoes, tentativas):
    resultados = {N: [] for N in realizacoes}
    for N in realizacoes:
        #Coloquei _ nos dois for porque estava dando conflito se colocasse a letra i;
        for _ in range(tentativas):
            Nc = 0     
            # Definição da uniformidade dos pontos a serem colocados no gráfico (que o professor explicou sobre o algoritmo de monte carlo);
            for _ in range(N):
                x = -1.0 + 2.0 * np.random.rand()
                y = -1.0 + 2.0 * np.random.rand()
                if (x*2 + y*2 < 1.0):
                    Nc += 1
            # Realizando os cálculos para obtenção de PI
            Prob = Nc / N
            estimativa = 4 * Prob
            resultados[N].append(estimativa)

    return resultados

# Definindo as variáveis da função montecarlo()
realizacoes = [10*2, 103, 104, 105, 10*6]
tentativas = 6

pi = montecarlo(realizacoes, tentativas)

# Criando array estruturado para fazer a tabela
dtype = [('Tentativa', 'i4')] + [(f'N={N}', 'f4') for N in realizacoes]
data = np.zeros((tentativas,), dtype=dtype)

for i in range(tentativas):
    data[i]['Tentativa'] = i + 1
    for j, N in enumerate(realizacoes):
        data[i][f'N={N}'] = pi[N][i]

# Calculando o desvio padrão para cada coluna (excluindo a coluna "Tentativa")
desvio_padrao = {name: np.std(data[name]) for name in data.dtype.names if name != 'Tentativa'}

# Criando um gráfico log-log para o desvio padrão
plt.figure(figsize=(10, 6))
plt.loglog(realizacoes, list(desvio_padrao.values()), marker='o', label='Desvio Padrão')

# Calculando e plotando N^(-1/2) que será nosso parâmetro de acerto do código, já que esse tracejado nos dá o valor teórico do desvio padrão de PI
N_values = np.array(realizacoes)
n_half_inverse = N_values ** (-0.5)
plt.loglog(N_values, n_half_inverse, label='N^(-1/2)', linestyle='--')

# Configuran gráfico
plt.title('Desvio Padrão da Estimativa de π e N^(-1/2)')
plt.xlabel('N (número de pontos)')
plt.ylabel('Desvio Padrão da Estimativa de π')
plt.grid(True)
plt.legend()
plt.show()






import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(1 - x**2)  # Função: f(x) = sqrt(1 - x^2)

def soma_riemann(n):
    delta_x = 1 / n  # Delta x definido como 1/n
    soma = 0
    
    for i in range(n):
        x_i = i * delta_x  # Ponto à esquerda
        soma += f(x_i) * delta_x
        
    return soma

# Definições
n_values = [1000, 2000, 3000, 4000, 5000]  # Vários valores de n
erros = []

#Valor real de pi
pi_real = np.pi

# Cálculo da soma de Riemann e do erro para cada n
for n in n_values:
    soma_esquerda = soma_riemann(n)
    soma_esquerda *= 4  # Multiplicar o resultado por 4
    erro = abs(soma_esquerda - pi_real)  # Cálculo do erro
    erros.append(erro)  # Armazenar o erro
    print(f"Valor de pi para n={n}: {soma_esquerda}, Erro: {erro}")

# Plotar os erros em função de n
plt.figure(figsize=(10, 6))
plt.plot(n_values, erros, marker='o')
plt.yscale('log')  # Usar escala logarítmica para melhor visualização
plt.title('Erro na Estimativa de π em Função de n')
plt.xlabel('Número de Subintervalos (n)')
plt.ylabel('Erro (log escala)')
plt.xticks(n_values)  # Exibir todos os valores de n
plt.grid()
plt.show()





import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Definindo as funções
def f(x):
    return 1 + 0.5 * np.sin(2 * x)**3

def g(x):
    return 3 + 0.5 * np.cos(3 * x)**5

# Definindo variáveis simbólicas para a área
x_sym = sp.symbols('x')
f_sym = 1 + 0.5 * sp.sin(2 * x_sym)**3
g_sym = 3 + 0.5 * sp.cos(3 * x_sym)**5
area_sym = sp.integrate(g_sym - f_sym, (x_sym, 0, 2 * sp.pi))

# Método de Monte Carlo
def monte_carlo_area(f, g, x_range, num_samples):
    x_samples = np.random.uniform(*x_range, num_samples)
    y_min = min(f(x_range[0]), g(x_range[0]))
    y_max = max(f(x_range[1]), g(x_range[1]))
    y_samples = np.random.uniform(0, 3.5, num_samples)
    inside_count = (y_samples <= g(x_samples)) & (y_samples >= f(x_samples))
    
    area_mc = (np.sum(inside_count) / num_samples) * (x_range[1] - x_range[0]) * (y_max - y_min)
    return area_mc, x_samples, y_samples, inside_count

# Parâmetros
x_range = (0, 2 * np.pi)
num_samples = 100000

# Cálculo usando o método de Monte Carlo
area_mc, x_samples, y_samples, inside_count = monte_carlo_area(f, g, x_range, num_samples)

# Visualização
plt.figure(figsize=(12, 7))

# Plotando as curvas
x_vals = np.linspace(0, 2 * np.pi, 500)
plt.plot(x_vals, f(x_vals), label='f(x) = 1 + 0.5 * sin^3(2x)', color='black')
plt.plot(x_vals, g(x_vals), label='g(x) = 3 + 0.5 * cos^5(3x)', color='black')

# Plotando os pontos de Monte Carlo
plt.plot(x_samples[inside_count], y_samples[inside_count], 'go', markersize=2, alpha=0.4, label='Dentro da área')
plt.plot(x_samples[~inside_count], y_samples[~inside_count], 'ro', markersize=2, alpha=0.4, label='Fora da área')

# Definindo os limites do gráfico
plt.xlim(0, 2 * np.pi)
plt.ylim(0.5, 3.5)

plt.title('Região com Pontos de Monte Carlo e Curvas f(x) e g(x)', fontsize=20)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.grid()
plt.legend()
plt.show()




import numpy as np
import matplotlib.pyplot as plt

#usamos as funções do exercício 4
#as funções devem receber x como argumento
def f(x):
    return 1 + 0.5 * np.sin(2*x)**3

def g(x):
    return 3 + 0.5 * np.cos(3*x)**5

#agora tem que plotar as parábolas da esquerda e da direita nos pontos x e y
#numpy tem uma função pronta para funções polinomiais
#ela aceita 3 argumentos, os valores para x, para y e o grau do polinômio
parabola_esquerda = np.polyfit([0, -1, 0.5], [1, 2.25, 3.5], 2)
                    #[0, -1, 0.5] são os pontos de x
                    #[1, 2.25, 3.5] é os pontos de y
                    #2 é o grau do polinômio

#agora vamos plotar a parábola da direita
parabola_direita = np.polyfit([2 * np.pi, 2 * np.pi + 1, 2 * np.pi + 2.25], [1, 2.25, 3.5], 2)
                    #2 vezes pi 
                    #2 vezes pi mais 1,2 vezes 2.25
                    #grau 2 do polinômio

#agora a gente precisa calcular o valor dessas funções nesses pontos
#numpy.polyval faz isso
#essa função em especial avalia os pontos dados e a função

def parabola_esquerda_func(x):
    return np.polyval(parabola_esquerda, x)

def parabola_direita_func(x):
    return np.polyval(parabola_direita, x)

def plot_monte_carlo(N):
    # Gerar N pontos aleatórios
    x_random = np.random.uniform(-1, 2 * np.pi + 1, N)
    y_random = np.random.uniform(1, 3.5, N)

    # Identificar os pontos dentro e fora da região
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for i in range(N):
        if f(x_random[i]) <= y_random[i] <= g(x_random[i]):
            if (x_random[i] <= 0 and y_random[i] <= parabola_esquerda_func(x_random[i])) or \
               (x_random[i] >= 2 * np.pi and y_random[i] <= parabola_direita_func(x_random[i])):
                x_inside.append(x_random[i])
                y_inside.append(y_random[i])
            else:
                x_outside.append(x_random[i])
                y_outside.append(y_random[i])

    # Plotar os pontos
    plt.scatter(x_inside, y_inside, color='green', label='Pontos dentro')
    plt.scatter(x_outside, y_outside, color='red', label='Pontos fora')

# Plotando as funções f(x) e g(x)
x = np.linspace(0, 2 * np.pi, 1000)
plt.plot(x, f(x), label='f(x)', color='blue')
plt.plot(x, g(x), label='g(x)', color='black')

# Plotando as parábolas
x_left = np.linspace(-1, 0.5, 100)
x_right = np.linspace(2 * np.pi, 2 * np.pi + 1, 100)

plt.plot(x_left, parabola_esquerda_func(x_left), label='Parábola Esquerda', color='red')
plt.plot(x_right, parabola_direita_func(x_right), label='Parábola Direita', color='green')

# Chamando a função para plotar os pontos Monte Carlo
plot_monte_carlo(1000)

# Configurando o gráfico
plt.title('Região delimitada pelas funções e parábolas')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()




import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Valores de N para testar
valores_N = [10**3, 10**4, 10**5]  #Diferentes números de pontos
resultados_pi = []
erros = []
pi_real = np.pi

for N in valores_N:
    #gerando valores para x,y,z
    #exercício pediu no intervalo -1 e 1
    x = np.random.uniform(-1, 1, N)
    y = np.random.uniform(-1, 1, N)
    z = np.random.uniform(-1, 1, N)
    
    #testando um valor pequeno para ver como fica
    for i in range(5):
        print(f'Ponto {i+1}: (x={x[i]}, y={y[i]}, z={z[i]})')

    #agora tenho que saber a distância
    #d=\sqrt{x²+y²+z²}

    #d = raiz quadrada de x+y+z elevado ao quadrado
    distancias = np.sqrt(x**2 + y**2 + z**2)

    #se d<=1 está dentro da esfera
    numeros_dentro = distancias <= 1

    #agora contar o numero de pontos dentro dessa esfera e somar
    pontos_dentro = np.sum(numeros_dentro)

    print(f'Número de pontos dentro da esfera: {pontos_dentro}')
    print(f'Número total de pontos: {N}')

    #o volume de um cubo de lado 2: 2³ = 8
    #volume da esfera de raio 1: 4/3.pi 

    #volume da esfera/volume do cubo é proporcional à razão pontos de dentro/ponto total
    #Vol esfera / Vol do cubo = 4/3pi/8 = pi/6

    #aproxima o pi aqui
    pi_aproxim = 6 * (pontos_dentro / N)

    #calcular o erro relativo
    erro_relativo = abs((pi_aproxim - pi_real) / pi_real)
    erros.append(erro_relativo)
    resultados_pi.append(pi_aproxim)

    print(f'N = {N}, π aproximado = {pi_aproxim:.6f}, Erro relativo = {erro_relativo:.6f}')

    #agora plotar em 3d com a lib que chamamos lá em cima
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x[numeros_dentro], y[numeros_dentro], z[numeros_dentro], color='black', alpha=0.5, label='Dentro da esfera')

    #Plotar os pontos fora da esfera em vermelho
    ax.scatter(x[~numeros_dentro], y[~numeros_dentro], z[~numeros_dentro], color='red', alpha=0.5, label='Fora da esfera')

    #Adicionar rótulos aos eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    #Adicionar uma legenda
    ax.legend()

    #Mostrar o gráfico
    plt.show()

#Plotando o erro em função de N
plt.figure()
plt.loglog(valores_N, erros, marker='o')
plt.xlabel('Número de Pontos (N)')
plt.ylabel('Erro Relativo')
plt.title('Erro Relativo na Aproximação de π em Função de N')
plt.grid(True)
plt.show()





import numpy as np
import matplotlib.pyplot as plt

#se i=0 é ponto inicial
#a posição tem que ser aleatório então usa um random aqui
#np.random.choice 
#como é em 2 dimensões, preciso gerar n passos

def n_passos(N):
    #preciso criar uma array de posição N e com 2 colunas (pensando em x,y)
   posicao = np.zeros((N, 2))

    #se i=0 é ponto inicial
    #a posição tem que ser aleatório então usa um random aqui
    #np.random.choice 
    
    #norte = +1 para y
    #sul = -1 para y
    #leste = +1 para x
    #oeste = -1 para x
   for i in range(1, N):
      passo = np.random.choice(['norte', 'sul', 'leste', 'oeste'])

      if passo == 'norte':
         posicao[i] = posicao[i-1] + [0, 1]   # Mover no eixo Y positivo
      elif passo == 'sul':
         posicao[i] = posicao[i-1] + [0, -1]  # Mover no eixo Y negativo
      elif passo == 'leste':
         posicao[i] = posicao[i-1] + [1, 0]   # Mover no eixo X positivo
      elif passo == 'oeste':
         posicao[i] = posicao[i-1] + [-1, 0]  # Mover no eixo X negativo

   return posicao 

#como sao m caminhadas aleatorias de n passos
#vou tentar essa quantidade de passos para ver se está errado
N = 1000 

posicoes = n_passos(N)

plt.figure(figsize=(6, 6))
plt.plot(posicoes[:, 0], posicoes[:, 1], color='black', alpha=0.7)
plt.title("caminhada aleatória em 2d")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.grid(True)
plt.show()


        