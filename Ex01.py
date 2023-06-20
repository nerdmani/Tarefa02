#1 -Escreva um programa que peça ao usuário inserir três números e, em seguida, determine se um dos três números é maior que a soma dos outros dois.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o  segundo número: "))
c = float(input("Digite o terceiro número: "))


if a> b+c or b> a+c or c> a+b :
  print("Um dos números selecionados é maior que a soma dos outros dois!!")

else:
  print("Nenhum número foi maior que a soma dos dois números :(")