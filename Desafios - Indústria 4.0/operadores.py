'''     >>>> DESAFIO OPERADORES <<<<
            >>>> Cauã Campos <<<<       '''

from time import sleep 

##### Início do código #####

print('Olá, sou sua calculadora.')
sleep(1)

print('')

print('Abaixo, você deve colocar os números que deseja operar.')
sleep(1)
print('Lembrando que sempre será trabalhado o primeiro número pelo segundo. Ex: Meu primeiro número é 100 e o segundo é 50, nas operações vão funcionar: 100 + 50, 100 - 50, 100 / 50...')
sleep(5)
print('')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('')

print('Calculando...')
sleep(3)
print('')

# Separa uma váriavel para cada operação.

adicao = n1 + n2 
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_int = n1 // n2
potenciacao = n1 ** n1
resto_div = n1 % n2

# Realiza as operações com os números escolhidos. 

print('-⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻-')
print('')

print(f'O resultado da soma {n1} + {n2} é: {adicao}.')
sleep(1)
print('------------------------------------------------------------------------')
print(f'O resultado da subtração {n1} - {n2} é: {subtracao}.')
sleep(1)
print('------------------------------------------------------------------------')
print(f'O resultado da multiplicação {n1} x {n2} é: {multiplicacao}.')
sleep(1)
print('------------------------------------------------------------------------')
print(f'O resultado da divisão {n1} : {n2} é: {divisao}.')
sleep(1)
print('------------------------------------------------------------------------')
print(f'O resultado da divisão inteira de {n1} : {n2} é: {divisao_int}.')
sleep(1)
print('------------------------------------------------------------------------')
print(f'O resultado da potência {n1} sobre {n2} é: {potenciacao}.')
sleep(1)
print('------------------------------------------------------------------------')
print(f'O resultado do resto da divisão {n1} : {n2} é: {resto_div}.')
sleep(1)

print('')
print('-⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻-')