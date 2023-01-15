'''     >>>> DESAFIO DOS ESTUDIOSOS <<<<
            >>>> Cauã e Jéssica <<<<          '''

from time import sleep 

class cores:

    Branco = '\033[0m'	
    Vermelho = '\033[1;31m'
    Verde =	'\033[1;32m'

##### Início do código #####

nome = str(input('Olá, seja bem-vindo ao quiz, qual seu nome? '))
sleep(1)

while True:
    print('»»————-　★　————-««')
    print('1 - Física')
    print('2 - Matemática')
    print('3 - Geografia')
    print('4 - Biologia')
    print('»»————-　★　————-««')

    materia = int(input(f'{nome}, escolha uma matéria para realizar o quiz(Coloque o número): '))

    print('Formulando as perguntas...')
    sleep(3)
    print('')

    if materia == 1:
        print('Uma locomotiva afasta-se de um observador enquanto sua velocidade aumenta a cada segundo. O movimento descrito por essa locomotiva pode ser classificado como:')
        print('»»————-　★　————-««')
        print('a) progressivo e retardado.')
        print('b) regressivo e retardado.')
        print('c) progressivo e retilíneo.')
        print('d) regressivo e acelerado.')
        print('e) progressivo e acelerado.')
        print('»»————-　★　————-««')
        sleep(5)
        resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
        print('')
        if resposta == 'e':
            print(f'{cores.Verde}Parabéns, você acertou!{cores.Branco}')      
        else: 
            print(f'{cores.Vermelho}Você errou! tá precisando dar uma estudada em física... haha!{cores.Branco}') 
    elif materia == 2:
        print('Qual a fração geratriz da dízima 0,444...?')
        print('»»————-　★　————-««')
        print('a) 4/9.')
        print('b) 4/99.')
        print('c) 4/999.')
        print('d) 12/3.')
        print('e) 12/33.')
        print('»»————-　★　————-««')
        sleep(5)
        resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
        print('')
        if resposta == 'a':
            print(f'{cores.Verde}Parabéns, você acertou!{cores.Branco}')      
        else: 
            print(f'{cores.Vermelho}Você errou! tá precisando dar uma estudada em matemática... haha!{cores.Branco}')
    elif materia == 3:
        print('A linha imaginária considerada o marco 0° dos fusos horários é: ')
        print('»»————-　★　————-««')
        print('a) Linha do Equador.')
        print('b) Trópico de Capricórnio.')
        print('c) Meridiano de Greenwich.')
        print('d) Trópico de Câncer.')
        print('»»————-　★　————-««')
        sleep(5)
        resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
        print('')
        if resposta == 'c':
            print(f'{cores.Verde}Parabéns, você acertou!{cores.Branco}')      
        else: 
            print(f'{cores.Vermelho}Você errou! tá precisando dar uma estudada em geografia... haha!{cores.Branco}')
    else:
        print('Os carboidratos podem ser divididos em quantos grupos? Quais? ')
        print('»»————-　★　————-««»»————-　★　————-««»»————-　★　————-««')
        print('a) 2, monossacarídeos e dissacarídeos.')
        print('b) 2, monossacarídeos e polissacarídeos.')
        print('c) 3, monossacarídeos, dissacarídeos e frutose.')
        print('d) 3, monossacarídeos, dissacarídeos e polissacarídeos.')
        print('»»————-　★　————-««»»————-　★　————-««»»————-　★　————-««')
        sleep(5)
        resposta = str(input('(Utilize letras minúsculas) Eae, qual letra é a certa? '))
        print('')
        if resposta == 'd':
            print(f'{cores.Verde}Parabéns, você acertou!{cores.Branco}')      
        else: 
            print(f'{cores.Vermelho}Você errou! tá precisando dar uma estudada em biologia... haha!{cores.Branco}')
    
    print('')
    print(f'''{cores.Verde}
    1 - Sim{cores.Vermelho}
    2 - Não{cores.Branco}''')
    print('')
    escolha = int(input('Vamos continuar? '))
    print('')

    if escolha == 2:
        print(f'Muito obrigado por realizar nosso quiz, {nome}, até mais!')
        break
        
    print(f'Caso você tenha{cores.Verde} acertado{cores.Branco}, escolha outra matéria.')
    sleep(2)