num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1]Converter para BINÁRIO
[2]Converter para OCTAL
[3]Converter para HEXADECIMAL
''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'Convertido para BINÁRIO é igual a {num,bin(num)}')
elif opção == 2:
        print(f"Convertido para OCTAL é igual a {num, oct(num)}")
elif opção == 3:
    print(f'Convertido para HEXADECIMAL é igual a {num,hex(num)}')

