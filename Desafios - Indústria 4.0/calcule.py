'''     >>>> DESAFIO CALCULE <<<<
            >> Cauã Campos <<       '''

from time import sleep 
import sys

class Crs:

    branco = '\033[0m'	
    vermelho = '\033[1;31m'
    verde =	'\033[1;32m	'
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

#========== Início do código ==========#

print(f'{Crs.ciano}Olá, sou sua calculadora, você pode escolher 2 números, e deixa que eu faço o resto.{Crs.branco}')
sleep(1)
print(f'{Crs.ciano}Lembrando que sempre será trabalhado o primeiro número pelo segundo.{Crs.branco}')

print('')

#========== O usuário escolhe os números com quais deseja operar ==========#

while True:

    n1 = float(input(f'{Crs.azul}Digite o primeiro número:{Crs.branco} '))
    sleep(1)
    n2 = float(input(f'{Crs.azul}Digite o segundo número:{Crs.branco} '))

    print('')

    #========== São declaradas as operações ==========#

    adicao = n1 + n2 
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    divisao_int = n1 // n2
    potenciacao = n1 ** n1
    resto_div = n1 % n2

    #========== Realiza as operações com os números escolhidos ==========#

    print(f'{Crs.azul}-⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻-{Crs.branco}')
    print('')

    print(f'''{Crs.vermelho}Adição: {n1} + {n2} {Crs.verde}
    Soma: {adicao}.{Crs.branco}''')
    sleep(2)
    print(f'{Crs.azul}========================================================================{Crs.branco}')
    print(f'''{Crs.vermelho}Subtração: {n1} - {n2} {Crs.verde}
    Diferença: {subtracao}.{Crs.branco}''')
    sleep(2)
    print(f'{Crs.azul}========================================================================{Crs.branco}')
    print(f'''{Crs.vermelho}Multiplicação: {n1} x {n2} {Crs.verde}
    Produto: {multiplicacao}.{Crs.branco}''')
    sleep(2)
    print(f'{Crs.azul}========================================================================{Crs.branco}')
    print(f'''{Crs.vermelho}Divisão {n1} : {n2} {Crs.verde}
    Quociente: {divisao}.{Crs.branco}''')
    sleep(2)
    print(f'{Crs.azul}========================================================================{Crs.branco}')
    print(f'''{Crs.vermelho}Divisão (Somentos com inteiros): {n1} : {n2} {Crs.verde}
    Quociente: {divisao_int}.{Crs.branco}''')
    sleep(2)
    print(f'{Crs.azul}========================================================================{Crs.branco}')
    print(f'''{Crs.vermelho}Potenciação: {n1} sobre {n2} {Crs.verde}
    Potência: {potenciacao}.{Crs.branco}''')
    sleep(2)
    print(f'{Crs.azul}========================================================================{Crs.branco}')
    print(f'''{Crs.vermelho}Resto da divisão {n1} : {n2} {Crs.verde}
    Resto: {resto_div}.{Crs.branco}''')
    sleep(2)

    print('')
    print(f'{Crs.azul}-⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻--⎽__⎽-⎻⎺⎺⎻-⎽__⎽--⎻⎺⎺⎻-{Crs.branco}')
    print('')

    print(f'''{Crs.verde}
    [1] Sim{Crs.vermelho}
    [2] Não
    {Crs.branco}''')

    conti = int(input(f'{Crs.azul}Deseja fazer mais operações?{Crs.branco} '))
    print('')

    print(f'{Crs.azul}========================================================================{Crs.branco}')

    print('')

    if conti == 1:
        print(f'{Crs.ciano}Opa, vamos lá.{Crs.branco}') 
        print('')
    elif conti == 2:
        print(f'{Crs.ciano}Mas já vai? lembre-se que estamos aqui se precisar, até mais!{Crs.branco}')
        sys.exit()
    elif conti > 2:
        print(f'{Crs.ciano}Vou entender isso como um sim, vamos lá.{Crs.branco}')
        print('')