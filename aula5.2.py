import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scisors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

usuario_escolha = int(input("Escolha entre, 0, 1, 2, sendo pedra, papel e tesoura\n"))

computador_escolha = random.randint(0,2)
print(f"A escolha do computador foi {computador_escolha}")

if computador_escolha == usuario_escolha:
   print("Você e o computador escolheram a mesma opção.")

elif computador_escolha > usuario_escolha:
   print("Você perdeu")

if usuario_escolha > computador_escolha:
   print("Você venceu.")      

if input == computador_escolha:
   print("Perdeu!")
else:
   print("Você escolheu um número fora do intervalo!")   