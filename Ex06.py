#Criar um programa que verifica se uma pessoa tem desconto em um produto, baseado na idade e sua categoria (estudante, aposentado, etc.) 
#e no dia da semana. (Use quantas categorias desejar)

a = float(input("Digite a sua idade: "))
b = input("Digite a sua categoria (estudante, adulto e aposentado)")
c = input("Digite o dia da semana: ")

desconto = 0

if a >= 10 and b == "estudante":
  desconto = 0.50

elif a >= 60: 
  desconto = 0.30

elif b == "estudante":
  desconto = 0.15

elif c == "quarta" or c== "terça":
  desconto = 0.15

elif b == "adulto" and c == "sexta":
  desconto: 0.20

if desconto > 0:
    print("Você tem direito a um desconto de {:.0%}.".format(desconto))
else:
  print("Você não tem direito a descontos")