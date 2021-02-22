import random
print('O jogo é simples. Você escolherá um número de 1-10 e se acertar ganhará R$100,00')
num=int(input('Escolha um número: '))
lista=[1,2,3,4,5,6,7,8,9,10]
esc=random.choice(lista)
while num!=esc:
    if num>10 or num==0:
        num=int(input('Número Inválido. Digite um número entre 1-10 '))
    elif num<esc:
        num=int(input('Tente um número maior '))
    else:
        num=int(input("Tente um númeor menor: "))

else:
    print('O número sorteado foi {}'.format(esc))
    print('Parabéns. Você acabou de ganhar R$100,00')


