from random import *

jogando = True
score = 0
cont = 0
pontuacao = 0
resposta = True
anterior = 0
print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

while jogando == True:
    score = randint(1, 10)
    print("Seu próximo número é", score)
    cont+=1
    print("\nGostaria de somar mais um número(s/n)")
    resposta = str(input()[0].lower())
    
    if resposta == 'n':break
    anterior = score
    pontuacao+=anterior
    print("sua pontuação é", pontuacao)
if score == 21:
    print("Parabéns!")
if score != 21:
    print("Tente outra vez.")
