import random

print("Olá, qual o seu nome?")
user_nome = input()
print(user_nome + ", você está pronta para jogar? As regras são as seguintes: \n 1- O número sorteado está entre 0 e 20 \n 2- Você tem 6 chances para tentar acertar o número \n 3- A cada erro, eu te darei uma dica de aproximação. \nBoa sorte! ")
count = 1
print ("Já sorteei o número.")
num_sorteado = random.randint(0,20)
print (f"{num_sorteado}")
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
        print(f"Você acertou em {count} tentativa(s) \nNúmero sorteado: {num_sorteado}") 
        break
else:
        if (int(count) == 6 and int(num_sorteado) != int(num_tentativa_user)):
            print(f"Sinto muito, suas tentativas acabaram! \nNúmero sorteado: {num_sorteado}")
        elif(int(count) == 6 and int(num_sorteado) == int(num_tentativa_user)):
            print(f"Você acertou! \nNúmero sorteado: {num_sorteado}")