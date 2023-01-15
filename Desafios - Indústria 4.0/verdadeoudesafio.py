'''     >>>>> VERDADE OU DESAFIO <<<<<
            >>>> Cauã Campos <<<<         '''

#========== Início do código ==========#

from time import sleep 
import sys
import random

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


#========== Lista dos jogadores, perguntas e desafios ==========#

desafios = ['Ligue para uma lanchonete ou pizzaria e tente desabafar com o atendente, dizendo que seu namorada (o) terminou contigo.', 'Ligue para sua mãe chorando dizendo que quer sua chupeta.', 'Ligue para o quinto contato no seu telefone e cante um trecho de uma música que o grupo escolher.', 'Invente um rap sobre sua situação amorosa atual.', 'Finja ser um gato e se esfregue em todas as pessoas do grupo.', 'Finja ser o animal de estimação da pessoa à sua esquerda.', 'Finja que você é um peixe se debatendo fora d’água.']
perguntas = ['Conte algo infantil que você ainda faz.', 'Qual é o seu medo mais sombrio?', 'Com que pessoa você se arrepende profundamente de já ter se envolvido?', 'Qual a coisa mais estranha ou vergonhosa que você já fez por dinheiro?', 'Se você pudesse mudar de vida com uma celebridade por um dia, quem seria?', 'Qual a maior mentira que você já contou para alguém da sua família?']
jogadores = []

print(f'{crs.Vermelho}Olá, pronto para jogar verdade ou desafio? lembrando que você tem que jogar em 3 pessoas.{crs.Branco}')
print(f'{crs.Vermelho}Os jogadores são escolhidos a cada rodada por um sistema randômico.{crs.Branco}')
print('')

jogador1 = input(f'{crs.Amarelo}Digite o nome do jogador 1:{crs.Branco} ')
jogador2 = input(f'{crs.Amarelo}Digite o nome do jogador 2:{crs.Branco} ')
jogador3 = input(f'{crs.Amarelo}Digite o nome do jogador 3:{crs.Branco} ')

jogadores.append(jogador1)
jogadores.append(jogador2)
jogadores.append(jogador3)

print('')
iniciar = input(f'{crs.Amarelo}Aperte ENTER para começar.{crs.Branco}')
print(f'{crs.Vermelho}3...{crs.Branco}')
sleep(1)
print(f'{crs.Vermelho}2..{crs.Branco}')
sleep(1)
print(f'{crs.Vermelho}1.{crs.Branco}')
sleep(1)

#========== O jogador escolhe entre verdade ou desafio ==========#

while True:

    print(f'''{crs.Vermelho}
[1] Verdade
[2] Desafio
[3] Sair do jogo
    {crs.Branco}''')

#========== Inicia o jogo ==========#   

    escolha = int(input(f'{crs.Amarelo}{random.choice(jogadores)}, verdade ou desafio?(coloque o número): '))
    print('')

    if escolha == 1:
        print(f'{crs.Vermelho}{random.choice(perguntas)}{crs.Branco}')
        resposta = input(f'{crs.Amarelo}Responda:{crs.Branco} ')

    elif escolha == 2:
        print(f'{crs.Vermelho}Agora que escolheu, vai ter que cumprir. (quando concluir aperte ENTER){crs.Branco}')
        desafio = input(f'{crs.Vermelho}{random.choice(desafios)}{crs.Branco}')

    else:
        print(f'{crs.Vermelho}Obrigado por jogar, até a próxima.{crs.Branco}')
        sys.exit()