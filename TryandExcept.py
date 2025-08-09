#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

def teste1 ():
    try: 
        numero = int(input('insira um numero: '))
        print (numero)
    except:
        print('houve um erro!')


#Exercício 2:
#Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

def teste2 ():
    try:
        n1 = float(input('n1 = '))
        n2 = float(input('n2 = '))
        print (n1, 'dividido por',n2 ,'é: ', n1/n2)
    except ZeroDivisionError:
        print('n2 não pode ser zero!')
    
#Exercício 3:
#Crie uma função que aceite uma lista e um índice como entrada e retorne o parametro do elemento naquele índice. Manipule a exceção caso o índice seja inválido
# (caso imprima um indice que não exista na lista).

def teste3():
    try:
        lista = [1,2,3,4]
        indice = int(input('digite o indice: '))
        print(lista[indice])
    except IndexError:
        print ('esse indice não existe na lista, tente novamente!')


