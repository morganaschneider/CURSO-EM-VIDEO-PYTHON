import random
p1 = str(input('Primeiro aluno'))
p2 = str(input('Segundo aluno'))
p3 = str(input('Terceiro aluno'))
p4 = str(input('Quarto aluno'))
nomes = (p1,p2,p3,p4)
escolha = random.choice(nomes)
print(f'O aluno escolhido foi {escolha}')
