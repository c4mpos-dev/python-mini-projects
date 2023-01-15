'''     >>>>> PEDRA, PAPEL E TESOURA <<<<<
               >>>> Cauã Campos <<<<            '''

#========== Início do código ==========#

from time import sleep 
import sys
import random

class crs:

    Branco = '\033[0m'	
    Vermelho = '\033[1;31m'
    Verde =	'\033[1;32m	'
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

print(f'{crs.Azul}{crs.Branco}')
print(f'{crs.Ciano}{crs.Branco}')

#========== Listas com os itens possíveis ==========#

itens = ['Pedra', 'Papel', 'Tesoura']

#========== Variável com as jogados do PC ==========#

computador = random.randint(0,2)

#========== Começo do jogo ==========#

print(f'{crs.Ciano}Ooopa, vamos jogar "pedra papel e tesoura".{crs.Branco}')
sleep(1)
print(f'{crs.Ciano}Será assim, você irá escolher entre pedra, papel ou tesoura.{crs.Branco}')
sleep(1)
print(f'{crs.Ciano}E o computador irá escolher entre esses também. (aleatoriamente) {crs.Branco}')
sleep(1)

print(f'''{crs.Ciano}
[0] Pedra
[1] Papel
[2] Tesoura
{crs.Branco}''')

jogador = int(input(f'{crs.Azul}Escolha um:{crs.Branco} '))
print('')
print(f'{crs.Azul}================={crs.Branco}')
sleep(1)
print(f'{crs.Ciano}JO{crs.Branco}')
sleep(1)
print(f'{crs.Ciano}KEN{crs.Branco}')
sleep(1)
print(f'{crs.Ciano}PÔ{crs.Branco}')
sleep(1)
print(f'{crs.Azul}================={crs.Branco}')
print('')

print(f'{crs.Ciano}Você escolheu: {itens[jogador]}{crs.Branco}')
sleep(2)
print(f'{crs.Ciano}O computador escolheu: {itens[computador]}{crs.Branco}')
print(f'{crs.Azul}======================={crs.Branco}')
print('')
sleep(1)

#========== Primeira condição ==========#

if computador == 0:

    if jogador == 0:
        print(f'{crs.Ciano}EMPATE!!!{crs.Branco}')

    elif jogador == 1:
        print(f'{crs.Ciano}VOCÊ GANHOU!!!{crs.Branco}')

    elif jogador == 2:
        print(f'{crs.Ciano}VOCÊ PERDEU!!!{crs.Branco}')

#========== Segunda condição ==========#

elif computador == 1:

    if jogador == 0:
        print(f'{crs.Ciano}VOCÊ PERDEU!!!{crs.Branco}')

    elif jogador == 1:
        print(f'{crs.Ciano}EMPATE!!!{crs.Branco}')

    elif jogador == 2:
        print(f'{crs.Ciano}VOCÊ GANHOU!!!{crs.Branco}')

#========== Terceira condição ==========#

elif computador == 2:

    if jogador == 0:
        print(f'{crs.Ciano}VOCÊ GANHOU!!!{crs.Branco}')

    elif jogador == 1:
        print(f'{crs.Ciano}VOCÊ PERDEU!!!{crs.Branco}')

    elif jogador == 2:
        print(f'{crs.Ciano}EMPATE!!!{crs.Branco}')