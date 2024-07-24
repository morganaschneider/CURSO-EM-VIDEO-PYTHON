peso = float(input('Qual seu peso ? (Kg)'))
altura = float(input('Qual sua altura (m)'))
imc = peso/(altura ** 2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no seu peso ideal')
elif imc < 30:
    print('Você está com sobrepeso')
elif imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')