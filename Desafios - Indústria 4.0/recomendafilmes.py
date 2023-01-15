'''     >>>> DESAFIO RECOMENDA FILMES <<<<
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

#========== Início do código ==========#


#========== Listas com os filmes de cada categoria ==========#

acao = ['Bad Boys', 'Resgate', 'Vingadores', 'Legado Explosivo', 'Pantera Negra', 'A Caçada']
aventura = ['O Rei Leão', 'Venom', 'Logan', 'Kong', 'Godzilla', 'Jurassic World']
terror = ['Medo Profundo', 'A Ilha da Fantasia', 'O Homem Invisível', 'It: A Coisa', 'O Chalé', 'O Grito']
comedia = ['Férias Frustadas', 'Minha Mãe é Uma Peça (1, 2 e 3)', 'Gente Grande (1 e 2)', 'Se Beber, Não Case!', 'Até Que a Sorte Nos Separe (1, 2 e 3)']

#========== Mensagem de boas-vindas e apresentação do "site" ==========# 

print(f'{crs.Ciano}»»————-　★　————-««________»»————-　★　————-««{crs.Branco}')

print(f'''{crs.Verde}
Seja bem-vindo(a) à C4MP02 RECOMENDAÇÕES, aqui temos:
• Recomendações de filmes de diferentes categorias.
{crs.Branco}''')

print(f'{crs.Ciano}»»————-　★　————-««________»»————-　★　————-««{crs.Branco}')

#========== Começo do site e perguntas para o cliente ==========#

while True:

    print('')
    print(f'''{crs.Verde}
    [1] Ação
    [2] Aventura
    [3] Terror
    [4] Comédia
    {crs.Branco}''')
    print('')
    categoria = int(input(f'{crs.Ciano}Escolha um tipo de filme:{crs.Branco} '))
    print('')

#========== Caso o cliente escolha 1, recomenda a lista de ação ==========#

    if categoria == 1:
        print(f'{crs.Verde}Para filmes de ação, recomendamos esses:{crs.Branco}')
        print(f'{crs.Magenta} \n - {acao[0]} \n - {acao[1]} \n - {acao[2]} \n - {acao[3]} \n - {acao[4]} \n - {acao[5]} {crs.Branco}')
        print('')

        print(f'''{crs.Verde}
        [1] Sim{crs.Vermelho}
        [2] Não
        {crs.Branco}''')
        print('')

        continuar = int(input(f'{crs.Ciano}Quer continuar vendo as recomendações?{crs.Branco} '))

        if continuar == 2:
            print(f'{crs.Verde} \n Obrigado por acessar nosso site! \n Esperamos que goste das recomedações, até a próxima!{crs.Branco}')
            sys.exit()

#========== Caso o cliente escolha 2, recomenda a lista de aventura ==========#

    elif categoria == 2:

        print(f'{crs.Verde}Para filmes de aventura, recomendamos esses:{crs.Branco}')
        print(f'{crs.Magenta} \n - {aventura[0]} \n - {aventura[1]} \n - {aventura[2]} \n - {aventura[3]} \n - {aventura[4]} \n - {aventura[5]} {crs.Branco}')
        print('')

        print(f'''{crs.Verde}
        [1] Sim{crs.Vermelho}
        [2] Não
        {crs.Branco}''')
        print('')

        continuar = int(input(f'{crs.Ciano}Quer continuar vendo as recomendações?{crs.Branco} '))

        if continuar == 2:
            print(f'{crs.Verde} \n Obrigado por acessar nosso site! \n Esperamos que goste das recomedações, até a próxima!{crs.Branco}')
            sys.exit()

#========== Caso o cliente escolha 3, recomenda a lista de terror ==========#

    elif categoria == 3:

        print(f'{crs.Verde}Para filmes de terror, recomendamos esses:{crs.Branco}')
        print(f'{crs.Magenta} \n - {terror[0]} \n - {terror[1]} \n - {terror[2]} \n - {terror[3]} \n - {terror[4]} \n - {terror[5]} {crs.Branco}')
        print('')

        print(f'''{crs.Verde}
        [1] Sim{crs.Vermelho}
        [2] Não
        {crs.Branco}''')
        print('')

        continuar = int(input(f'{crs.Ciano}Quer continuar vendo as recomendações?{crs.Branco} '))

        if continuar == 2:
            print(f'{crs.Verde} \n Obrigado por acessar nosso site! \n Esperamos que goste das recomedações, até a próxima!{crs.Branco}')
            sys.exit()

#========== Caso o cliente escolha 4, recomenda a lista de comédia ==========#

    else:

        print(f'{crs.Verde}Para filmes de comédia, recomendamos esses:{crs.Branco}')
        print(f'{crs.Magenta} \n - {comedia[0]} \n - {comedia[1]} \n - {comedia[2]} \n - {comedia[3]} \n - {comedia[4]} {crs.Branco}')
        print('')

        print(f'''{crs.Verde}
        [1] Sim{crs.Vermelho}
        [2] Não
        {crs.Branco}''')
        print('')

        continuar = int(input(f'{crs.Ciano}Quer continuar vendo as recomendações?{crs.Branco} '))

        if continuar == 2:
            print(f'{crs.Verde} \n Obrigado por acessar nosso site! \n Esperamos que goste das recomedações, até a próxima!{crs.Branco}')
            sys.exit()