'''     >>>>> DESAFIO BHASKARA <<<<<
            >>>> Cauã Campos <<<<         '''

#========== Início do código ==========#

from time import sleep 
import sys
import math

class Crs:

    branco = '\033[0m'	
    vermelho = '\033[1;31m'
    verde =	'\033[1;32m'
    amarelo	= '\033[1;33m'	
    azul = '\033[1;34m'	                
    magenta = '\033[1;35m'	
    ciano = '\033[1;36m'	
    cinzaclaro = '\033[1;37m'	
    cinzaescuro = '\033[1;90m'	
    vermelhoclaro = '\033[1;91m'	
    verdeclaro	= '\033[1;92m'	
    amareloclaro = '\033[1;93m'	
    azulclaro = '\033[1;94m'
    magentaclaro = '\033[1;95m'	
    cianoclaro = '\033[1;96m'


print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print(f'{Crs.amarelo}Opa, querendo uma calculadora de bhaskara?{Crs.branco}')
print(f'{Crs.amarelo}Achoou, vamos lá.{Crs.branco}')
print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')
sleep(1)

a = int(input(f'{Crs.amarelo}Digite a:{Crs.branco} '))
b = int(input(f'{Crs.amarelo}Digite b:{Crs.branco} '))
c = int(input(f'{Crs.amarelo}Digite c:{Crs.branco} '))

print('')

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

print('')
print(f'{Crs.amarelo}EQUAÇÃO:{Crs.branco}')
print('')
print(f'x = -{b} ± √{b}^2-4.{a}.{c} / 2.{a}')
print('')
print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

delta = (b**2)-(4*a*c)

if delta < 0:
        print ('A raiz é negativa, isso não existe. :)')
        sys.exit()
 
else :
    delta = math.sqrt(delta)

    x1 = (-b+delta)/(2*a)

    x2 = (-b-delta)/(2*a)

print('')

print(f'{Crs.amarelo}RESULTADO:{Crs.branco}')
print('')

print(f'''X1 = %s 
X2 = ''' % x1, x2 )

print('')
print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print(f'{Crs.branco}')