#2 - Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine 
#se o aluno passou ou não. Um aluno passa se a soma das notas for maior ou igual a 60 e nenhuma nota é menor que 40.

a = float(input("Digite a primeira nota (0 a 100): "))
b = float(input("Digite a segunda nota (0 a 100): "))
 


if a+ b>= 60 and a >= 40 and b>= 40 :
  print("O Aluno passou!")

else:
  print("O aluno não passou ")