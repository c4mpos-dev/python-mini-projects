'''     >>>> DESAFIO RPGG <<<<
          >> Cauã Campos <<      '''

from time import sleep 

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

print(f'{crs.CianoClaro}Seja bem-vindo(a) ao C4MP02 RPG, o seu mundo!{crs.Branco}')
print('')
nickname = input(f'{crs.Azul}Digite seu nickname:{crs.Branco} ')
print('')
print(f'{crs.CianoClaro}{nickname}, agora é a hora de escolher seu armamento.{crs.Branco}')
print(f'''{crs.CianoClaro}
[1] Espada
[2] Arco e flecha
[3] Canhão portátil
[4] Adagas
{crs.Branco}''')

armamento = int(input(f'{crs.Azul}Eae, vai pegar qual arma?{crs.Branco} '))

if armamento == 1:
    armamento = 'espada'

elif armamento == 2:
    armamento = 'arco e flecha'

elif armamento == 3:
    armamento = 'canhão portátil'

else:
    armamento = 'adagas'

print('')

print(f'{crs.CianoClaro}{nickname}, agora que já escolheu as armas, escolha o tipo do seu personagem.{crs.Branco} ')
print(f'''{crs.CianoClaro}
[1] Mago
[2] Humano
[3] Elfo
[4] Vampiro
{crs.Branco}''')

personagem = int(input(f'{crs.Azul}Eae, vai escolhar qual?{crs.Branco} '))

if personagem == 1:
    personagem = 'mago'

elif personagem == 2:
    personagem = 'humano'

elif personagem == 3:
    personagem = 'elfo'

else:
    personagem = 'vampiro'

print('')

print(f'{crs.CianoClaro}{nickname}, agora que já escolheu as armas e o personagem, escolha uma habilidade. {crs.Branco} ')
print(f'''{crs.CianoClaro}
[1] Velocidade
[2] Visão noturna
[3] Força
[4] Sabedoria
{crs.Branco}''')

habilidade = int(input(f'{crs.Azul}Eae, vai ficar com qual?{crs.Branco} '))

if habilidade == 1:
    habilidade = 'velocidade'

elif habilidade == 2:
    habilidade = 'visão noturna'

elif habilidade == 3:
    habilidade = 'força'

else:
    habilidade = 'sabedoria'

print('')

print(f'{crs.VermelhoClaro}Que beleeeza, {nickname}, você lutará com {armamento}, será um {personagem} e sua habilidade será a {habilidade}.{crs.Branco}')

print('')

print(f'''{crs.Verde}
Você está convidado para nossa festa de lançamento, será no final do ano, na BGS.{crs.Branco}''')