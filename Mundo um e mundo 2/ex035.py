x = float(input('Digite o valor da primeira reta: '))
y = float(input('Agora mais um: '))
z = float(input('A terceira reta: '))
if abs(y-z)<x<y+z:
    if abs(z-x)<y<z+x:
        if abs(x-y)<z<x+y:
            print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não poderiam formar um triângulo.')