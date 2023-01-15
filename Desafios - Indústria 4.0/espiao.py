'''     >>>>> DESAFIO ESPIÃO <<<<<
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

certas = 0

print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print(f'{Crs.ciano}Opa, seja bem-vindo(a).{Crs.branco}')
print(f'{Crs.ciano}Aqui testaremos suas habilidades sobre Guerra Fria.{Crs.branco}')
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')

print(f'''{Crs.ciano}Qual dos acontecimentos seguintes não teve relação com a Guerra Fria:

a) Guerra Civil Espanhola
b) Guerra da Coreia
c) Revolução Cubana
d) Ditaduras latino-americanas
e) Guerra do Afeganistão
{Crs.branco}''')
        
resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
print('')

if resposta == 'a':
    print(f'{Crs.verde}Parabéns, você acertou!{Crs.branco}')  
    certas += 1

else: 
    print(f'{Crs.vermelho}Você errou!{Crs.branco}') 

print('')
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')

print(f'''{Crs.ciano}A Perestroika e a Glasnot foram propostas de reforma que levaram a União Soviética a sua dissolução. Quem foi o presidente responsável por essas reformas:

a) Boris Ieltsin
b) Yuri Andropov
c) Leonid Brejnev
d) Nikita Kruschev
e) Mikhail Gorbachev
{Crs.branco}''')
        
resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
print('')

if resposta == 'e':
    print(f'{Crs.verde}Parabéns, você acertou!{Crs.branco}')
    certas += 1  

else: 
    print(f'{Crs.vermelho}Você errou!{Crs.branco}') 

print('')
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')

print(f'''{Crs.ciano}O Plano Marshall foi uma das ações do governo norte-americano motivadas pela rivalidade na Guerra Fria. Esse plano propunha:

a) o financiamento da reconstrução de países europeus destruídos pela Segunda Guerra.
b) a realização de golpes militares no sul da Europa.
c) o envio de espiões para executar as lideranças de esquerda na Europa Ocidental.
d) a imposição de embargos para os países da Europa Ocidental que não aderiram à Otan.
e) nenhuma das alternativas anteriores.
{Crs.branco}''')
        
resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
print('')

if resposta == 'a':
    print(f'{Crs.verde}Parabéns, você acertou!{Crs.branco}') 
    certas += 1 

else: 
    print(f'{Crs.vermelho}Você errou!{Crs.branco}') 

print('')
print(f'{Crs.verde}▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃{Crs.branco}')
print('')
print(f'{Crs.ciano}Obrigado por participar, você acertou {certas} pergunta(as).{Crs.branco}')


