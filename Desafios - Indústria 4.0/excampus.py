'''     >>>> DESAFIO EXCAMPUS <<<<
            >>>> Cauã Campos <<<<       '''

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

#========== Início do código ==========#

total = 0

print(f'{crs.CianoClaro}»»————-　★　————-««________»»————-　★　————-««{crs.Branco}')
print('')
print(f'{crs.CianoClaro}Seja bem-vindo(a) à C4MP02 STORE, aqui temos:{crs.Branco}')
print(f'{crs.CianoClaro}• As melhores marcas e modelos de tênis.{crs.Branco}')
print('')
print(f'{crs.CianoClaro}»»————-　★　————-««________»»————-　★　————-««{crs.Branco}')

print('')

print(f'{crs.MagentaClaro}Vamos as compras. Verificando estoque...{crs.Branco}')
sleep(3)

while True:

    print(f'''{crs.MagentaClaro}
    [1] Nike
    [2] Adidas
    [3] Asics{crs.Branco}''')

    print('')

    escolha = int(input(f'{crs.MagentaClaro}Qual você curte mais?{crs.Branco} '))

    print('')
    
    if escolha == 1:  
        print(f'''
        [1] Nike Air{crs.Verde}R$129,90{crs.Branco}
        [2] Nike Lunar{crs.Verde}R$199,90{crs.Branco}
        [3] Nike Free{crs.Verde}R$99,90{crs.Branco}''')

        print('')

        esc_modelo = int(input(f'Qual modelo quer comprar? '))

        print('')

        if esc_modelo == 1:
            print('Nike Air adicionado ao carrinho.') 
            total += 129.90

        elif esc_modelo == 2:
            print('Nike Lunar adicionado ao carrinho.')
            total += 199.90

        else:
            print('Nike Free adicionado ao carrinho.')
            total += 99.90

        print(f'''
        {crs.Amarelo}1 - Sim{crs.Branco}
        {crs.Amarelo}2 - Não{crs.Branco}''')

        print('')

        continuar = int(input('Quer continuar comprando? '))   

        if continuar == 2:
            print(f'{crs.Ciano}O preço final da sua compra foi: {total}. Obrigado pela preferência, até a próxima!{crs.Branco}')
            break

    elif escolha == 2:  
        print(f'''
        [1] Adidas UltraBoost{crs.Verde}R$159,90{crs.Branco}
        [2] Adidas FortaRun{crs.Verde}R$119,90{crs.Branco}
        [3] Adidas PrimeKnit{crs.Verde}R$99,90{crs.Branco}''')

        print('')

        esc_modelo = int(input(f'Qual modelo quer comprar? '))

        print('')

        if esc_modelo == 1:
            print('Adidas UltraBoost adicionado ao carrinho.') 
            total += 159.90

        elif esc_modelo == 2:
            print('Adidas FortaRun adicionado ao carrinho.')
            total += 119.90

        else:
            print('PrimeKnit adicionado ao carrinho.')
            total += 99.90

        print(f'''
        {crs.Amarelo}1 - Sim{crs.Branco}
        {crs.Amarelo}2 - Não{crs.Branco}''')

        print('')

        continuar = int(input('Quer continuar comprando? '))   

        if continuar == 2:
            print(f'{crs.Ciano}O preço final da sua compra foi: {total}. Obrigado pela preferência, até a próxima!{crs.Branco}')
            break

    else:
        print(f'''
        [1] Asics Gel Quantum{crs.Verde}R$159,90{crs.Branco}
        [2] Asics Gel Rocket{crs.Verde}R$129,90{crs.Branco}
        [3] Asics Gel Kayano{crs.Verde}R$99,90{crs.Branco}''')

        print('')

        esc_modelo = int(input(f'Qual modelo quer comprar? '))

        print('')

        if esc_modelo == 1:
            print('Asics Gel Quantum adicionado ao carrinho.') 
            total += 159.90

        elif esc_modelo == 2:
            print('Asics Gel Rocket adicionado ao carrinho.')
            total += 129,90

        else:
            print('Asics Gel Kayano adicionado ao carrinho.')
            total += 99.90

        print(f'''
        {crs.Amarelo}1 - Sim{crs.Branco}
        {crs.Amarelo}2 - Não{crs.Branco}''')

        print('')

        continuar = int(input('Quer continuar comprando? '))   

        if continuar == 2:
            print(f'{crs.Ciano}O preço final da sua compra foi: {total}. Obrigado pela preferência, até a próxima!{crs.Branco}')
            break