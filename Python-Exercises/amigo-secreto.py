import random

amigos = []
verifica_amigo = []

print("Digite quantas pessoas irão participar do amigo secreto:")
qtde_amigos = int(input())

for count in range(qtde_amigos):
    print(f"Digite o nome da(o) amiga(o):")
    amigo = input()
    amigos.append(amigo)

#verifica_amigo = amigos[:] auxiliar para verificar se pessoa já foi sorteada

i = 0
while len(verifica_amigo) < len (amigos):
    sorteio = random.choice(amigos) #sorteia nome dx participante
    if (amigos[i] != sorteio) and (sorteio not in verifica_amigo):
        print(f"{amigos[i]} saiu com {sorteio}")
        verifica_amigo.append(sorteio)
        i += 1
    else:
        continue

"""i = 0
while i < len(qtde_amigos):
    sorteio 

print(sorteio)
print (verifica_amigo)"""

  

