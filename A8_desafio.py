#Desafio 1:  Condicionais***

#Sistema de Reservas de Hotel:***
#Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.
#1- Cadastro de Cliente: O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.
#2- Reservas de Quartos: O sistema deve oferecer 3 tipos de quartos:"Simples", "Duplo" e "Luxo".
#3- Cada cliente deve escolher um quarto para sua estadia.
#O preço da diária varia conforme o tipo de quarto:
#Simples: R$ 100,00 por dia.
#Duplo: R$ 150,00 por dia.
#Luxo: R$ 250,00 por dia.***
#4-Cálculo da Estadia: O usuário deve informar quantos dias cada cliente ficará no hotel. O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

dados = {}
print('Cadastre-se: ')
nome1 = input('Nome: ')
idade1 = int(input('Idade: '))
senha1 = input('Senha:')
nome2 = input('Nome: ')
idade2 = int(input('Idade: '))
senha2 = input('Senha:')
dados['nomes'] = [nome1,nome2]
dados['idades'] = [idade1, idade2]
dados['senhas'] = [senha1, senha2]
print('DADOS CADASTRADOS: ', dados)
# ------------
# login = input('Login: ')
# senha_login = input('Senha de login: ')
for n in range(2):
    login = input('Login: ')
    senha_login = input('Senha de login: ')
    if login in dados['nomes'] and senha_login in dados['senhas']:
        print('''Tipos de quartos
        1 - Simples: R$ 100,00 por dia.
        2 - Duplo: R$ 150,00 por dia.
        3 - Luxo: R$ 250,00 por dia.
        ''')
        quartos = ['',100.0,150.0,250.0]
        nomes_quartos = ['', 'Simples', 'Duplo','Luxo']
        quarto1 = int(input(f'Escolha o quarto {nome1} pelo ID 1 - 2 -3'))
        quant_dias1 = int(input(f'Quantidade Dias do {nome1}: '))
        calculo_1 = quartos[quarto1] * quant_dias1
        print(f'O cliente {nome1}, escolheu o quarto{nomes_quartos[quarto1]}')
        print(f'Total - cliente {nome1}, R$ {calculo_1}')
        dados['quartos'] = [quartos[quarto1]]
        quarto2 = int(input(f'Escolha o quarto {nome2} pelo ID 1 - 2 -3'))
        quant_dias2 = int(input(f'Quantidade Dias do {nome2}: '))
        calculo_2 = quartos[quarto2] * quant_dias2
        print(f'O cliente {nome1}, escolheu o quarto{nomes_quartos[quarto1]}')
        print(f'Total - cliente {nome2}, R$ {calculo_2}')
        dados['quartos'] = [quartos[quarto1]]
        dados['entradas'] = [calculo_1,calculo_2]
        print('DADOS CADASTRADOS:', dados)
    else:
        print('Você digitou algo errado, tente novamente')
else:
    print('Conta bloqueada!')