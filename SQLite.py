import sqlite3
conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXITS pessoas(
               id INTEGER PRIMARY KEY AUTOINCREMEN NOT NULL,
               nome TEXT NOT NULL
               idade INTEGER NOT NULL
               cidade TEXT NOT NULL        
    )

''')   
#INSERIR DADOS MA TABELA

nome = input ('Digite um nome: ') 
idade = int(input('digite dua idade: '))
cidade = input('cidade: ') 

cursor.execute('''
    INSERT INTO pessoas (nome,idade,cidade)  
    VALUES(?,?,?)
''', (nome, idade, cidade))

conexao.commit()


#CONSULTAR DADOS DA TABELA
cursor.execute('SELECT * FROM pessoas')
pessoas = cursor.fetchall()

#MOSTRAR OS DADOS CONSULTADOS
for pessoa in pessoas:
    print(f'''ID:{ pessoas[0] },Nome:{pessoa[1]},Idade: {pessoa[2]}, Cidade:{pessoa[3]})''')
          
conexao.close()