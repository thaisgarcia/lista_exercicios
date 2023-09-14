nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1*1 + nota2*2 + nota3*3) / (1 + 2 + 3)

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")