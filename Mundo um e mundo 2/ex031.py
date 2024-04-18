dist = int(input('Qual a distância de uma viagem em Km?'))
print(f'Você está prester  a começar uma viagem de {dist}km')
if dist <= 200:
    price = dist * 0.5
    print(f'A distancia de sua viagem terá {dist} Km e custará R${price:.2f}.')
else:
    price = dist * 0.45
