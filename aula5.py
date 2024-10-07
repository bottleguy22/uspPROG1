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
escolha_usuario = int(input("O que você escolhe? aperte 0 para pedra, 1 para papel e 2 para tesoura1\n"))

aleatorio = random.randint(0,2)
print(f"a escolha foi {aleatorio}")

if escolha_usuario == 0 and aleatorio == 2:
   print("Você venceu!")
elif aleatorio > escolha_usuario:
    print("O computador venceu!")
elif aleatorio == escolha_usuario:
    print("Deu empate!")    
else: 
    print("Você entrou um numero errado. Perdeu mané")