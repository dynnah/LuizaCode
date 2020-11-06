#saudacao = 'Olá'
#nome = 'Maria'
#print(saudacao + ', ' + nome)


#exercicio 01
"""print("Olá, qual o seu nome?")
user_nome = input()
print(user_nome + ", em que ano você nasceu?")
user_ano = input()
user_idade = 2020 - int(user_ano)
user_idade_nov_dez = user_idade -1
print(f"{user_nome}, se você já fez aniversário você tem {user_idade} anos. Mas se ainda não, tem {user_idade_nov_dez} anos.")

#exercicio 02
robo_idade = 107
print("Olá, eu sou a Lu da Magalu. Qual seu nome?")
user_nome = input()
print("Olá, " + user_nome + " É um prazer conhecer você! Qual a sua idade?")
user_ano = input()
diferenca_idade = int(robo_idade) - int(user_ano)
print(f"{user_nome}, sou {diferenca_idade} anos mais velha que você.")

#exercicio 03
print("Olá, qual o seu nome?")
user_nome = input()
print("Diga as notas de cada um dos trimestres. Separe-as por um espaço")
um,dois,tres = input().split(" ") # pega 3 valores na mesma linha e atribui a variáveis
um = float(um)
dois = float(dois)
tres = float(tres)
media = float(um + dois + tres) / 3
print(f"{media:.2f}")

if numero == 4:
        print('Sou 2 + 2')
elif numero <= 3:
        print('Sou pequeno')
else:
        if numero == 5:
            numero = numero + 5
            print('5 não, sou ' + str(numero))
        else:
            print(numero)

print("Olá, qual o seu nome?")
user_nome = input()
print(user_nome + ", em que ano você nasceu?")
user_ano = input()
print(user_nome + ", digite o número do mês que você nasceu:")
user_mes = input()
user_idade = 2020 - int(user_ano)
if int(user_mes) <= 10:
    print(f"Você tem {user_idade} anos.")
else:
    print(f"Você tem {user_idade - 1} anos.")

#Desafio
for number in range(0,100):
    number = number + 1
    if int((number%3) == 0):
        print(f"{number} é múltiplo de 3")
    elif int((number%5) == 0):
     print(f"{number} é Múltiplo de 5")
    else:
        if int(((number%3) == 0) and ((number%5) == 0)):
            print(f"{number} é Múltiplo de 3 e de 5")"""
