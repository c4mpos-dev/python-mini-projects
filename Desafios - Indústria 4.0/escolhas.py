'''     >>>>> DESAFIO DAS ESCOLHAS <<<<<
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

print(f'{Crs.ciano}Olá, você acaba de cair de paraquedas no nosso mundo.{Crs.branco}')
sleep(1)
print('')
nome = input(f'{Crs.ciano}Digite seu nome:{Crs.branco} ')
sleep(1)
print('')
print(f'{Crs.ciano}Muito bem!, {nome}, agora você escolhe o que fazer, boa sorte!{Crs.branco}')



while True:

    print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Ir para a floresta. 
[2] Ir para o riacho.
[3] Ir para aldeia mais próxima.
[4] Bater asas e ir para outro mundo.
{Crs.branco}''')

    esc = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
    sleep(2)
    print('')
    print(f'{Crs.azul}=============================================={Crs.branco}')
    print('')

    #============================= 1 ==============================#

    if esc == 1:
        print(f'{Crs.ciano}{nome}, você chegou na floresta.{Crs.branco}')

        while True:
            print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Procurar um abrigo.
[2] Procurar comida.
[3] Procurar água potável. 
[4] Sair da floresta.{Crs.branco}
        ''')

            floresta = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
            sleep(2)
            print('')
            print(f'{Crs.azul}=============================================={Crs.branco}')
            print('')

            if floresta == 1:
                print(f'{Crs.ciano}Você está procurando um abrigo...{Crs.branco}')
                sleep(3)
                print(f'{Crs.ciano}Woow, olha o tamanho dessa caverna que você achou, {nome}. já sabe onde dormir.{Crs.branco}')
            elif floresta == 2:
                print(f'{Crs.ciano}Você está procurando comida...{Crs.branco}')
                sleep(3)
                print(f'{Crs.ciano}{nome}, você encontrou uma macieira carregada. matou a fome.{Crs.branco}')
            elif floresta == 3:
                print(f'{Crs.ciano}Você está procurando água potável...{Crs.branco}')
                sleep(3)
                print(f'{Crs.ciano}Proonto, você encontrou uma mina. matou a sede.{Crs.branco}')
            elif floresta == 4:
                print(f'{Crs.ciano}Você saiu da floresta.{Crs.branco}')
                break

    #============================= 2 ==============================#
    
    if esc == 2:
        print(f'{Crs.ciano}Você chegou no riacho.{Crs.branco}')

        while True:
            print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Tomar banho.
[2] Nadar e relaxar.
[3] Pegar peixes. 
[4] Sair do riacho.{Crs.azul}{Crs.branco}
        ''')

            riacho = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
            sleep(2)
            print('')
            print(f'{Crs.azul}=============================================={Crs.branco}')
            print('')

            if riacho == 1:
                print(f'{Crs.ciano}{nome}, você tomou banho.{Crs.branco}')
            elif riacho == 2:
                print(f'{Crs.ciano}Você nadou e está relaxando...{Crs.branco}')
                sleep(2)
            elif riacho == 3:
                print(f'{Crs.ciano}Você achou um cardume e pegou todos os peixes, está com um estoque grande.{Crs.branco}')
            elif riacho == 4:
                print(f'{Crs.ciano}Você saiu do riacho.{Crs.branco}')
                break
    
    #============================= 3 ==============================#

    if esc == 3:
        print(f'{Crs.ciano}Você chegou na aldeia.{Crs.branco}')

        while True:
            print(f'''{Crs.azul}
=============================================={Crs.ciano}
[1] Conhecer a cultura do povo.
[2] Dar um passeio pela aldeia.
[3] Ajudar o povo com a agricultura.
[4] Sair da aldeia.{Crs.branco}
        ''')

            aldeia = int(input(f'{Crs.ciano}Selecione o que quer fazer:{Crs.branco} '))
            sleep(2)
            print('')
            print(f'{Crs.azul}=============================================={Crs.branco}')
            print('')

            if aldeia == 1:
                print(f'{Crs.ciano}Você conversou com todos e conhecou suas culturas.{Crs.branco}')
            elif aldeia == 2:
                print(f'{Crs.ciano}Você deu passeio pela a aldeia e descobriu paisagens incríveis.{Crs.branco}')
            elif aldeia == 3:
                print(f'{Crs.ciano}Você ajudou eles a cultivarem, e ganhou sementes de trigo, agora, {nome}, você pode pensar em fazer sua própria plantação.{Crs.branco}') 
            elif aldeia == 4:
                print(f'{Crs.ciano}Você saiu da aldeia.{Crs.branco}')
                break
    
    #============================= 4 ==============================#

    if esc == 4:
        print(f'{Crs.ciano}Você foi embora do nosso mundo.{Crs.branco}')
        sys.exit()    