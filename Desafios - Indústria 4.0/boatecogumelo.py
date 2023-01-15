'''     >>>> DESAFIO BOATE COGUMELO <<<<
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

senha = '1745'

print(f'{crs.Ciano}»»————-　★　————-««________»»————-　★　————-««{crs.Branco}')
print('')
print(f'{crs.Azul}Seja bem-vindo(a) à BOATE C4MP0$, divirta-se!{crs.Branco}')
print('')
print(f'{crs.Ciano}»»————-　★　————-««________»»————-　★　————-««{crs.Branco}')
print('')

print(f'{crs.Azul}Ôôô, achou que ia ser fácil assim?{crs.Branco}')
print('')

idade = int(input(f'{crs.Ciano}Qual sua idade?{crs.Branco} '))
print('')

if idade >= 18:
    print(f'{crs.Azul}Hmm, deixa eu ver sua identidade... ok, tá liberado.{crs.Branco}')
else:
    print(f'{crs.Azul}Infelizmente você não poderá entrar, não é permitida entrada de menores. {crs.Branco}')
    print(f'{crs.Azul}Só é permitido se você tiver a senha secreta, que o dono da boate lhe passou.{crs.Branco}')
    print(f'''{crs.Azul}
    [1] Sim{crs.Vermelho}
    [2] Não
    {crs.Branco}''')
    acesso = int(input(f'{crs.Ciano}Você tem a senha?{crs.Branco} '))
    print('')

    if acesso == 1:
        ctz = str(input(f'{crs.Ciano}Digite a senha:{crs.Branco} '))
        if ctz == senha:
            print('')
            print(f'{crs.Azul}Sucesso! pode entrar!{crs.Branco}')
        else:
            print('')
            print(f'{crs.Vermelho}Acesso negado! senha incorreta.{crs.Branco}')
            sys.exit()
    else:
        print(f'{crs.Vermelho}Acesso negado! você não pode entrar.{crs.Branco}')
        sys.exit()

print('')

print(f'{crs.Azul}Agora vá se divertir!{crs.Branco} ')

while True:

    print(f'''{crs.Azul}
    [1] Dançar
    [2] Beber/comer
    [3] Sair da boate
    {crs.Branco}''')

    opcoes = int(input(f'{crs.Ciano}Escolha o que quer fazer:{crs.Branco} '))

    if opcoes == 1:
        print(f'{crs.Azul}Ooooopa, vai lá, aproveita que a música é boa.{crs.Branco}')

    elif opcoes == 2:
        print(f'{crs.Azul}Essa aqui é a melhor que temos, experimente.{crs.Branco}')
        print('''
                
        ░░░░░▓███▓
        ░░░░▓█████▓
        ░░░░▓█████▓
        ░░░░░▓███▓ 
        ░░░░░█████
        ░░░░░█████
        ░░░░░█████
        ░░░░░█████
        ░░░░▓█████▓
        ░░░░▓█████▓
        ░░░░▓█████▓
        ░░░▓███████▓
        ░░▓█████████▓
        ░▓███████████▓
        ▓█████████████▓
        ▓███░░░░░░░▀▀▀▓
        ▓███░░░░████████████
        ▓███░░░░█▒▒▒▒▒▒▒▒▒▒█
        ▓███░░░░░█▒▒▒▒▒▒▒▒█
        ▓███░░░░░░█▒▒▒▒▒▒█
        ▓███░░░░░░░█▒▒▒▒█
        ▓███░░░░░░░░████
        ▓███░░░░░░░░▌██▌
        ▓███░░░░░░░░▌██▌
        ▓███░░░░░░░░▌██▌
        ▓███░░░░░░░░▌██▌
        ░▓██░░░░░░░▓████▓
        ░▓████▓▓█████████▓
        ''')
        

    else:
        print(f'{crs.Vermelho}Mas já vai? até a próxima!{crs.Branco}')
        break