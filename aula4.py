estados = ["RJ", "MG", "SP", "MT", "PI","RS"]
print(len(estados))

adicionar = len(estados)

#fazendo aparecer o erro out of range
#print(estados[7])

#posso solucionar assim
#indexação por zero
print(estados[adicionar-4])

#pesticidas = ["maçã", "banana", "laranja", "uva", "abacaxi", "melancia", "morango", "pera", "kiwi", "mamão", "cereja", "manga"]
#print(len(frutas-3))

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi", "melancia", "morango", "pera", "kiwi", "mamão", "cereja", "manga"]
verduras = ["alface", "couve", "espinafre", "agrião", "rúcula", "brócolis", "acelga", "repolho", "salsinha", "coentro", "hortelã", "manjericão"]

pesticidas = [frutas, verduras]
print(pesticidas)

#tem dois colchetes no final pois são duas listas dentro de uma terceira lista

#printar apples
#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#print(fruits[-5])
#o último elemento da lista é -1, o penultimo -2, etc..


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
#aqui acessa a segunda lista e seu segundo elemento 
print(dirty_dozen[1][1])

#alguns exemplos de aplicações
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
