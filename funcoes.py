import random

#1 - Crie um número aleatório de 5,10
def aleatorio(n1,n2):
    return random.randint (n1,n2)
  

#2 - Crie 3 números aleatórios
def _3_aleatorios(n1,n2):
    a = random.randint (n1,n2)
    b = random.randint (n1,n2)
    c = random.randint (n1,n2)
    return a,b,c

#3 - Crie um número aleatório entre 10 a 30 utilize o range()
def aleatorio_2(n1,n2):
    return range(n1,n2)



#4 - Contagem regressiva simples**
#Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)





#**5 - Soma de números pares**
#Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
# Peça ao usuário que insira um número inteiro 
# faça o loop com range e for ate´o numero
# positivo e, em seguida, calcule a soma de 
# todos os números pares de 2 até o número inserido.
#(use módulo, if, for)

#def soma_pares(n):
 #   for x in range (n):





#6 - Tabuada de multiplicação
#Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
#(while ou for )

def tabuada(a):
    for n in range (1,10):
        resultado = n*a
        print (n,'x',a,'=', resultado)   




#7 -  Números ímpares reversos**
#Exiba uma contagem regressiva de números ímpares de 99 a 1.
#(for)