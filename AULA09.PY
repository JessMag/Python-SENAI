## ***ATIVIDADE 1***

#1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
n = 0
while n < 1001:
    print(n)
    n=n+1
    
#2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

quantidade_pessoas = 10
pessoas = []

while quantidade_pessoas > 0:
    pessoas.append(input('digite o nome da pessoa: '))
    quantidade_pessoas = quantidade_pessoas-1

print ('lista de pessoas: ', pessoas)