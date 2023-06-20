#5 -Escreva um código que verifique se uma pessoa é alfabetizada (sabe ler e escrever) e tem mais de 25 anos de idade.

a = input("Você é alfabetizado ? (sim/não): ")
b = float(input("Digite a sua idade: "))

if a == "sim" and b > 25:
  print("A pessoa é alfabetizda e maior de 25 anos")

else:
  print("A pessoa a não atende os critérios")