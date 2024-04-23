sal = float(input('Digite o salário de um funcionário! R$'))
if sal > 1250:
 print('O salário que era R${:.2f}, com um aumento de 10%, passa a ser R${:.2f}'.format(sal, (sal*10/100)+sal))
else:
    print('O salário que era R${:.2f}, com um aumento de 15%, passa a ser R${:.2f}'.format(sal, (sal*15/100)+sal))

