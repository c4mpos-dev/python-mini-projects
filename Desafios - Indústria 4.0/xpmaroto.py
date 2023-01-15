'''     >>>>> XP MAROTO <<<<<
          >> Cauã Campos <<         '''

#========== Início do código ==========#

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

xp = 0

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print(f'{Crs.amarelo}Opa, seja bem-vindo(a) ao nosso mundo.{Crs.branco}')
print(f'{Crs.amarelo}Aqui você vai passar por algumas batalhas em busca da liberdade.{Crs.branco}')
print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
sleep(2)
print('')
nome = input(f'{Crs.ciano}Digite seu nickname:{Crs.branco} ')
print('')

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')

arma = int(input(f'''{Crs.amarelo}{nome}, Escolha a sua arma:
{Crs.ciano}
[1] Espada
[2] Adagas
[3] Machado
{Crs.branco} '''))

if arma == 1:
    arma = 'espada'

elif arma == 2:
    arma = 'adagas'

elif arma == 3:
    arma = 'machado'

print(f'{Crs.amarelo}Hm, {arma}, boa escolha.{Crs.branco}')
sleep(1)

pausa = input(f'{Crs.ciano}Assim que estiver pronto aperte ENTER:{Crs.branco} ')
print('')
sleep(1)
print(f'{Crs.amarelo}Vamos começar em, agora não tem volta.{Crs.branco}')
print(f'{Crs.amarelo}3...{Crs.branco}')
sleep(1)
print(f'{Crs.amarelo}2..{Crs.branco}')
sleep(1)
print(f'{Crs.amarelo}1.{Crs.branco}')
sleep(1)

print('')

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃ FASE 1 ▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')
print(f'{Crs.amarelo}Você deve apertar ENTER 5 vezes.{Crs.branco}')
sleep(2)
print(f'{Crs.amarelo}VALENDO!!!.{Crs.branco}')


k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')

print('')
print(f'{Crs.amarelo}Wow, você derrubou o dragão com um combo de golpes fantásticos de sua(seu) {arma}.{Crs.branco}')
sleep(1)
print(f'{Crs.amarelo}Mandou bem, {nome}. +150 de XP{Crs.branco}')
xp += 150
print('')
sleep(2)

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃ FASE 2 ▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')
print(f'{Crs.amarelo}Você deve apertar ENTER 3 vezes.{Crs.branco}')
sleep(2)
print(f'{Crs.amarelo}VALENDO!!!.{Crs.branco}')

k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')


print('')
print(f'{Crs.amarelo}QUE GOLPE FANTÁSTICO, o inimigo não entendeu nada e só aceitou a morte.{Crs.branco}')
sleep(1)
print(f'{Crs.amarelo}Mandou bem, {nome}. +200 de XP{Crs.branco}')
xp += 200
print('')
sleep(2)

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃ FASE 3 ▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')
print(f'{Crs.amarelo}Você deve apertar ENTER 7 vezes.{Crs.branco}')
sleep(2)
print(f'{Crs.amarelo}VALENDO!!!.{Crs.branco}')

k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')
k = input(f'{Crs.ciano}Aperte ENTER:{Crs.branco} ')

print('')
print(f'{Crs.amarelo}QUEEE ISSO! Você lançou sua(seu) {arma} na cabeça no monstro.{Crs.branco}')
sleep(1)
print(f'{Crs.amarelo}Mandou bem, {nome}. +340 de XP{Crs.branco}')
xp += 340
print('')
sleep(2)

print(f'{Crs.amarelo}{nome}, você conquistou sua liberdade!{Crs.branco}')
print('')

print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃ TOTAL DE XP ADQUIRIDO ▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print(f'{Crs.amarelo}{(xp)}{Crs.branco}')
print(f'{Crs.vermelho}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
sys.exit()