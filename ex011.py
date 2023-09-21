value = float(input(' Qual o preço ?'))
discount = value * (5 / 100)
final = value - discount
print(f'O valor final com desconto é {final:.2f}')
