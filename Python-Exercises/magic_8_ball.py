import random
import time

respostas = [
    "Certamente",
    "Sem dúvida alguma",
    "Você pode acreditar nisso",
    "Sim, definitivamente",
    "Pode ser que sim",
    "Sim",
    "Melhor não te dizer agora",
    "Pergunte novamente mais tarde",
    "Não tenho certeza agora",
    "Se concetre e pergunte novamente",
    "Não conte com isso",
    "Não me parece uma boa ideia",
    "Acredito que não",
    "Não, sinto muito"
]
print("----- Bola Mágica -----")
print()

print("Para qual pergunta você gostaria de saber uma resposta?")
user_answer = input()
print("Estou pensando...")
time.sleep(random.randrange(0,5))
answer = random.choice(respostas)
print(f"A resposta que você procura é: {answer}")
print()

print("Você gostaria de fazer outra pergunta? [S/N]")
ask_again = input()
print()

while ask_again == 'S' or ask_again == 's' or ask_again == 'Sim' or ask_again == 'sim' or ask_again == 'SIM':
    print("Para qual pergunta você gostaria de saber uma resposta?")
    user_answer = input()
    print("Estou pensando...")
    time.sleep(random.randrange(0,5))
    answer = random.choice(respostas)
    print(f"A resposta que você procura é: {answer}")
    print()
    print("Você gostaria de fazer outra pergunta? [S/N]")
    ask_again = input()
if ask_again == 'N' or ask_again == 'n' or ask_again == 'Não' or ask_again == 'não' or ask_again == 'nao' or ask_again == 'NÃO':
    print("Volte sempre para mais respostas")