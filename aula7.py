notas_estudantes = [85, 92, 78, 64, 89, 73, 91, 88, 77, 95, 
                    82, 76, 90, 68, 84, 87, 81, 74, 93, 79, 
                    65, 72, 80, 96, 86]

#usando a função SUM (soma)
#alor_nota_total = sum(notas_estudantes)
#print(valor_nota_total)

#posso somar atraves de um loop
sum = 0 
for notas in notas_estudantes:
    sum += notas
    #soma + notas = 0+notas, pois definimos que a soma começa em zero
print(sum)

#POSSO ALTERAR A SOMA PARA ALGUM VALOR NO LOOP E ALTERAR O VALOR FINAL
#para cada soma definida aqui, começamos com cem MIL e depois somamos os valores totais

sum = 100000
for notas in notas_estudantes:
    sum += notas 
print(sum)    

#usando o max para achar o valor maximo dentro da lista
print(max(notas_estudantes))

#posso tentar fazer isso com if e else usando um loop
#aqui eu defini que a hora que a nota for igual 96, eu defini o máximo
max = 96

for notas in notas_estudantes:
   if notas == 96:
    print(notas) 


#posso fazer isso de outra forma
max = 0
for notas in notas_estudantes:
    if notas > max:
       max = notas
print(max)       

#aqui o loop verifica cada elemento da lista de notas
#e compara inicialmente com zero
#definimos todos elementos com o nome notas
#toda vez que notas > max ele passa adiante
#se alguma hora o max for igual a um valor de notas
#ele vai printar o max

#também posso omitir o novo nome do loop
#guardar apenas como uma variável

sum = 0 
for _ in notas_estudantes:
   sum += _
    #soma + notas = 0+notas, pois definimos que a soma começa em zero
print(sum)

