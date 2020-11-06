print("Olá, qual o seu nome?")
user_name = input()
print(f"Olá {user_name}! Em que ano você está na escola?")
user_ano = input()

somatorio = []
for count in range(0,3):
    print(f"Qual foi sua nota no {count+1}o trimestre?")
    nota = float(input())
    somatorio.append(nota)
media = sum(somatorio)/3

if media < 7:
    print(f"Sua média no {user_ano}o ano foi: {media:.2f}. Você foi reprovada(o)")
else:
    print(f"Sua média no {user_ano}o ano foi: {media:.2f}. Você foi aprovada(o)")