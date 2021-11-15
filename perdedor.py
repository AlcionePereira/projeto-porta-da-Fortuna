from random import *

jogando = True
score = 0
resposta = True
cont = 0
pontuacao = 0

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

while jogando == True:
    score = randint(1, 10)
    print("Seu próximo número é", score)
    if cont == 1:
        print("sua pontuação é", score)
        cont+=1
    else:
        anterior = score
        pontuacao+=anterior
        print("sua pontuação é", pontuacao)
    print('\nGostaria de somar mais um número (s/n)')
    resposta = input()
    if resposta == 'n':break
    

if pontuacao == 21:
    print("parabéns")

if pontuacao!= 21:
    print("Tente outra vez.")

    
