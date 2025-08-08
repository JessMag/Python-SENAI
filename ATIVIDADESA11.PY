#1 - CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.
def par_ou_impar():
    n = float(input('digite um número: '))
    if n % 2 == 0:
        print('par')
    else: print('impar')

#2 - CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def multi ():
    a = float(input('digite um número: '))
    b = float(input('digite um número: '))
    c = float(input('digite um número: '))
    multi = a*b*c
    print (multi)

#3 -CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
def elev (a,b):
    eleva = a**b
    print(eleva)
    

#4 -CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

def maior(idade):
    idade = int(input('Digite sua idade: '))
    if idade == 18:
        print('você tem 18 anos !!!')
    else: pass

#5 -DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
def descubra ():
    ano = int(input('digite o ano que você nasceu: '))
    idade = 2025 - ano
    print ('você tem', idade, 'anos')

#6 -DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999



#7 -DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***
def valor_pagar(escolha,valor):
    return escolha*valor

def sistema ():
    cardapio = ['','1-SALADA', '2-MACARRONADA', '3-SANDUICHE', '4-SORVETE'] 
    precos = ['',10.00, 25.00, 14.99, 7.00]
    print ('BEM VINDO!')
    print(f''''BEM VINDO!'
                Veja nosso cardapio'
                {cardapio}
                {precos}
            ''')
    escolha = int(input('qual sua escolha: '))
    valor = (precos[escolha])
    A_pagar = [valor_pagar(escolha,valor)]
    escolha = input('deseja algo mais: ')
    while escolha == 'sim':
            escolha = int(input('o que mais escolhe: '))
            valor = (precos[escolha])
            A_pagar2 = valor_pagar(escolha,valor)
            A_pagar.append (A_pagar2)
            total = sum(A_pagar)
            escolha = input('deseja algo mais: ')
    else: print('seu total é', total)





sistema()