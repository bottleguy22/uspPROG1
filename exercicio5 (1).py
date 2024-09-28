import numpy as np
import matplotlib.pyplot as plt

# Definindo variáveis para o diagrama de bifurcação proveniente do mapa logístico;
R = np.linspace(0, 4, 30000)

"""Aqui usamos uma variável, denominada 'R', que é quase idêntica a 'valores_a' por motivos de rapidez
de execução, pois para aparecer as bifurcações é necessário um tamanho altíssimo da sequência;"""

X = []
Y = []

"""Esse laço armazena os parâmetros de controle da sequência em uma variável enquanto armazena
o resultado do algoritmo na outra;"""
for r in R:
    X.append(r)

    x = np.random.random()

    for n in range(100):
        x = r*x*(1-x)
    Y.append(x)
'''Aqui existem dois 'for' pois os dados mais velhos não se alteram tanto e o gráfico fica monótono.
O que acontece é um for correndo até cem e o outro apagando esses cem e correndo de novo, dessa vez
sem apagar nada;'''

# Plotagem do gráfico de bifurcação.
plt.plot(X, Y, ls='', marker='o', markersize=0.5)
plt.show()
