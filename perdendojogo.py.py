from random import *

jogando = True
score = 0
print('''
Porta da Fortuna!
========

 Existe um super prêmio atrás de uma destas 3 portas!
 Adivinhe qual é  a porta certa para ganhar o prêmio!

  ______   _____   _____
 |      | |     | |     |
 | [1]  | | [2] | | [3] |
 |   º  | |   º | |   º |
 |      | |     | |     |
 |______| |_____| |_____|
 ''')

while jogando == True:
    print("\nEscolha uma porta(1, 2 ou 3):")

    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
    portaCerta = randint(1, 3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        score = score + 1
    else:
        score = score = 0
        print("Que peninha!")

    print("Sua pontuação é", score)
    print("\nVocê que jogar de novo?(s/n)")
    resposta = str(input()[0].lower())

    if resposta == 'n':
        jogando = False

print("Obrigada por jogar.")
print("sua pontuação final é de", score)

      
