import numpy as np
import matplotlib.pyplot as plt

# Definimos uma função para guardar a conta do mapa;
def mapa_logistico(a, x):
    return a*x*(1-x)

# Definindo variáveis;
valores_a = np.linspace(0, 4, 200)
x0 = 0.1
N = 5000

# Esse laço serve para criar uma lista vazia e colocar os números da sequência dentro;
for a in valores_a:
    x = np.zeros(N)
    x[0] = x0

    for i in range(1, N):
            x[i] = mapa_logistico(a, x[i-1])
    plt.plot(range(N), x[-N:], label=f'a = {a}')

#Média e variancia usando numpy;
mediapy = np.median(x)
varianciapy = np.var(x)

#Média e variancia usando somente python;

media = sum(x)/N

var = np.zeros(N)

for i in x:
     var = (x - media)**2

variancia = sum(var)/(N-1)

# Printando os dois métodos para comparar o resultado;
print(f'Média numpy - {mediapy} \n Média normal - {media}')
print(f'Variança numpy - {varianciapy} \n Variança normal - {variancia}')

# Plotando o gráfico da sequência númerica dada pelo laço;
plt.title('Sequência do Mapa Logístico para Diferentes Valores de a')
plt.xlabel('N')
plt.ylabel('x')
plt.xscale('log')
plt.grid(True)
plt.show()
