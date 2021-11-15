from random import *

# imprima as 3 portas e as instruçôes do jogo
print('''
 Porta da Fortuna!
 =========
 Existe um super prêmio atrás de uma destas 3 portas!
 Adivinhe qual é a porta certa para ganhar o prêmio!

  ______   _____   _____
 |      | |     | |     |
 | [1]  | | [2] | | [3] |
 |   º  | |   º | |   º |
 |      | |     | |     |
 |______| |_____| |_____|

 Escolha uma porta (1, 2, 3):
 ''')
# pegue a porta escolhida e a armazene como um número
#inteiro (int)

portaEscolhida = input()
portaEscolhida = int(portaEscolhida)

# escolha aleatoriamente a porta que esconde o prêmio
#(entre 1 e 3)

portaCerta = randint(1, 3)

#mostre ao jogador qual porta ele escolheu e qual era a
#porta certa
print("A porta escolhida foi a", portaEscolhida)
print(" A porta certa é a ", portaCerta)

#o jogador ganha se o número da porta escolhida e o
# da porta certa forem o mesmo

if portaEscolhida ==portaCerta:
    print("Parabéns!")
else:
    print("Que peninha!")
    


















    
    
