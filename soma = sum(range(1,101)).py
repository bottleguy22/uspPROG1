soma = sum(range(1,101))
print(soma)

for valor in range(1,101):
  if valor % 3 == 0 and valor % 5 == 0:  # Divisível por 3 e 5
   print("FizzBuzz")
  if valor % 3 == 0:
   print("fizz")
  elif valor % 5 == 0:
    print("buzz")
  else: 
    print(valor)

#exercicio fizz buzz
#    