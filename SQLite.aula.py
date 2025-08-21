#CHAMA A BIBLIOTECA
import sqlite3
#CRIA O BANCO DE DADOS
conexao = sqlite3.connect('meu_banco_de_dados.db')
#CURSOR É A FUNÇÃO PARA PERMITIR USAR SQL EM PROGRAMAÇÃO PYTHON 
cursor = conexao.cursor()

#CRIA A TABELA
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               cidade TEXT NOT NULL        
    )


''')  
#INSERIR DADOS MA TABELA


nome = input ('Digite um nome: ')
idade = int(input('digite dua idade: '))
cidade = input('cidade: ')

#INSERE DADOS NA TABELA/BANCO DE DADOS
cursor.execute('''
    INSERT INTO pessoas (nome,idade,cidade)  
    VALUES(?,?,?)
''', (nome, idade, cidade))

#SALVA E ATUALIZA O BANCO DE DADOS
conexao.commit()




#CONSULTAR DADOS DA TABELA
#SELECIONA TODA A TABELA
cursor.execute('SELECT * FROM pessoas')
#FETCHALL TRAS PRA UMA LISTA
pessoas = cursor.fetchall()


#MOSTRAR OS DADOS CONSULTADOS
for pessoa in pessoas:
    print(f'''ID:{ pessoas[0] },Nome:{pessoa[1]},Idade: {pessoa[2]}, Cidade:{pessoa[3]})''')

#FECHA A CONEXÃO         
conexao.close()