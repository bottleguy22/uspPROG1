#usando range no loop
#usando o LOOP FORA DA LISTA
#importante dizer que o range tem que andar junto com o loop

for nota in range(0,100):
    print(nota)

#aqui eu printei de zero a 99
# sendo o 0, o proprio 0
# e o 100, sendo o 99

#também posso definir o intervalo entre cada pulo desse range
#estou indo de 0 a 99, pulando 5 em 5
for nota in range(0,100,5):     
    print(nota)

#também posso fazer uma soma de elementos
#aqui está errado, pois eu poderia usar soma apenas se estivesse uma lista pré-existente
#
sum = 1
for nota in range(0,100):
    sum += nota
    print(nota)    



#correção após com a lista
notas_estudantes = [85, 92, 78, 64, 89, 73, 91, 88, 77, 95, 
                    82, 76, 90, 68, 84, 87, 81, 74, 93, 79, 
                    65, 72, 80, 96, 86]
sum = 1

for nota in notas_estudantes:
    sum += nota
    print(nota)




#resolução da professora
total = 0
for number in range (0,100):
    total += number
print(total)    


#também posso fazer ambos
soma = sum(range(1,101))
print(soma)
#resultado 5050