casa = float(input('Valor da casa R$'))
salário = float(input('Salario do comprador R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
print(f'Para paggar uma casa de R$ em {anos,casa}')
print(f'A prestação será de  de R$ em {prestação}')

