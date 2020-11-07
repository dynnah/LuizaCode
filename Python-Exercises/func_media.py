def media (nota1, nota2, nota3):
  calc_media = ((float(nota1) + float(nota2) + float(nota3))/3)
  print(f"Sua média foi: {calc_media:.2f}")

print(f"Qual sua nota do 1o trimestre?")
nota1 = input()

print(f"Qual sua nota do 2o trimestre?")
nota2 = input()

print(f"Qual sua nota do 3o trimestre?")
nota3 = input()

media(nota1, nota2, nota3)