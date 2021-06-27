nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

cal = nota1 + nota2
media = cal / 2

if media >= 7 and media < 10:
    print("Voce foi aprovado parabens :D")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Voce foi reprovado")