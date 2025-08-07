## ***ATIVIDADE 2***

#Crie um sistema de notas alunos, com as seguintes operações:
#***Utilize While ou for*** 
# Sistema de notas de alunos
#- Acesso a conta com condicionais
#- 3 chances de acessar o sistema
#- Após errar 3 x mensagem que diga que a conta bloqueada 
#- Inserir notas 
#- Fazer a média

dados_alunos = {[Nomes], [Notas]}
dados_professores = {}


print('BEM VINDO - CADASTRE-SE')
login = input('Cadastre um login: ')
senha = input('Cadastre uma senha:')
print('_________________________')
dados_professores['logins'] = [login]
dados_professores['senhas'] = [senha]

for n in range(3):
    login = input('Login: ')
    senha_login = input('Senha de login: ')
    if login in dados_professores['logins'] and senha_login in dados_professores['senhas']:
        nome = input('digite o nome do aluno: ')
        nota = float(input('digite a nota do aluno: '))
        dados_alunos['Nomes'] + nome
        dados_alunos['Notas'] + nota
        condicional_notas = input('deseja inserir mais notas? ')
        while condicional_notas == 'sim':
            nota = float(input('digite a nota do aluno: '))
            dados_alunos['Notas'] + nota
            print(dados_alunos['Nomes'])
            print(dados_alunos['Notas'])
            condicional_notas = input('deseja inserir mais notas? ')
        else: print ('a média do aluno', nome, 'é: ', sum([dados_alunos['Notas']])/len([dados_alunos['Notas']]))
        encerrar = input('deseja encerrar?')
        if encerrar == 'nao': 
            condicional_notas = input('deseja inserir mais notas? ')
            while condicional_notas == 'sim':
                nota = float(input('digite a nota do aluno: '))
                dados_alunos['Notas'] + nota
                print(dados_alunos['Nomes'])
                print(dados_alunos['Notas'])
                condicional_notas = input('deseja inserir mais notas? ')
            else: print ('a média do aluno', nome, 'é: ', sum([dados_alunos['Notas']])/len([dados_alunos['Notas']]))
            print(dados_alunos['Notas'])
        else:print ('até breve!')
        break
    else:
        print('Você digitou algo errado, tente novamente')
else:
    print('Conta bloqueada!')