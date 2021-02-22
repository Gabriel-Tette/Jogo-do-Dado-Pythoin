# # #a= int(input('Entre com o primeiro valor '))
# # #b= int(input('Entre com o segundo valor'))
# #
# # #soma = a+b
# # #sub= a-b
# # #mult= a*b
# # #div = a/b
# #
# # #print('soma {}'
# #       '\nsub {} '
# #       '\nmult {} '
# #       '\ndiv {}'  .format(soma, sub , mult , div))
# #
# # print('soma {}' .format(soma))
# # print('sub  {}' .format(sub))
# # print('mult {}' .format(mult))
# # print('div: {}' .format(div))
#
#
# # nome= input('Digite seu nome ')
# # print('Bom dia',nome)
# # produto=int(input('O que você quer comprar:'
# #                   '\n[1] Tenis'
# #                   '\n[2] Chinelo '))
# # if produto ==1 :
# #     print('Você escolheu tenis')
# #
# # else :
# #     print('Você escolhe chinelo')
#
#
# # n1= float(input('Digite a nota: '))
# # n2= float(input('Digite a nota: '))
# # n3= float(input('Digite a nota: '))
# # n4= float(input('Digite a nota: '))
# # media= (n1+n2+n3+n4)/4
# # if n1 or n2 or n3 or n4>10:
# #     print('Uma nota foi digitada incorretamente')
# # else:
# #     print(media)
#
# # ===================================== ESTRUTURA DE REPETIÇÃO FOR ===========================================
# # qualquer coisa que estiver dentro do range será repetida o número de vezes do numero que está no parenteses do range
# # a=int(input("Digite um número: " ))
# # div=0
# # for x in range (1, a+1):
# #     resto=a%x
# #     print(x, resto)
# #     if resto==0:
# #         div=div+1
# #
# # if div==2:
# #     print('Número {} primo '.format(a))
# # else:
# #     print('Número não é primo')
# # #------------------------------------------------------------
# # s=0
# # for x in range (1, 10+1):
# #    # print(x)
# #     a=int(input('Digite um número: '))
# #     s=s+a
# # print(s)
#
# # =-=-=-=-=--=-==-=-=-=-=-=-==-===---===-=-=-=-=-=-=-=-=-
# # i=int(input('Digite o primeiro número: '))
# # f= int(input('Digite o último número: '))
# # p=int(input('Digite em quantas vezes vai ser a passada'))
# # for x in range (i, f+1, p):
# #     print(x)
# # ---------------------------------------------------
# # a=int(input('Digite um numero '))
# # div=0
# #
# # for x in range (1, a+1):
# #     resto=a%x
# #     print(x,resto)
# #     if resto==0:
# #         div=div+1
# #
# #
# # if div==2:
# #     print('O número {} é primo '.format(a))
# # else:
# #     print('o número {} não é primo ' .format(a))
#
#
# # ---------------------------------------------------
#
#
# # for num in range (1,15+1):
# #     div=0
# #     for x in range (1, num+1):
# #         resto=num%x
# #         #print(x,resto)
# #         if resto==0:
# #             div=div+1
# #     if div==2:
# #         print(num)
#
# # -------------------------------lista----------------------------------------
# # lista = [1, 3, 7, 19]
# # listaanimal = ['gato', 'cachorro', 'peixe']
# # listaanimal.sort() - .sort serve para ordenar a lista, .reverse serve para deixa-la ao contrário
# # print(listaanimal)
# # listaanimal.reverse()
# # print(listaanimal)
#
# # print(listaanimal[1])
# # print(min(lista))
# # if 'gato' in listaanimal:
# #     print('Sim')
# # else:
# #     print('Não')
# # listaanimal.append('cavalo') - .append serve para adc algo na lista - .pop serve para remover o ultimo
# # print(listaanimal)
#
# #- posso usar o if  para procurar algo especifico na lista como no exemplo ao lado
#
#
# # tupla=(1,2,3,4,5)
# # print(tupla)
# # tupla1=('agua', 'refri', 'cerveja' 'suco')
# # print(tupla1)
# # print(max(tupla))
# from typing import List
#
# # a=int(input('Primeiro bimestre: '))
# # while a >10:
# #     a=int(input('Nota incorreta. Digite novamente: '))
# # b= int(input('Segundo bimestre: '))
# # while b >10:
# #     a=int(input('Nota incorreta. Digite novamente: '))
#
# # lista1=['cavalo' , 'macaco' , 'cachorro ']
# # print(lista1)
# # lista1.sort()
# # print(lista1)
# # lista1.append('peixe')
# # lista1[0]='tigre'
# # print(lista1)
#
#
# # conj={1,2,3,4}
# # print(conj)
# # conj.discard(7)
# # print(conj)
#
# # conj={1,2,3,4,5}
# # conj2=(5,6,7,8,9,)
# # conj_uniao=conj.union(conj2)
# # print(conj_uniao)
# # conjinter=conj.intersection(conj2)
# # print(conjinter)
# # conjdif= conj.difference(conj2)
# # print(conjdif)
# # conjs=conj.symmetric_difference(conj2)
# # print(conjs)
# #
# # conj_a={1,2,3}
# # conj_b={1,2,3,4,5}
# # conj_c= conj_a.issubset(conj_b)
# # print(conj_c)
#
# # listaanimais=['gato' ,'gato', 'cachorro' ,'cachorro', ' cavalo' ]
# # print(listaanimais)
# # conjaniamal= set(listaanimais)
# # print(conjaniamal)
# # lista1=list(conjaniamal)
# # print(lista1)
#
#
# # seu eu não quiser usar o 'init'
#
#
#
# # class Calculadora:
# #     def __init__(self, n1, n2):
# #         self.a=n1
# #         self.b=n2
# #
# #     def soma ( self):
# #         return self.a + self.b
# #     def sub ( a, b):
# #         return a-b
# # calculadora=Calculadora(10,2)
# # print(calculadora.a)
# # print(calculadora.soma())
#
#
#
# # class Calculadora:
# #     def __init__(self, n1, n2):
# #         self.a=n1
# #         self.b=n2
# #     def soma (self):
# #         return self.a + self.b
# # calculadora=Calculadora(10,2)
# # print(calculadora.a)
# # print(calculadora.soma())
#
#
#
#
#
#
#
#
#
#
#
# # sal=float(input("Qual o seu salário: "))
# # temp=int(input("Há quanto tempo voce trabalha aqui: "))
# # if temp >= 10:
# #     reajuste=(sal/100)*25
# #     print('O aumento é de {}' .format(reajuste))
# # else:
# #     print("Não houve reajuste")
#
#
# # nome=(input("Bem Vindo. Qual o seu nome: "))
# # print("Ola ", nome)
# # print("O que o você deseja comprar hoje: ")
# # print("[1] TENIS")
# # prod=input("[2] Chinelo")
# #
# # if prod==1:
# #     print("Voce escolheu Tenis")
# #     print("Muito bem, esse tenis é muito legal")
# #     print("Se o pagamento for a vista, o senhor tem um desconto de 37%: ")
# #     pag=(input('Deseja fazer o pagamento a vista: '
# #                 '\n[1] SIM'
# #                 '\n[2] NÂO '))
# #
# # else:
# #     print("Obrigado")
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#










