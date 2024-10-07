#sorteando qual amigo vai pagar
import random

# 1 option
amigos = ["Bruno", "Juan" , "Diego", "Thales"]
print(random.choice(amigos))

# 2 option
a = random.randint(0,3)
print(amigos[a])

