'''     >>>> DESAFIO IMC <<<<
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

print(f'{crs.MagentaClaro}Olá, seja bem-vindo(a).{crs.Branco}')
print(f'{crs.MagentaClaro}Vamos calcular seu IMC. responda as perguntas abaixo..{crs.Branco}')
print('')
print(f'''{crs.Verde}
[1] Sim{crs.Vermelho}
[2] Não
{crs.Branco}''')
atleta = int(input(f'{crs.Amarelo}Você é atleta?{crs.Branco} '))
print('')

if atleta == 1:
    print(f'{crs.MagentaClaro}Faremos o cálculo, mas por você ser atleta, ele não será preciso. {crs.Branco}')

print('')

altura = float(input(f'{crs.Amarelo}Qual a sua altura?{crs.Branco} '))

print('')

peso = float(input(f'{crs.Amarelo}Qual o seu peso?{crs.Branco} '))

print('')

alturaa = altura * altura
imc = peso / alturaa

if imc <= 18.5:
    print(f'{crs.MagentaClaro}Seu IMC é {imc}, você está abaixo do peso.{crs.Branco}')

elif imc >= 18.6 and imc <= 24.9:
    print(f'{crs.MagentaClaro}Seu IMC é {imc}, você está no peso ideal, parabéns!{crs.Branco}')

elif imc >= 25.0 and imc <=  29.9:
    print(f'{crs.MagentaClaro}Seu IMC é {imc}, você está levemente acima do peso.{crs.Branco}')
    
elif imc >= 30:
    print(f'{crs.MagentaClaro}Seu IMC é {imc}, você está obeso, vamos fazer uma dieta... sua saúde é muito importante.{crs.Branco}')