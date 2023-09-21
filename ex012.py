print('Calcular aumento do salário')

sa = float(input('Qual é o valor do salário atual? R$'))
au = int(input('Qual é a porcentagem de aumento?'))
p = sa * au / 100
t = sa + p
print(f'Com um aumento de {au}%, o salário tera um acrescimo de R${p:.2f} ficando com um total de R${t:.2f}.')
