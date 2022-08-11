
## O objetivo deste programa é que o computador gere um número aleatório entre 0 e 100 e o usuário tente acertar qual é.

from random import Random, randint 

computador = Random.randint(1, 100)

print(computador)

usuario = int(input("Defina um número entre 1 e 100: "))

i = 0

while i < 101:
    if usuario != computador:
        i = i + 1
    else:
        print("Parabéns, você acertou!")





    


