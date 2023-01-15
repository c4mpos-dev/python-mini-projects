'''     >>>> DESAFIO PEAKY BLINDERS <<<<
              >>>> Cauã Campos <<<<         '''

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



#========== Listas do cadastrados (começa vazia) ==========#

cadastrados = []

#========== Boas-vindas ao usuário e o começa do login/cadastro ==========#

print(f'{Crs.amarelo}»»————-　★　————-««________»»————-　★　————-««{Crs.branco}')
print('')
print(f'{Crs.vermelho}Seja bem-vindo(a) à C4MP0$ GAMES. {Crs.branco}')
print(f'{Crs.vermelho}• A melhor comunidade gamer do Brasil.{Crs.branco}')
print('')
print(f'{Crs.amarelo}»»————-　★　————-««________»»————-　★　————-««{Crs.branco}')

print('')

print(f'{Crs.vermelho}Antes de ingressar nessa comunidade maravilhosa, temos que saber quem é você.{Crs.branco}')

print('')

while True:

    print(f'{Crs.amarelo}»»————-　★　————-««________»»————-　★　————-««{Crs.branco}')
    print(f'''{Crs.vermelho}
    [1] Sim
    [2] Não
    {Crs.branco}''')
    simnao = int(input(f'{Crs.amarelo}Já possui cadastro?{Crs.branco} '))
    print('')

    if simnao == 1:
        login = input(f'{Crs.amarelo}Digite seu nome senha(no modelo como cadastrou):{Crs.branco} ')

        if login in cadastrados:
            print('')

            print(f'{Crs.vermelho}Login realizado com sucesso.{Crs.branco}')

            print(f'''{Crs.amarelo}
            Mensagens: {Crs.vermelho}
            João: Eae mano, qual vamos jogar aquele COD?
            Marcos: Falaee, descobri como passar aquela fase...
            Miguel: Comprei a game pass, agora é só gameplay, gogo.
            {Crs.branco}''')
            sleep(5)
            continuar = input(f'{Crs.vermelho}Aperte ENTER para entrar com outra conta.{Crs.branco}')

        else:
            print('')
            print(f'{Crs.vermelho}Erro no login.{Crs.branco}')
            sys.exit()

    else:
        print(f'{Crs.vermelho}Então vamos fazer agora.{Crs.branco}')

        cadastro = input(f'{Crs.amarelo}Digite seu nome e a senha na frente (ex: Cauã 1254):{Crs.branco} ')
        cadastrados.append(cadastro)
        print('')
        print(f'{Crs.vermelho}Cadastro realizado.{Crs.branco}')

        continuar = input(f'{Crs.vermelho}Aperte ENTER para fazer login ou entrar com outra conta.{Crs.branco}')