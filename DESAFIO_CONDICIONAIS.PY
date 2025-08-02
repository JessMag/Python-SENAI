clientes = []
idades = []
quartos =['Simples','Duplo','Luxo']
valores = [100,150,250]



print('''----- BEM VINDO AO HOTEL ---
      ''')
c1 = input('digite seu nome: ')
i1 = int(input('digite sua idade: '))
clientes.extend (c1)

if i1 < 18:
    print ('menores de idade não são autorizados para reserva')
else: c2 = input('voce possui acompanhante? S ou N > ')

if i1 < 18:
    print ('')
elif c2 == 'S':
        Ac1 = input('digite nome do acompanhante: ')
elif c2 == 'S':
        clientes.extend (Ac1)
else: print ('escolha seu quarto: ', quartos)
 
if i1 < 18:
    print ('')
elif c2 == 'S':
        i2 = input('digite idade do acompanhante: ')
elif c2 == 'S':
        idades.extend (i2)
else: print ('escolha seu quarto: ', quartos)

if i1 < 18:
    print ('')
else: c3 = input('voce possui mais 1 acompanhante? S ou N > ')

if i1 < 18:
    print ('')
elif c3 == 'S':
        Ac2 = input('digite nome do acompanhante: ')
elif c3 == 'S':
        clientes.extend (Ac2)
elif c3 == 'S': 
      print ('escolha seu quarto: ', quartos)
 
if i1 < 18:
    print ('')
elif c3 == 'S':
        i3 = input('digite idade do acompanhante: ')
elif c3 == 'S':
        idades.extend (i3)
else: print ('escolha seu quarto: ', quartos)


print ('Clientes: ', clientes)