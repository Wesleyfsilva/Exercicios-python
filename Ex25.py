print("*****************************************")
print("Bem vindo ao calculo de reajuste salarial")
print("*****************************************")

sal = float(input("Digite o seu salario bruto atual: "))

vinte = (20/100) * sal
quinze = (15/100) * sal
dez = (10/100) * sal
cinco = (5/100) * sal

if sal <= 280.00:
    print("O seu novo salario com o reajuste de 20% é de R$ {:.2f} ".format(vinte + sal ))
    print("O seu salario era de R$", sal)
    print("Foi aplicado um aumento de 20% no seu salario bruto")
    print("O valor do aumento foi de R$", vinte)
elif sal >= 280.00 and sal <= 700.00:
    print("O seu novo salario com reajuste de 15% é de R$ {:.2f}".format(quinze + sal))
    print("O seu salario era de R$", sal)
    print("Foi aplicado um aumento de 15% no seu salario bruto")
    print("O valor do aumento foi de R$", quinze)
elif sal >= 700.00 and sal <= 1500.00:
    print("O seu salario com reajuste de 10% é de R$ {:.2f} ".format(dez + sal))
    print("O seu salario era de R$", sal)
    print("Foi aplicado um aumento de 10% no seu salario bruto")
    print("O valor do aumento foi de R$ {:.2f}".format(dez))
elif sal > 1500.00:
    print("O seu salario com reajuste de 5% é de R$ {:.2f} ".format(cinco + sal))
    print("O seu salario era de R$", sal)
    print("Foi aplicado um aumento de 5% no seu salario bruto")
    print("O valor do aumento foi de R$ {:.2f}".format(cinco))




