#CRIE UM BANCO DE DADOS PARA UMA AGENCIA DE MARKETING 
#PRECISA  CADASTRAR OS LEADS DA AGENCIA:

#DADOS: 

#NOME 
#IDADE
#EMAIL 
#ENDEREÇO
#TRABALHO
#GRADUÇÃO 
#APLIQUE TODAS DAS TRANSAÇÕES CITADAS ACIMA:


import sqlite3
conexao = sqlite3.connect('dados_agencia.db')
conn = conexao.cursor()

conn.execute ('''
    CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            endereco TEXT NOT NULL,
            trabalho TEXT NOT NULL,
            graduacao TEXT NOT NULL
        )

    ''')

novo_lead = True
while novo_lead:
    nome = input ('nome: ')
    email = input('e-mail: ')
    endereco = input('endereço: ')
    trabalho = input('trabalho: ')
    graduacao= input ('graduação: ')

    conn.execute('''
    INSERT INTO leads (nome,email,endereco,trabalho,graduacao)
    VALUES (?,?,?,?,?)''',(nome,email,endereco,trabalho,graduacao))

    novo_lead = input('inserir novo lead? ')
    if novo_lead == 'não':
        novo_lead = False
        
    conexao.commit()

conexao.close() 