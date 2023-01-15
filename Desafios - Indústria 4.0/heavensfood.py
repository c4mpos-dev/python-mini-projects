'''     >>>>> Heaven’s Food <<<<<
            >> Cauã Campos <<         '''

#========== Início do código ==========#

from time import sleep 
import sys

class Crs:

    reset = '\033[0;0m'
    negrito =  '\033[;1m'
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


#========== Listas ==========#

secret = []

#============================#

print(f'{Crs.amarelo}============================================================================================={Crs.branco}')

print(f'''{Crs.vermelho}
Você vai com seus amigos para a inauguração do Restaurante C4MP0$, vai de estômago vazio que tem muita coisa boa.
O micro-ônibus dos seus amigos passa daqui a pouco para te pegar, se arrume.{Crs.branco}''')
print('')
print(f'{Crs.amarelo}============================================================================================={Crs.branco}')

sleep(7)

print(f'''
___$$$$$$$$$$$$$$$$$$$$$$$$$$
_$$$$$$______$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$______$$$$$$$$$$$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
________$$$$$$$$$$_____$$$$$________$$$$
_______$$____$$$$$_____$$$$$________$$$$
______$______$$$$$_____$$$$$________$$$$
____$$$$$$$$$$$$$$_____$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$_____$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$_____$$$$$$$$$$$$$$$$$
$$$$$_$$$$_$$$$$$$$$$$$$$$$_$$$$_$$$$$$$
_$$$_$$$$$$_$$$$$$$$$$$$$$_$$$$$$_$$$$
______$$$$__________________$$$$  
''')

print(f'{Crs.vermelho}Olha ele aíí, booora!{Crs.branco}')

sleep(3)

print(f'{Crs.amarelo}============================================================================================={Crs.branco}')
print('')
print(f'{Crs.vermelho}Você chegou ao restaurante, está você e seus amigos na maior mesa do local.{Crs.branco}')
print('')
print(f'{Crs.amarelo}============================================================================================={Crs.branco}')
sleep(2)
print(f'{Crs.negrito}NA INAUGURAÇÃO É TUDO POR CONTA DA CASA, APROVEITE!!!{Crs.reset}')
print(f'{Crs.amarelo}============================================================================================={Crs.branco}')
print('')
sleep(1)
print(f'{Crs.vermelho}O cardápio chegou, escolha o tipo do prato principal:{Crs.branco}')

#========== Tipo da comida ==========#

princ = int(input(f'''{Crs.ciano}
[1] Massas
[2] Frangos e Peixes
[3] Bifes
[4] Não quero o prato principal
{Crs.branco} '''))

print('')

#========== MASSAS ==========#

if princ == 1:
    print(f'{Crs.amarelo}=================================================={Crs.branco}')
    print('')
    print(f'{Crs.vermelho}Massas, hmm, temos esses pratos:{Crs.branco}')
    print(f'''{Crs.ciano}
[1] Parmegiana - (Arroz, farofa, fritas, alface e cenoura)
[2] Lasanha Q&P - (Arroz, fritas e queijo parmesão)
[3] Espaguete à bolonhesa- (Espaguete, molho à bolonhesa e queijo parmesão)
{Crs.branco}''')

    massas = int(input(f'{Crs.vermelho}Escolha um:{Crs.branco} '))
    print('')

    if massas == 1:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Parmegiana - (Arroz, farofa, fritas, alface e cenoura)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

    elif massas == 2:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Lasanha Q&P - (Arroz, fritas e queijo parmesão)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

    elif massas == 3:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Espaguete à bolonhesa- (Espaguete, molho à bolonhesa e queijo parmesão)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)
    
#========== FRANGOS E PEIXES ==========#

elif princ == 2:
    print(f'{Crs.amarelo}=================================================={Crs.branco}')
    print('')
    print(f'{Crs.vermelho}Temos esses pratos de frangos e peixes:{Crs.branco}')
    print(f'''{Crs.ciano}
[1] Frango Jumbo - (Pedaços crocantes de peito de frango empanado)
[2] Peixe empanado - (Para celebrar nossas raízes britânicas, cortes de filet de peixe empanados à mão)
[3] Filé de tilápia - (Filé de tilápia com leveza e suculência)
{Crs.branco}''')

    fep = int(input(f'{Crs.vermelho}Escolha um:{Crs.branco} '))
    print('')

    if fep == 1:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Frango Jumbo - (Pedaços crocantes de peito de frango empanado)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

    elif fep == 2:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Peixe empanado - (Para celebrar nossas raízes britânicas, cortes de filet de peixe empanados à mão)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

    elif fep == 3:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Filé de tilápia - (Filé de tilápia com leveza e suculência)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

#========== BIFES ==========#

