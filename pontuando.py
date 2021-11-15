from random import *

tentativas = 0
score = 0

print('''
Porta da Fortuna!
=========

 Existe um super prêmio atrás de uma destas 3 portas!
 Adivinhe qual é  a porta certa para ganhar o prêmio!

  ______   _____   _____
 |      | |     | |     |
 | [1]  | | [2] | | [3] |
 |   º  | |   º | |   º |
 |      | |     | |     |
 |______| |_____| |_____|
 ''')

while score < 3:
    tentativas = tentativas + 1
    print("\nTentativas", tentativas, ''': Escolha uma porta
(1, 2, 3):''')
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1, 3)

    print('A porta escolhida foi a', portaEscolhida)
    print("A porta certa é a", portaCerta)
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score = score + 1
    else:
        print("Que peninha!")

    print("Sua pontuação atual é", score)
print("\n**Você consegui! Terminou o jogo em",
tentativas, "tentativas ***")
    
    
    
          
