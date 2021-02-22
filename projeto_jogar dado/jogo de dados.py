from random import choice
from time import sleep
nome=input("Para começar digite o se nome: ")
print('Bem Vindo {}. Eu sou o Silvio Santos' .format(nome))
jogar=input('Você gostaria de jogar os dados: [S/N]')
if jogar =='S' or jogar=='s':
    print("Os dados estão rolando...")
    dd=[1,2,3,4,5,6]
    escolha=choice(dd)
    sleep(1)
    print('Você tirou o número {}. ' .format(escolha))
else:
    print('GAME OVER')
