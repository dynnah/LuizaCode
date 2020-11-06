letras = ['R', 'B', 'R', 'R','B','G','G','B','G','R', ]
lista_R = []
lista_B = []
lista_G = []

for letra in letras:
  if letra == 'R':
    lista_R.append(letra)
  elif letra == 'B':
    lista_B.append(letra)
  elif letra == 'G':
    lista_G.append(letra)
    
RBG_lista = lista_R + lista_B + lista_G
print(RBG_lista)
print(' - '.join(RBG_lista))