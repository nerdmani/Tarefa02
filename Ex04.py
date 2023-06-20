#4 - Escreva um código que verifique se um número é par ou divisível por 3.

a = float(input("Digite um número: "))

if a % 2 == 0 :
  print("Esse número é par")
elif a % 3 == 0 :
  print("O número é divisível por 3")

else:
  print("O número não é par e nem divisível por 3")