elif princ == 3:
    print(f'{Crs.amarelo}=================================================={Crs.branco}')
    print('')
    print(f'{Crs.vermelho}Bife, muito bom né? temos esses pratos:{Crs.branco}')
    print(f'''{Crs.ciano}
[1] Filé Mignon - (Filé mignon em tiras e empanado. Crocante por fora e macio por dentro)
[2] T-Steak - (Cerca de 500g de um corte nobre e macio em formato de T)
[3] New-Steak - (375g do corte nobre do contra-filet, perfeitamente temperado e preparado na chapa.)
{Crs.branco}''')

    bife = int(input(f'{Crs.vermelho}Escolha um:{Crs.branco} '))
    print('')

    if bife == 1:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('Filé Mignon - (Filé mignon em tiras e empanado. Crocante por fora e macio por dentro)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

    elif bife == 2:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('T-Steak - (Cerca de 500g de um corte nobre e macio em formato de T)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

    elif bife == 3:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        sleep(1)
        secret.append('New-Steak - (375g do corte nobre do contra-filet, perfeitamente temperado e preparado na chapa.)')
        print(f'{Crs.vermelho}Vamos para as bebidas.{Crs.branco}')
        sleep(1)

elif princ == 4:
    print(f'{Crs.amarelo}=================================================={Crs.branco}')

#========== BEBIDAS ==========#

print('')

bebida = int(input(f'''{Crs.vermelho}
Escolha sua bebida:{Crs.ciano}

[1] Água sem gás
[2] Água com gás
[3] Coca Cola (Lata 350ml)
[4] Coca Cola (Garrafa 600ml)
[5] Coca Cola (Garrafa 2l)
[6] Guaraviton (Giseng)
[7] Ativ Plus (Guaraná)
[8] Suco de Laranja (Dell Vale)
[9] Suco de Uva (Dell Vale)
[10] Suco de Maracujá (Dell Vale)
[11] Não quero bebida
{Crs.branco} '''))
print('')
print(f'{Crs.amarelo}=================================================={Crs.branco}')

print('')

if bebida == 1:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Água sem gás')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 2:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Água com gás')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 3:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Coca Cola (Lata 350ml)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 4:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Coca Cola (Garrafa 600ml)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 5:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Coca Cola (Garrafa 2l)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 6:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Guaraviton (Giseng)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 7:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Ativ Plus (Guaraná)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')    
    
elif bebida == 8:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Suco de Laranja (Dell Vale)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 9:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Suco de Uva (Dell Vale)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')

elif bebida == 10:
    print(f'{Crs.vermelho}Anotado!{Crs.branco}')
    secret.append('Suco de Maracujá (Dell Vale)')
    print(f'{Crs.vermelho}Vamos para a sobremesa.{Crs.branco}')       


#========== SOBREMESAS ==========#

print('')

sobremesa = int(input(f'''{Crs.vermelho}
Escolha sua sobremesa:{Crs.ciano}

[1] Pudim
[2] Milkshake (Chocolate 400ml)
[3] Milkshake (Morango 400ml)
[4] Sorvete Sundae (Chocolate)
[5] Sorvete Sundae (Morango)
[6] Pular sobremesa
[7] Não quero sobremesa
{Crs.branco} '''))
print(f'{Crs.amarelo}=================================================={Crs.branco}')

print('')

if sobremesa == 1:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        secret.append('Pudim')
        print(f'{Crs.vermelho}Agora é só esperar chegar...{Crs.branco}')

elif sobremesa == 2:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        secret.append('Milkshake (Chocolate 400ml)')
        print(f'{Crs.vermelho}Agora é só esperar chegar...{Crs.branco}')

elif sobremesa == 3:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        secret.append('Milkshake (Morango 400ml)')
        print(f'{Crs.vermelho}Agora é só esperar chegar...{Crs.branco}')

elif sobremesa == 4:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        secret.append('Sorvete Sundae (Chocolate)')
        print(f'{Crs.vermelho}Agora é só esperar chegar...{Crs.branco}')

elif sobremesa == 5:
        print(f'{Crs.vermelho}Anotado!{Crs.branco}')
        secret.append('Sorvete Sundae (Morango)')
        print(f'{Crs.vermelho}Agora é só esperar chegar...{Crs.branco}')

print('')

print(f'{Crs.amarelo}=================================================={Crs.branco}')

if (princ == 4) and (bebida == 11) and (sobremesa == 7):
    print(f'{Crs.vermelho}Então você veio só pra olhar? ok... até a próxima.{Crs.branco}')
    print(f'{Crs.amarelo}=================================================={Crs.branco}')
    sys.exit()
    
print('')
sleep(3)
print(f'{Crs.vermelho}Achou que ia demorar? aqui não! tá na mão...{Crs.branco}')
print(f'{Crs.ciano}Seu pedido:{Crs.branco}')
sleep(1)
print(f'{Crs.ciano}{[secret]}{Crs.branco}')
print('')
sleep(1)
print(f'{Crs.amarelo}=================================================={Crs.branco}')
sleep(1)
print(f'{Crs.vermelho}Deixe seu feedback depois... bom apetite!{Crs.branco}')
sleep(1)
print(f'{Crs.amarelo}=================================================={Crs.branco}')

feedback = input(f'{Crs.vermelho}Eae, o que achou do restaurante?{Crs.branco} ')
print(f'{Crs.vermelho}Obrigado pelo feedback, esperamos lhe ver mais vezes, até!{Crs.branco}')
sys.exit()