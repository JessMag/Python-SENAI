## ***ATIVIDADE 2***

#Crie um sistema de notas alunos, com as seguintes operações:
#***Utilize While ou for*** 
# Sistema de notas de alunos
#- Acesso a conta com condicionais
#- 3 chances de acessar o sistema
#- Após errar 3 x mensagem que diga que a conta bloqueada 
#- Inserir notas 
#- Fazer a média

dados_alunos = {}
dados_professores = {}


print('Cadastre-se professor')
login = input('Nome: ')
senha = input('Senha:')
print('_________________________')
dados_professores['logins'] = [login]
dados_professores['senhas'] = [senha]

for n in range(3):
    login = input('Login: ')
    senha_login = input('Senha de login: ')
    if login in dados_professores['logins'] and senha_login in dados_professores['senhas']:
        nome = input('digite o nome do aluno: ')
        nome = input('digite as notas doaluno: ')


    else:
        print('Você digitou algo errado, tente novamente')
else:
    print('Conta bloqueada!')

