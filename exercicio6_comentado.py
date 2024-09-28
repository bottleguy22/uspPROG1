import numpy as np  # Importa o pacote numpy para trabalhar com números e tabelas
import matplotlib.pyplot as plt  # Importa a ferramenta para desenhar gráficos

#Cria uma tabela de zeros para representar o grafo (as conexões entre os pontos)
def cria_grafo(vertices):
    return np.zeros((vertices, vertices), dtype=int)  #Cria uma tabela com o número de pontos (vertices)

#Adiciona uma conexão (aresta) entre dois pontos (u e v)
def adiciona_aresta(grafo, u, v):
    #Verifica se os pontos existem
    if 1 <= u <= len(grafo) and 1 <= v <= len(grafo):
        #Adiciona a conexão (aresta) entre u e v
        grafo[u-1][v-1] = 1  #Marca a conexão do ponto u para o ponto v
        grafo[v-1][u-1] = 1  #Marca a conexão do ponto v para o ponto u (conexão nos dois sentidos)
    else:
        #Mostra erro se os pontos não existirem
        print(f"Erro: Vértices {u} ou {v} estão fora do intervalo.")

#Remove uma conexão (aresta) entre dois pontos
def remove_aresta(grafo, u, v):
    #Verifica se os pontos existem
    if 1 <= u <= len(grafo) and 1 <= v <= len(grafo):
        #Remove a conexão entre os dois pontos, voltando o valor a zero
        grafo[u-1][v-1] = 0  #Remove a conexão do ponto u para o ponto v
        grafo[v-1][u-1] = 0  #Remove a conexão do ponto v para o ponto u
    else:
        #Mostra erro se os pontos não existirem
        print(f"Erro: Vértices {u} ou {v} estão fora do intervalo.")

#Remove um ponto (e todas as suas conexões) do grafo
def remove_no(grafo, coordenadas, no):
    #Verifica se o ponto existe
    if 1 <= no <= len(grafo):
        #Remove as conexões do ponto
        grafo[no-1] = 0  #Remove todas as conexões do ponto na linha
        grafo[:, no-1] = 0  #Remove todas as conexões do ponto na coluna
        
        #Remove o ponto da tabela
        grafo = np.delete(grafo, no-1, axis=0)  #Remove a linha do ponto
        grafo = np.delete(grafo, no-1, axis=1)  #Remove a coluna do ponto
        coordenadas = np.delete(coordenadas, no-1, axis=0)  #Remove as coordenadas do ponto
        
        #Verifica se algum ponto ficou sem conexões e remove ele também
        i = 0
        while i < len(grafo):
            if np.sum(grafo[i]) == 0:  #Se o ponto não tiver nenhuma conexão
                grafo = np.delete(grafo, i, axis=0)  #Remove a linha do ponto
                grafo = np.delete(grafo, i, axis=1)  #Remove a coluna do ponto
                coordenadas = np.delete(coordenadas, i, axis=0)  #Remove as coordenadas
            else:
                i += 1  #Continua verificando o próximo ponto

        return grafo, coordenadas  #Devolve a tabela e as coordenadas atualizadas
    else:
        #Mostra erro se o ponto não existir
        print(f"Erro: Vértice {no} está fora do intervalo.")
        return grafo, coordenadas  #Devolve a tabela sem mudanças

#Mostra a tabela de conexões no terminal
def mostra_matriz(grafo):
    print("A matriz de adjacência é:")
    print(grafo)  #Mostra a tabela que mostra as conexões entre os pontos

#Mostra o grafo desenhado em um gráfico
def visualizar_grafo(grafo, coordenadas):
    plt.figure(figsize=(8, 6))  #Define o tamanho do gráfico
    vertices = len(grafo)  #Conta quantos pontos o grafo tem

    #Desenha as conexões do grafo
    for i in range(vertices):
        for j in range(i + 1, vertices):
            if grafo[i][j] == 1:  #Se existe uma conexão entre os pontos i e j
                #Desenha a linha conectando os dois pontos
                plt.plot([coordenadas[i][0], coordenadas[j][0]], 
                         [coordenadas[i][1], coordenadas[j][1]], 'bo-')  #Linha azul com pontos

    #Desenha os pontos como círculos vermelhos
    for i in range(vertices):
        plt.scatter(coordenadas[i][0], coordenadas[i][1], s=100, color='red')  #Desenha o ponto
        plt.text(coordenadas[i][0], coordenadas[i][1], str(i+1), fontsize=12, ha='center')  #Mostra o número do ponto

    #Ajusta o gráfico para mostrar todos os pontos
    plt.xlim(-1, max(coordenadas[:, 0]) + 1)  #Limita o eixo X
    plt.ylim(-1, max(coordenadas[:, 1]) + 1)  #Limita o eixo Y
    plt.title("Grafo")  #Dá o título ao gráfico
    plt.grid()  #Mostra uma grade no fundo do gráfico
    plt.show()  #Exibe o gráfico

#Cria um grafo com 5 pontos
num_vertices = 5
grafo = cria_grafo(num_vertices)

#Define as coordenadas dos pontos
coordenadas = np.array([
    (1, 3),   #Coordenadas do ponto 1
    (1, 2),   #Coordenadas do ponto 2
    (2, 0),   #Coordenadas do ponto 3
    (3, 3),   #Coordenadas do ponto 4
    (4, 0)    #Coordenadas do ponto 5
])

#Adiciona conexões entre os pontos
adiciona_aresta(grafo, 1, 2)  #Conecta o ponto 1 ao ponto 2
adiciona_aresta(grafo, 1, 3)  #Conecta o ponto 1 ao ponto 3
adiciona_aresta(grafo, 2, 4)  #Conecta o ponto 2 ao ponto 4
adiciona_aresta(grafo, 3, 5)  #Conecta o ponto 3 ao ponto 5

#Mostra a tabela de conexões e o grafo desenhado
mostra_matriz(grafo)  #Mostra a tabela de conexões
visualizar_grafo(grafo, coordenadas)  #Desenha o grafo

#Remove a conexão entre os pontos 1 e 3
remove_aresta(grafo, 1, 3)  #Remove a conexão entre o ponto 1 e o ponto 3
mostra_matriz(grafo)  #Mostra a tabela de conexões atualizada
visualizar_grafo(grafo, coordenadas)  #Desenha o grafo atualizado

#Adiciona uma conexão entre os pontos 3 e 4
adiciona_aresta(grafo, 3, 4)  #Conecta o ponto 3 ao ponto 4
visualizar_grafo(grafo, coordenadas)  #Desenha o grafo com a nova conexão

#Remove o ponto 3 e suas conexões
grafo, coordenadas = remove_no(grafo, coordenadas, 3)  #Remove o ponto 3
mostra_matriz(grafo)  #Mostra a tabela de conexões após a remoção
visualizar_grafo(grafo, coordenadas)  #Desenha o grafo atualizado sem o ponto 3
