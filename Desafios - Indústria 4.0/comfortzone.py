'''     >>>> DESAFIO COMFORT ZONE <<<<
            >>>> Cauã Campos <<<<       '''

from time import sleep
import sys

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

    
#========== Início do código ============#

print(f'{crs.Vermelho}Seja bem-vindo(a) à C4MP0$ Stúdio.{crs.Branco}')
sleep(2)
print('')
print(f'{crs.Vermelho}Vamos a criação do personagem?{crs.Branco}')
sleep(1)
print(f'{crs.Vermelho}Preparando perguntas...{crs.Branco}')
sleep(3)
print('')
nickname = input(f'{crs.Amarelo}Digite seu nome:{crs.Branco} ')
print('')

#========== Escolha do gênero ============#

print(f'{crs.Vermelho}{nickname}, vamos começar a montar seu personagem.{crs.Branco}')
print(f'''{crs.Vermelho}
[1] Homem
[2] Mulher
{crs.Branco}''')

genero = int(input(f'{crs.Amarelo}Selecione seu gênero:{crs.Branco} '))

if genero == 1:
    genero = 'homem'

elif genero == 2:
    genero = 'mulher'

print('')

#========== Escolha da cor dos olhos ============#

print(f'{crs.Vermelho}{nickname}, agora que já selecionou o gênero, é a hora da cor dos olhos.{crs.Branco} ')
print(f'''{crs.Vermelho}
[1] Castanho
[2] Castanho Claro
[3] Verde
[4] Azul
{crs.Branco}''')

olhos = int(input(f'{crs.Amarelo}Selecione a cor dos olhos:{crs.Branco} '))

if olhos == 1:
    olhos = 'castanhos'

elif olhos == 2:
    olhos = 'castanhos claro'

elif olhos == 3:
    olhos = 'verdes'

else:
    olhos = 'azuis'

print('')

#========== Escolha do estilo do cabelo ============#

print(f'{crs.Vermelho}{nickname}, agora escolha o estilo do cabelo.{crs.Branco}')
print(f'''{crs.Vermelho}
[1] Curto
[2] Comprido
{crs.Branco}''')

cabelo = int(input(f'{crs.Amarelo}Selecione o estilo do cabelo:{crs.Branco} '))

if cabelo == 1:
    cabelo = 'curto'

elif cabelo == 2:
    cabelo = 'comprido'

print('')

#========== Escolha da cor da pele ============#

print(f'{crs.Vermelho}{nickname}, pra finalizar o personagem, escolha a cor da pele.{crs.Branco} ')
print(f'''{crs.Vermelho}
[1] Branca
[2] Morena Clara
[3] Morena
[4] Negra
{crs.Branco}''')

pele = int(input(f'{crs.Amarelo}Selecione a cor da pele:{crs.Branco} '))

if pele == 1:
    pele = 'branca'

elif pele == 2:
    pele = 'morena clara'

elif pele == 3:
    pele = 'morena'

else:
    pele = 'negra'


print('')

#========== Escolha da classificação da série ============#

print(f'{crs.Vermelho}{nickname}, pra fechar com chave de ouro, escolha a classificação da sua série.{crs.Branco} ')
print(f'''{crs.Vermelho}
[1] Romance
[2] Comédia
[3] Ação
[4] Terror
{crs.Branco}''')

serie = int(input(f'{crs.Amarelo}Selecione a cor da pele:{crs.Branco} '))

if serie == 1:
    serie = 'romance'

elif serie == 2:
    serie = 'comédia'

elif serie == 3:
    serie = 'ação'

else:
    serie = 'terror'

print('')

print(f'{crs.Vermelho}{nickname}, na série, você será {genero}, terá olhos {olhos} e cabelo {cabelo}, e a cor de sua pele será {pele}.{crs.Branco}')
print(f'{crs.Vermelho}A classificação da sua série será: {serie}.{crs.Branco}')