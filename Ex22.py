num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print("O maior numero é o numero {:.0f}".format(num1))
elif num2 > num1 and num2 > num3:
    print("O maior numero é o numero {:.0f}".format(num2))
else:
    print("O maior numero é o numero {:.0f}".format(num3))


if num1 < num2 and num1 < num3:
    print("O menor numero é o numero {:.0f}".format(num1))
elif num2 < num1 and num2 < num3:
    print("O menor numero é o numero {:.0f}".format(num2))
else:
    print("O menor numero é o numero {:.0f}".format(num3))


