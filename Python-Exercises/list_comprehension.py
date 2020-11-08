import random

RGB = ['R','G','B']
list_RGB = [random.choice(RGB) for elementos in range(15)]

print(list_RGB)

list_R = [letra for letra in list_RGB if letra == 'R']
list_G = [letra for letra in list_RGB if letra == 'G']
list_B = [letra for letra in list_RGB if letra == 'B']
lista_RGB = list_R + list_B + list_G
print(lista_RGB)