'''Homework Aula 1 - Um jogo

- Criar um programa que pegue nome do usuário e explique as regras do jogo para o usuário.
- Pense em um numero de 1 a 20
- Sortear um numero aleatório
- Usuário tente adivinha numero sorteado
- Usuário só pode ter 6 chances
- Pegar cada palpite e verificar se é: maior, igual ou menor que o número sorteado
- Falar mensagem que o número que o usuário deu palpite é maior, igual ou menor que o número sorteado.
- Colocar condição de parada "break" nas condições de verificação'''

import random

print("Olá, qual o seu nome?")
user_nome = input()
print(user_nome + ", você está pronta para jogar? As regras são as seguintes: \n 1- O número sorteado está entre 0 e 20 \n 2- Você tem 6 chances para tentar acertar o número \n 3- A cada erro, eu te darei uma dica de aproximação. \nBoa sorte! ")
count = 1
print ("Já sorteei o número.")
num_sorteado = random.randint(0,20)
#print (f"{num_sorteado}")
print ("Digite sua aposta:")
num_tentativa_user =  input()
while (count < 6):
    if (int(num_sorteado) < int(num_tentativa_user)):
        count += 1
        print("O número sorteado é menor. Tente novamente:")
        num_tentativa_user =  input()
    elif (int(num_sorteado) > int(num_tentativa_user)):
        count += 1
        print("O número sorteado é maior. Tente novamente:")
        num_tentativa_user =  input()
    elif (int(num_sorteado) == int(num_tentativa_user)):
        print(f"Você acertou! \nNúmero sorteado: {num_sorteado}") 
        break
else:
        if (int(count) == 6 and int(num_sorteado) != int(num_tentativa_user)):
            print(f"Sinto muito, suas tentativas acabaram! \nNúmero sorteado: {num_sorteado}")
        elif(int(count) == 6 and int(num_sorteado) == int(num_tentativa_user)):
            print(f"Você acertou! \nNúmero sorteado: {num_sorteado}")