'''     >>>>> DESAFIO DUNGEON <<<<<
             >> Cauã Campos <<         '''

#========== Início do código ==========#

from time import sleep 
import sys
import random

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

#========== Introdução do game ==========#

print(f'{Crs.ciano}=================================================================================={Crs.branco}')
print(f'{Crs.vermelho}Oopa, falae, vamos jogar Dungeon? é assim:{Crs.branco}')
sleep(1)
print(f'{Crs.vermelho}Você e eu, vamos jogar 2 dados cada um, a soma que der maior ganha.{Crs.branco}')
print(f'{Crs.ciano}=================================================================================={Crs.branco}')

print('')

nome = input(f'{Crs.verde}Digite seu nome:{Crs.branco} ')

print('')

start = input(f'{Crs.verde}{nome}, aperte ENTER para jogar:{Crs.branco} ')

print('')

print('')
sleep(1)
print(f'{Crs.vermelho}Ok, vamos lá...{Crs.branco}')
sleep(1)
print(f'{Crs.vermelho}3...{Crs.branco}')
sleep(1)
print(f'{Crs.vermelho}2..{Crs.branco}')
sleep(1)
print('')

arma = int(input(f'''{Crs.vermelho}ÔÔÔ perae, esqueci de te avisar, isso é uma guerra, então escolha seu armamento:{Crs.verde}
[1] M4A4   
[2] AK-47
[3] AUG 
{Crs.branco} '''))

if arma == 1:
    arma = 'M4A4'

elif arma == 2:
    arma = 'AK-47'

elif arma == 3:
    arma = 'AUG'

else:
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print(f'{Crs.vermelho}Você foi sem arma {nome}, obviamente, você perdeu. R.I.P{Crs.branco}') 
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    sys.exit()

print('')

print(f'{Crs.ciano}=================================================================================={Crs.branco}')
print(f'{Crs.vermelho}Elá é potente hein! boa escolha, {nome}! vamos lá.{Crs.branco}')
pausa = input(f'{Crs.verde}Aperte ENTER para iniciar:{Crs.branco} ')
sleep(1)
print(f'{Crs.ciano}=================================================================================={Crs.branco}')

print('')

while True:

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = random.randint(1,6)
    dado4 = random.randint(1,6)
    soma = dado1 + dado2
    soma2 = dado3 + dado4

    go = input(f'{Crs.verde}{nome}, aperte ENTER para jogar o dado:{Crs.branco} ')

    print('')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print(f'{Crs.vermelho}Você jogou o primeiro dado, resultado: {Crs.ciano}{dado1}{Crs.branco}')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')

    gogo = input(f'{Crs.verde}{nome}, aperte ENTER para jogar o segundo dado:{Crs.branco} ')

    print('')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print(f'{Crs.vermelho}Você jogou o outro dado, resultado: {Crs.ciano}{dado2}{Crs.branco}')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print('')

    print(f'{Crs.vermelho}{nome}, a soma dos seus dados foram de: {Crs.ciano}{soma}{Crs.branco}')
    print('')
    print(f'{Crs.vermelho}Agora é minha vez.{Crs.branco}')
    sleep(2)

    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print(f'{Crs.vermelho}Eu joguei o primeiro dado, resultado: {Crs.ciano}{dado3}{Crs.branco}')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')

    sleep(2)

    print('')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print(f'{Crs.vermelho}Joguei o outro dado, resultado: {Crs.ciano}{dado4}{Crs.branco}')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print('')

    print(f'{Crs.vermelho}A soma dos meus dados foram de: {soma2}{Crs.branco}')
    print('')
    print(f'{Crs.ciano}=================================================================================={Crs.branco}')
    print('')

    if soma > soma2:
        print(f'{Crs.vermelho}{nome}, você me executou com sua {arma}. :x{Crs.branco}')

    elif soma2 > soma:
        print(f'{Crs.vermelho}{nome}, eu te executei com minha M4A4. :x{Crs.branco}')

    elif soma == soma2:
        print(f'{Crs.vermelho}EMPATE!!!{Crs.branco}')

    print('')
    sleep(3)
    cont = int(input(f'''{Crs.vermelho}Quer jogar denovo?{Crs.verde}
[1] Sim   
[2] Não
{Crs.branco} '''))
    print('')

    if cont == 2:
        print(f'{Crs.vermelho}Obrigado por jogar, até a próxima!{Crs.branco}')
        sys.exit()





