alt = float(input('Digite a altura da parede'))
larg = float(input('Digite o comprimento de parede'))
mt = float(input('Digite quantos m² a tinta rende'))
al = larg * alt
lt = al / mt
print(f'A area é {al}m² e serão necessarios {lt}L de tinta para pintura.')
