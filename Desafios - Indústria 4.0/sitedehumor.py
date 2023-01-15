'''     >>>> DESAFIO SITE DE HUMOR <<<<
             >>>> Cauã Campos <<<<       '''

from time import sleep 
import sys
import random

class crs:

    Branco = '\033[0m'	
    Vermelho = '\033[1;31m'
    Verde =	'\033[1;32m'
    Amarelo	= '\033[1;33m'	
    Azul = '\033[1;34m'	                
    Magenta = '\033[1;35m'	
    Ciano = '\033[1;36m'	
    CinzaClaro = '\033[1;37m'	
    CinzaEscuro = '\033[1;90m'	
    VermelhoClaro = '\033[1;91m'	
    VerdeClaro	= '\033[1;92m'	
    AmareloClaro = '\033[1;93m'	
    AzulClaro = '\033[1;94m'
    MagentaClaro = '\033[1;95m'	
    CianoClaro = '\033[1;96m'

#========== Início do código ==========#

print(f'{crs.Vermelho}============================================{crs.Branco}')
print(f'{crs.Amarelo}Opa, seja bem-vindo(a) ao nosso site.{crs.Branco}')
print(f'{crs.Amarelo}Vamos começar com as perguntas, se prepare.{crs.Branco}')
print(f'{crs.Vermelho}============================================{crs.Branco}')

print('')

nome = input(f'{crs.Amarelo}Digite seu nome:{crs.Branco} ')
idade = input(f'{crs.Amarelo}{nome}, agora digite sua idade:{crs.Branco} ')

print('')
print(f'{crs.Vermelho}============================================{crs.Branco}')
print(f'''{crs.Amarelo}
[1] Estou bem.
[2] Estou mal.
{crs.Branco}''')
sleep(1)

p1 = int(input(f'{crs.Amarelo}{nome}, como você está?{crs.Branco} '))

if p1 == 1:
    print(f'{crs.Amarelo}Aí sim, ficamos felizes em saber que você está bem.{crs.Branco}')
    print('')
    print(f'{crs.Vermelho}============================================{crs.Branco}')
    print(f'''{crs.Amarelo}
[1] Sim.
[2] Não, to de boa.
    {crs.Branco}''')
    sleep(1)
    r1 = int(input(f'{crs.Amarelo}Eaí, esteve muito cansado(a) nos últimos dias?{crs.Branco} '))

    if r1 == 2:
        print(f'{crs.Amarelo}Então tá tudo tranquilo, até a próxima, obrigado por acessar nosso site!{crs.Branco}')
        print('')
        print(f'{crs.Vermelho}============================================{crs.Branco}')
        sys.exit()

    elif r1 == 1:
        print(f'{crs.Vermelho}============================================{crs.Branco}')
        print('')

        rr1 = input(f'{crs.Amarelo}Vish, o que você tem feito?{crs.Branco} ')
        print('')
        print(f'{crs.Amarelo}Hmmm, entendi, procure descansar um pouco.{crs.Branco} ')
        print(f'{crs.Amarelo}Até a próxima, obrigado por acessar nosso site!{crs.Branco} ')
        print(f'{crs.Vermelho}============================================{crs.Branco}')
        sys.exit()

#================================== 2 =================================#

elif p1 == 2:
    rr2 = input(f'{crs.Amarelo}Porque, o que houve?{crs.Branco}')
    print('')
    print(f'{crs.Amarelo}Putz, logo logo isso melhora, só acreditar.{crs.Branco}')
    print(f'{crs.Vermelho}============================================{crs.Branco}')
    print(f'''{crs.Amarelo}
[1] Sim.
[2] Não, to de boa.
    {crs.Branco}''')
    sleep(1)
    rr1 = int(input(f'{crs.Amarelo}Esteve muito cansado(a) nos últimos dias?{crs.Branco} '))

    if rr1 == 2:
        print(f'{crs.Amarelo}Então tá bom, até a próxima, obrigado por acessar nosso site!{crs.Branco}')
        print('')
        print(f'{crs.Vermelho}============================================{crs.Branco}')
        sys.exit()

    elif rr1 == 1:
        print(f'{crs.Vermelho}============================================{crs.Branco}')
        print('')

        rrr1 = input(f'{crs.Amarelo}Vish, o que você tem feito?{crs.Branco} ')
        print('')
        print(f'{crs.Amarelo}Hmmm, entendi, procure descansar um pouco.{crs.Branco} ')
        print(f'{crs.Amarelo}Até a próxima, obrigado por acessar nosso site!{crs.Branco} ')
        print(f'{crs.Vermelho}============================================{crs.Branco}')
        sys.exit()