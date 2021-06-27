tothora = int(input("Digite o total de horas trabalhadas: "))
valhora = float(input("Digite o valor da hora trabalhadas: "))


sal_bruto = tothora * valhora

#Descontos

ir = 11/100 * sal_bruto
inss = 8/100 * sal_bruto
sindicato = 5/100 * sal_bruto

descontos = ir + inss + sindicato

sal_liquido = sal_bruto - descontos

print("O seu salario do mes é de {}".format(sal_liquido))


print("******************Descontos*******************")

print("Salario bruto R${}".format(sal_bruto))
print("Imposto de renda: {}".format(ir))
print("INSS: {}".format(inss))
print("Sindicato: {}".format(sindicato))

print("Salario bruto R${} - Descontos R${}  Total de R${}".format(sal_bruto,descontos,sal_liquido))

