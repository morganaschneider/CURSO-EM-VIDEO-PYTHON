palavra=input('Digite algo:')
print(f'O tipo primitivo desse valor é{type(palavra)}')
print(f'Só tem espaços?{palavra.isspace()}') 
print(f'É um numero?{palavra.isalnum()}')
print(f'Está em maiscúlas?{palavra.isupper()}')
print(f'Está em minúsculas?{palavra.islower()}')
print(f'Está capitalizada?{palavra.istitle()}')