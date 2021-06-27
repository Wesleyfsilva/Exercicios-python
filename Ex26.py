print("**********************************************")
print("************Folha de pagamento****************")
print("**********************************************")

horas = float(input("Digite o total de horas trabalhadas: "))
valhora = float(input("Digite o valor de cada hora trabalhada: "))

sal = horas * valhora
ir = (5/100) * sal
ir_2 = (10/100) * sal
ir_3 = (20/100) * sal
inss = (10/100) * sal
fgts = (11/100) * sal
desc = ir + inss 
desc_2 = ir_2 + inss 
desc_3 = ir_3 + inss 
salliq = sal - desc
salliq_2 = sal - desc_2
salliq_3 = sal - desc_3
sal_sem = sal - inss

if sal <= 900:
    print("Salario bruto ( {:.0f} * {:.2f}) = {:.2f}".format(horas,valhora,sal))
    print("(-) IR                 : ISENTO")
    print("(-) INSS (10%)         : {:.2f}".format(inss))
    print("(-) FGTS (11%)         : {:.2f}".format(fgts))
    print("Total de descontos     :  0.00")
    print("Salario liquido        : {:.2f}".format(sal_sem))
elif sal > 900 and sal <= 1500:
    print("Salario bruto ( {:.0f} * {:.2f}) = {:.2f}".format(horas,valhora,sal))
    print("(-) IR (5%)            : {:.2f}".format(ir))
    print("(-) INSS (10%)         : {:.2f}".format(inss))
    print("(-) FGTS (11%)         : {:.2f}".format(fgts))
    print("Total de descontos     : {:.2f}".format(desc))
    print("Salario liquido        : {:.2f}".format(salliq))
elif sal > 1500 and sal <= 2500:
    print("Salario bruto ( {:.0f} * {:.2f}) = {:.2f}".format(horas,valhora,sal))
    print("(-) IR (10%)            :{:.2f}".format(ir_2))
    print("(-) INSS (10%)         : {:.2f}".format(inss))
    print("(-) FGTS (11%)         : {:.2f}".format(fgts))
    print("Total de descontos     : {:.2f}".format(desc_2))
    print("Salario liquido        : {:.2f}".format(salliq_2))
elif sal > 2500:
    print("Salario bruto ( {:.0f} * {:.2f}) = {:.2f}".format(horas,valhora,sal))
    print("(-) IR (20%)            :{:.2f}".format(ir_3))
    print("(-) INSS (10%)         : {:.2f}".format(inss))
    print("(-) FGTS (11%)         : {:.2f}".format(fgts))
    print("Total de descontos     : {:.2f}".format(desc_3))
    print("Salario liquido        : {:.2f}".format(salliq_3))

    



