#listas em python sempre começa com colchetes

lista_estados = ["SP" , "RJ" , "SP", "MATO GROSSO", "PERNAMBUCO"]
print(lista_estados[0])
print(lista_estados)
print(lista_estados[-1]) #nesse caso comecei a contar de pernambuco

(lista_estados[1]) = "Rio de Janeiro"
print(lista_estados)

#adicionar apenas um elemento na lista
lista_estados.append("CEARÁ CUMPADI")
print(lista_estados)

#adicionar varios elementos na lista
#aqui usou colchete novamente pois estou adicionando outra lista adicional na lista inicial
lista_estados.extend(["ROBERTO", "FISICA 1", "NOTA ALTA"])
print(len(lista_estados))
print(lista_estados)
#fruits = [item1, item2]
#frutas = ["maçã", "banana", "rolê"]
#print (frutas)