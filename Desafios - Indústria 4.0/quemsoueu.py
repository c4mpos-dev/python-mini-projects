'''     >>>>> QUEM SOU EU? <<<<<
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


print(f'''{Crs.ciano}=================================================={Crs.verde}
Oopa, seja bem-vindo(a).
Está no tédio? temos a solução!{Crs.ciano}
=================================================={Crs.branco}''')

print('')
sleep(1)

nome = input(f'{Crs.ciano}Já vou te contar ela, primeiro, digite seu nome:{Crs.branco} ')

print('')
print(f'{Crs.ciano}=================================================={Crs.verde}')

print('')

print(f'{Crs.verde}{nome}, vamos jogar "quem sou eu"!, prepare-se.{Crs.branco}')

print('')
print(f'{Crs.ciano}=================================================={Crs.verde}')
print('')

print(f'{Crs.verde}{nome}, o tema do jogo será sobre séries, temos duas.{Crs.branco}')

while True:

    serie = int(input(f'''{Crs.ciano}
Escolha:
[1] Cobra Kai
[2] The Flash
{Crs.branco} '''))

    print(f'{Crs.ciano}=================================================={Crs.verde}')
    print('')

    if serie == 1:
        print(f'{Crs.verde}Você escolheu Cobra Kai, agora tente adivinhar quem você é, com as dicas.{Crs.branco}')
        print(f'{Crs.verde}Lembre-se de colocar o nome com inicial maiúscula, acentos, etc.{Crs.branco}')
        print('')

#============================ 1 dica CK ============================#

        print(f'{Crs.ciano}=================================================={Crs.verde}')
        print(f'{Crs.verde}Dica 1:{Crs.verde}')
        print('')
        print(f'{Crs.verde}Você já foi um Cobra Kai.{Crs.branco}')
        print('')

        adv = input(f'{Crs.ciano}Responda ou aperte ENTER para próxima dica:{Crs.branco} ')
        print('')

        if adv == 'Falcão':
            print('')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print(f'{Crs.verde}Booa, você acertou!{Crs.branco}')
            print('')
            cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
            print('')

            if cont == 2:
                print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco} ')
                sys.exit()

        else:
            if adv == '':
                print(f'{Crs.verde}Ok, próxima dica:{Crs.branco}')

            else:
                print(f'{Crs.verde}Errou! próxima dica:{Crs.branco}')

#============================ 2 dica CK ============================#

        print('')
        print(f'{Crs.ciano}=================================================={Crs.verde}')
        print(f'{Crs.verde}Dica 2:{Crs.verde}')
        print('')
        print(f'{Crs.verde}Você já quebrou o braço do seu melhor amigo.{Crs.branco}')
        print('')

        adv = input(f'{Crs.ciano}Responda ou aperte ENTER para próxima dica:{Crs.branco} ')
        print('')

        if adv == 'Falcão':
            print('')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print(f'{Crs.verde}Booa, você acertou!{Crs.branco}')
            print('')
            cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
            print('')

            if cont == 2:
                print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                sys.exit()

        else:
            if adv == '':
                print(f'{Crs.verde}Ok, próxima dica:{Crs.branco}')

            else:
                print(f'{Crs.verde}Errou! próxima dica:{Crs.branco}')

#============================ 3 dica CK ============================#

        print('')
        print(f'{Crs.ciano}=================================================={Crs.verde}')
        print(f'{Crs.verde}Dica 3:{Crs.verde}')
        print('')
        print(f'{Crs.verde}Você era o garoto "nerd" e o mais maltratado da escola antes de entrar pro karatê.{Crs.branco}')
        print('')
        adv = input(f'{Crs.ciano}Acabou as dicas, responda ou aperte ENTER para ver a resposta:{Crs.branco} ')
        print('')

        if adv == 'Falcão':
            print('')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print(f'{Crs.verde}Booa, você acertou!{Crs.branco}')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print('')
            cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
            print('')

            if cont == 2:
                print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                sys.exit()

        else:
            if adv == '':
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                print(f'{Crs.verde}A resposta era: Falcão{Crs.branco}')
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                
                cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
                print('')
                print(f'{Crs.ciano}=================================================={Crs.verde}')

                if cont == 2:
                    print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                    sys.exit()
                    

                
            else:
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                print(f'{Crs.verde}Errou, a resposta era: Falcão{Crs.branco}')
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
                print('')

                if cont == 2:
                    print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                    sys.exit()

#============================ DIVISÃO DE SÉRIES ============================#

    elif serie == 2:
        
        print(f'{Crs.verde}Você escolheu The Flash, agora tente adivinhar quem você é, com as dicas.{Crs.branco}')
        print(f'{Crs.verde}Lembre-se de colocar o nome com inicial maiúscula, acentos, etc.{Crs.branco}')
        print('')

#============================ 1 dica TF ============================#
        print(f'{Crs.ciano}=================================================={Crs.verde}')
        print(f'{Crs.verde}Dica 1:{Crs.verde}')
        print('')
        print(f'{Crs.verde}Você faz parte da equipe The Flash.{Crs.branco}')
        print('')

        adv = input(f'{Crs.ciano}Responda ou aperte ENTER para próxima dica:{Crs.branco} ')
        print('')

        if adv == 'Caitlin':
            print('')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print(f'{Crs.verde}Booa, você acertou!{Crs.branco}')
            print('')
            cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
            print('')

            if cont == 2:
                print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco} ')
                sys.exit()

        else:
            if adv == '':
                print(f'{Crs.verde}Ok, próxima dica:{Crs.branco}')

            else:
                print(f'{Crs.verde}Errou! próxima dica:{Crs.branco}')

#============================ 2 dica TF ============================#
        print('')
        print(f'{Crs.ciano}=================================================={Crs.verde}')
        print(f'{Crs.verde}Dica 2:{Crs.verde}')
        print('')
        print(f'{Crs.verde}Você está com a equipe desde o início, e tem poderes..{Crs.branco}')
        print('')

        adv = input(f'{Crs.ciano}Responda ou aperte ENTER para próxima dica:{Crs.branco} ')
        print('')

        if adv == 'Caitlin':
            print('')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print(f'{Crs.verde}Booa, você acertou!{Crs.branco}')
            print('')
            cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
            print('')

            if cont == 2:
                print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                sys.exit()

        else:
            if adv == '':
                print(f'{Crs.verde}Ok, próxima dica:{Crs.branco}')

            else:
                print(f'{Crs.verde}Errou! próxima dica:{Crs.branco}')

#============================ 3 dica TF ============================#
        print('')
        print(f'{Crs.ciano}=================================================={Crs.verde}')
        print(f'{Crs.verde}Dica 3:{Crs.verde}')
        print('')
        print(f'{Crs.verde}Você é uma cientista incrível.{Crs.branco}')
        print('')
        adv = input(f'{Crs.ciano}Acabou as dicas, responda ou aperte ENTER para ver a resposta:{Crs.branco} ')
        print('')

        if adv == 'Caitlin':
            print('')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print(f'{Crs.verde}Booa, você acertou!{Crs.branco}')
            print(f'{Crs.ciano}=================================================={Crs.verde}')
            print('')
            cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
            print('')

            if cont == 2:
                print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                sys.exit()

        else:
            if adv == '':
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                print(f'{Crs.verde}A resposta era: Caitlin{Crs.branco}')
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                
                cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
                print('')
                print(f'{Crs.ciano}=================================================={Crs.verde}')

                if cont == 2:
                    print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                    sys.exit()
                    

                
            else:
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                print(f'{Crs.verde}Errou, a resposta era: Caitlin{Crs.branco}')
                print(f'{Crs.ciano}=================================================={Crs.verde}')
                cont = int(input(f'''{Crs.verde}
Quer continuar jogando?

[1] Sim {Crs.vermelho}
[2] Não
{Crs.branco} '''))
                print('')

                if cont == 2:
                    print(f'{Crs.verde}Obrigado por jogar {nome}, até a próxima!{Crs.branco}')
                    sys.exit()
    