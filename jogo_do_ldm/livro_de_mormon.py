from time import sleep
ponto=1
nome=input("Digite seu nome: ")
print('Seja bem vindo {} '.format(nome))
#sleep(3)
print('Iremos começar a jogar do Livro de Móemon')
lista=['[1]Alma', '[2]Néfi', '[3]Joseph']
for li in lista:
    print(li)
prof=int(input('Escolha um profeta: '))
while prof>3:
    prof=int(input('Número inválido. Digite novamente'))
if prof==1:
    print('Você escolheu Alma')
    alma=input('Quem foi o primeiro juís supremo:[1] Alma o Pai ou [2]Alma o Filho: ')
    while alma!='1':
        print('Resposta errada. Perdeu 1 ponto. Tente Novamente: ')
    else:
        ponto=ponto+1
        print('Resposta correta. Você ganhou 1 ponto')
        print(ponto)
        lista.append('[4] Moroni')
        for li in lista:
            print(li)
elif prof==2:
    print('Você escolheu Néfi')
else:
    print('Você escolheu Joseph')










