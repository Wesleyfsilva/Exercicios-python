num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero:"))

if num1 > num2 and num1 > num3:
    print("O numero",num1 ,"é o maior numero")
elif num2 > num3 and num2 > num1:
    print("O numero", num2,"é o maior numero")
else:
    print("O numero ",num3,"é o maior numero")