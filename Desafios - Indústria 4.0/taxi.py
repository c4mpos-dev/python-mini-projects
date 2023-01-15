'''     >>>>> DESAFIO TÁXI <<<<<
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

preco = 0

print(f'{Crs.ciano}Você chegou no Rio de Janeiro após uma viagem de avião, você está no aeroporto Galeão...{Crs.branco}')
print('')
sleep(2)
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print(f'{Crs.ciano}Opa, seja bem-vindo(a), sou o motorista C4MP0$.{Crs.branco}')
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')
sleep(1)

print(f'{Crs.ciano}Aqui temos destinos programados para vocês(turistas) conhecerem.{Crs.branco}')

print(f'''{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.ciano}
Escolha:

[1] Copa Cabana (Praia fantásticas)
[2] Jardim Botânico (Conecte-se com a natureza)
[3] Cristo Redentor (Paisagem espetacular, impossível de esquecer) {Crs.branco}''')
print('')

resposta = int(input(''))
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

print('')

#========================= 1 =========================#

if resposta == 1:
    print(f'{Crs.ciano}Temos 2 caminhos.{Crs.branco}')
    print(f'''{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.ciano}
Escolha:

[1] Mais rápido (Iremos direto ao ponto pela rodovia) R$50,00
[2] Mais Lento (Iremos passar por paisagens incríveis até Copa Cabana) R$75,00{Crs.branco}''')
    print('')

    copa = int(input(''))
    print('')
    print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

    if copa == 1:
        print(f'{Crs.ciano}Ok então, sem paisagens.{Crs.branco}')
        preco += 50

    elif copa == 2:
        print(f'{Crs.ciano}Você não vai se arrepender.{Crs.branco}')
        preco += 75

    print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

#========================= 2 =========================#

if resposta == 2:
    print(f'{Crs.ciano}Temos 2 caminhos.{Crs.branco}')
    print(f'''{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.ciano}
Escolha:

[1] Mais rápido (Iremos direto ao ponto pela rodovia) R$50,00
[2] Mais Lento (Iremos passar por paisagens incríveis até o Jardim Botânico) R$75,00{Crs.branco}''')
    print('')

    botanico = int(input(''))
    print('')
    print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

    if botanico == 1:
        print(f'{Crs.ciano}Ok então, sem paisagens.{Crs.branco}')
        preco += 50

    elif botanico == 2:
        print(f'{Crs.ciano}Você não vai se arrepender.{Crs.branco}')
        preco += 75

    print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

#========================= 3 =========================#

if resposta == 3:
    print(f'{Crs.ciano}Temos 2 caminhos.{Crs.branco}')
    print(f'''{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.ciano}
Escolha:

[1] Mais rápido (Iremos direto ao ponto pela rodovia) R$50,00
[2] Mais Lento (Iremos passar por paisagens incríveis até o Cristo Redentor) R$75,00{Crs.branco}''')
    print('')

    cristo = int(input(''))
    print('')
    print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

    if cristo == 1:
        print(f'{Crs.ciano}Ok então, sem paisagens.{Crs.branco}')
        preco += 50

    elif cristo == 2:
        print(f'{Crs.ciano}Você não vai se arrepender.{Crs.branco}')
        preco += 75

    print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')

print(f'{Crs.verde}Você chegou ao seu destino, até a próxima!{Crs.branco}')
print(f'{Crs.verde}O valor da viagem foi de {preco}.{Crs.branco}')

print('')
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
