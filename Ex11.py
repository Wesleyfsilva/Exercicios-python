num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print("O produto do dobro do 1º numero com metade do 2º numero é de {:.0f}".format(a))
print("O triplo do 1º numero somado com o 3º numero é de {:.0f}".format(b))
print("O 3º numero elevado ao cubo resulta em {:.2f}".format(c))