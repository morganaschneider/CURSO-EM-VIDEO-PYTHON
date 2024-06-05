from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento:'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} em {atual}')
if idade == 18:
 print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar, no ano de {nasc + 18}')
elif idade > 18:
    print(f'Você ja deveria ter se alistado há {18 - idade} anos')