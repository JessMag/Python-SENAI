#Crie um e-commerce com a estrutura de dicionários.

Produtos = {
    'Livros' : ['abc','cde','efg'],
    'Tablets': ['samsung','lg'],
    'Fone' : ['jbl', 'sony']}

Preços = {
    'Livros': [ 49.99, 19.99, 64.99],
    'Tablets': [450,550],
    'Fone' : [34.99,89.99]}


print(f'''  MEU E-COMMERCE
 ----------------------------------------------------------------------
Livros:
ID 0  {Produtos['Livros'][0]} - R$ {Preços["Livros"][0]}
ID 1 {Produtos['Livros'][1]} - R$ {Preços["Livros"][1]}
ID 2  {Produtos['Livros'][2]} - R$ {Preços["Livros"][2]}
Tablets:
ID 0 {Produtos["Tablets"][0]} - R$ {Preços["Tablets"][0]}
ID 1 {Produtos["Tablets"][1]} - R$ {Preços["Tablets"][1]}
Fone:
ID 0  {Produtos["Fone"][0]} - R$ {Preços["Fone"][0]}
ID 1  {Produtos["Fone"][1]} - R$ {Preços["Fone"][1]}
----------------------------------------------------------------------
''')

carrinho =[]
meu_total = []

secao = input('escolha sua seção: ')
print (Produtos[secao])
escolha_1 = int(input('escolha pelo id: '))
carrinho.append (Produtos[secao][escolha_1])
meu_total.append (Preços[secao][escolha_1])

print (f'''
----------------------------------------------------------------------
 Seu Carrinho:
{carrinho} 
{meu_total}

Total
{sum (meu_total)}
----------------------------------------------------------------------
       ''')
                 
secao = input('escolha sua seção: ')
print (Produtos[secao])
escolha_2 = int(input('escolha pelo id: '))
carrinho.append (Produtos[secao][escolha_2])
meu_total.append (Preços[secao][escolha_2])

print (f'''
----------------------------------------------------------------------
 Seu Carrinho:
{carrinho} 
{meu_total}

Total
{sum (meu_total)}
----------------------------------------------------------------------
       ''')