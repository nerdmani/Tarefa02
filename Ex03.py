#3 -Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.

a = float(input("Digite a sua idade: "))
b= input("Você possui autorização dos pais ? (sim/não): ")

if a >= 18 or b == "sim":
  print("Você poderá entrar")

else: 
  ("Você não poderá entrar")