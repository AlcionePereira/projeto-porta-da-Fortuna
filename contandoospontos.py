# Crie uma variável para saber quantas vezes o jogador adivinhou a porta correta-
# mente.Não esaqueça de mostrar a pontuação final do jogador ao fim do programa
#(fora do loop)

from random import *

cont = 0
print('''
Port da Fortuna!
=======
Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
  ______   _____   _____
 |      | |     | |     |
 | [1]  | | [2] | | [3] |
 |   º  | |   º | |   º |
 |      | |     | |     |
 |______| |_____| |_____|
 ''')

for c in range(3):
    print("\nEscolha um porta (1, 2,3):")
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)
   
    portaCerta = randint(1, 3)

    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)
    if portaEscolhida == portaCerta:
        print('Parabéns')
        cont +=1
    else:
        print("Que peninha!")
     
           
print(f'Você tem {cont} pontos.')
