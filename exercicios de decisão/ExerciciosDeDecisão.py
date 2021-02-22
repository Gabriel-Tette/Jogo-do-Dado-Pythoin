# num1=int(input("Digite um número: "))
# num2=int(input("Digite outro númeor: "))
# if num1>num2:
#     print("O maior número é{}" .format(num1))
# else:
#     print("O maior número é {} " .format(num2))

#-----------------------------------------------------

# valor=int(input("Digite um valor: "))
# if valor<0:
#     print("O valor é negativo ")
# else:
#     print("O valor é positivo")



#==========================================================


# sexo=input("Digite a letra F ou H: ")
# if sexo=='F' or sexo=='f':
#     print("Mulher")
# elif sexo=='H' or sexo=='h':
#     print('Homem')
# else:
#     print("Opção inexitente")



#============================-=====================================


# letra=input("Digite uma letre: ")
# if letra== 'a' or letra=='e' or letra=='i' or letra== 'o' or letra=='u':
#     print("Você digitou uma vogal")
#
# else:
#     print("Consoante")


# n1=int(input("Digite um número: "))
# n2=int(input("Digite um número: "))
# n3=int(input("digite um número: "))
#
# if n1> n2 and n1>n3:
#     print("O maior número é {}" .format(n1))
# elif n2>n1 and n2 >n3:
#     print("O maior valor é {}" .format(n2))
# elif n1==n2 and n2==n3 and n1==n3:
#     print("Os números  são iguais")
# else:
#    print("O maior valor é {}". format(n3))




# import random
# import calendar
#
# n1=input("Nome 1 : ")
# n2=input(("Nome 2: "))
# n3=input('Nome 3 : ')
# n4=input("Nome 4: ")
#
# lista=[n1,n2,n3,n4]
# lista.append("Luan")
# sort=random.choice(lista)
# cal=calendar.calendar
#
# print(cal)
#
# print(sort)


# frase=input("Digite qualquer coisa aqui: ")
# print(frase.upper())
# print(frase.lower())
# print('Gabriel' in frase)
# print(len(frase))
# print(frase[3+1])
# separar=frase.split()
# print('O primeiro nome tem {} letras' .format(len(separar[0])))

# import random
# import time
# nome=str(input('Qual o seu nome: '))
# print('Bom dia {}' .format(nome))
# prod=str(input("O que deseja comprar hoje: TENIS - CHINELO "))
# if prod=='TENIS' or prod=='tenis':
#     print('Legal! ')
#     marca=input('Qual marca você quer comprar: Nike ou Adidas: ')
#     if marca=='Nike' or marca=='nike':
#         print('Muito bem. Rode nossa roleta da sorte para ver quanto de desconto vai conseguir: ')
#         ok=input("Digite OK para girar a roda: ")
#         while ok!='ok':
#             ok=input("Digite corretamente: ")
#         desc=[10,20.30,40,50]
#         descfinal=random.choice(desc)
#         time.sleep(2)
#         print("Seu desconto é de {} " .format(descfinal))
#         desc1=(300/100)*descfinal
#         final=300-desc1
#         print('Seu desconto é de {:.2f}' .format(final))
#
#
#
#
#     else:
#         print("Adidas tem desconto especial")
# else:
#     print("Certo, você quer comprar Chinelo")


# from time import sleep
# for x in range (10,0):
#     sleep(1)
#     print(x)
# sleep(3)
# print('GAME OVER')


# for nota in range(1,4+1):
#     nota=int(input('Digite a nota: '))
# soma=nota*4
# print(soma)


# num=int(input("Digite a tabuada: "))
# resul=0
# for tab in range (1,10+1):
#     resul=resul+num
#     print(num,'x',tab ,'=',resul)

# num = 0
# n1=int(input("Digite um número: "))
# for n in range (1, 11 ):
#     num=num+n1
#     print(n1,"x",n,'=',num)

#lista=['Gabriel','Thiana','Leo','Carol']
# from time import sleep
# for x in range (1,6):
#     sleep(2)
#     ask=str(input('Responda a pergunta. Você tem 10 segundos para responder quanto é 10+20: '))
#     if ask!=30:
#         break


frase="O Gabriel Mora em Jacareí"
print(frase.upper())
print(frase.count(frase))
separar=frase.split()
print(format(len(separar[1])))

















