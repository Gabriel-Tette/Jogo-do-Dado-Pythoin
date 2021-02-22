from random import choice
lista=['Acho que sim', 'Acho que não', 'Talvez', ' Com Certeza', 'Lógico que não']
for perg in range (1,10):
    ask=input("Faça uma pergunta: ")
    resposta=choice(lista)
    print('Resposta: ',resposta)

