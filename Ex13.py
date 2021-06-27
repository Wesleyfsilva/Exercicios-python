sexo = str(input("Qual o seu sexo? M/F "))
altura = float(input("Qual a sua altura? "))

peso_ideal = 0

if sexo == "m":
    peso_ideal = (72.7 * altura) - 58 

else:
    peso_ideal = (62.1 * altura) - 44.7 

print("O seu peso ideal é de {:.1f}".format(peso_ideal))
