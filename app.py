def calculo_notaAluno(nota1, nota2):
    return ((nota1 + nota2) / 2)

print("=== Sistema Nota de Aluno (Média) ===")

n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digite a Segunda Nota: "))

media = calculo_notaAluno(n1, n2)

print("A média final é: ", media)

#Estrutura condicional para ver se reprovou ou passou 
if media <= 5 :
    
    print("Reprovado!")

else:
    print("Aprovado!")