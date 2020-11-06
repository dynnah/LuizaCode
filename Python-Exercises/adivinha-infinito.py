import random

jogar_novamente = 'sim'
while jogar_novamente == 'sim' or jogar_novamente.startswith('s'):
    print("Olá, você está pronta(o) para jogar? As regras são as seguintes: \n 1- O número sorteado está entre 0 e 80 \n 2- Você tem infinitas chances para tentar acertar o número \n 3- A cada erro, eu te darei uma dica de aproximação. \nBoa sorte! ")
    print()
    print ("Já sorteei o número.")
    num_sorteado = random.randint(1,80)
    palpite =  ''
    count_tentativa = 0

    while palpite != num_sorteado:
        print("Qual número eu estou pensando?")
        palpite = int(input())
        count_tentativa += 1
        if palpite <= (num_sorteado-10):
            print("Tente um número bem maior")
        elif (num_sorteado-10) < palpite < num_sorteado:
            print ("Você está próxima(o) de acertar. Tente um número um pouco maior")
        elif palpite >= (num_sorteado+10):
            print("Tente um número bem menor")
        else:
            continue

    if count_tentativa < 6:
        print(f"Parabéns, o número sorteado era {num_sorteado}. Você acertou em {count_tentativa} tentativa(s)")
    else:
        print(f"Finalmente, ein? O número sorteado era {num_sorteado}. Você acertou em {count_tentativa} tentativa(s)")
        
        print()
        print("Deseja jogar novamente?")
        jogar_novamente = input().lower()