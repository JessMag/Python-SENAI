#EXERCÍCIOS 1: 
#Utilize condicionais

# 1*  Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
#n = int(input('digite um numero: '))

#if n == 0:
#    print('é igual a 0')
#elif n > 0:
#    print ('numero positivo')
#else: print ('negativo')


# 2* Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

#idade = int(input('digite sua idade: '))

#if idade >=16:
 #   print ('pode votar')
#else: print('voce não pode votar')

# 3* Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

#v1 = int(10)

#if (v1) % 2 == 0:
#    print ('par')
#else: print('impar')

# 4* # Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

#lado1 = float(input('digite lado 1: '))
#lado2 = float(input('digite lado 2: '))
#lado3 = float(input('digite lado 3: '))

#if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
#    print ('triangulo equilátero')
#elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
#    print ('triangulo escaleno')
#else: print ('triangulo isósceles')

# 5* Determine se um número é múltiplo de 5 e 7.

#n1 = int(input('digite um numero: '))
#resultado = n1 % 5
#resultado_1 = n1 % 7

#if resultado == 0 and resultado_1 == 0:
#    print ('este numero É multiplo de 5 e 7')
#elif resultado == 0:
#    print ('este numero é multiplo de 5')
#elif resultado_1 == 0:
#    print ('este numero é multiplo de 7')
#else: print ('este numero não é multiplo de 5 e 7')

# 6* Verifique se um número é positivo e maior que 10
#n2 = int(input('digite um numero: '))

#if n2 > 0 and n2 > 10:
#    print ('número é positivo e maior que 10')
#else: print(False)

# 7 Verifique se um número é divisível por 3 ou 5.
n3 = int(input('digite um numero: '))

resultado = n3 % 3
resultado_1 = n3 % 5

if  resultado == 0:
    print ('este numero é divisível por 3')
elif resultado_1 == 0:
    print ('este numero é divisível por 5')
else: print ('este numero não é divisível por 3 ou 5')