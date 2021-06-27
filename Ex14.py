print("*************************")
print("*********PEIXES**********")
print("*************************")

peso = float(input("Digite a quantidade em kg de peixes: "))


if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Voce excedeu o peso de peixes e sofrerá uma multa de R$ {:.2f}".format(multa))
else:
    print("Voce esta dentro do permitido")