# tab=int(input('iDigite um número para ver a tabuada: '))
# r=0
# for x in range (1,10+1):
#     r=r+tab
#     print(tab,'x',x,"=",r)


# import random
# for x in range(1,5):
#     nome=str(input["Digite um nome: "]55)
# print(random.shuffle(nome))


# def soma(a,b):
#     s=a+b
#     print(s)
#
# soma(3,4)
# soma(329847298,32948709284092)

# def showLine ():
#     print('-'* 30)
#
# showLine()
# print('Ola mundo')
# showLine()


# def lin (msg):
#   tam=len(msg)+4
#   print('-'*tam)
#   print(f'  {msg}')
#   print('-'*tam)
#
#
# lin('Gabriel')








# def linha (texto):
#     tam=len(texto)
#     print('-'*tam)
#     print(f'{texto}')
#     print('-'*tam)
#
#
# linha('Gabriel')




# def maior (*num):
#     cont=maior=0
#     print('Analisando os valores...')
#     for valor in num:
#         print(f' {valor} ' , end='')
#         if cont==0:
#             maior=valor
#         else:
#             if valor>maior:
#                 maior=valor
#         cont =+1
#     print(f'\nForam informados {cont} valores')
#     print(f'O maior valor é: {maior} ')
#
#
# maior(3, 6, 5, 8, 2, 9)
# maior(4,2,3,5)
# maior(20,70,33,10)
# maior(1,2)


# from random import randint
#
# def sorteia(lista):
#     print('Sorteando 5 valores da lista ')
#     for cont in range(0,5):
#         n=randint (1,20)
#         lista.append(randint(1,20))
#         print(n)
#
#
# num=list()
# sorteia(num)
# print(num)


# def showLine(msg):
#     aut=len(msg)
#     print('-'*aut)
#     print(msg)
#     print('-'*aut)
#
#
# showLine('Gabriel Tette Silva')



# from random import choice
# def sorteia(msg):
#     aut=len(msg)
#     print('-'*aut)
#     print(msg)
#     print('-'*aut)
#     for cont in range(1,10):
#         print(cont)
#         s=choice()
#         print(s)
#         #print('O valor sorteado é {}'. format(s))
#
#
# sorteia('Verificando...')
#



# from random import randint
#
# def sorteia(lista):
#      print('Sorteando 5 valores da lista ')
#      for cont in range(0,10):
#          n=randint (1,20+1)
#          lista.append(randint(1,20))
#          print(n)
#
#
# num=list()
# sorteia(num)
# print(num)


import random

frase='Gabriel Tette Silvs Mora em Jacareí'
print(frase)
print('Há {} letras nessa frase' .format(len(frase)))
print(frase.isupper())





































































