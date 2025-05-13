#declara variavel
import random
numero_secreto = random.randint (1,10) 
tentativas = 0
contagem_tentativas = 0
print ('BEM VINDO AO JOGO DO NUMERO SECRETO')
print (tente adivinhar o numero_secreto.')
#laco de repeticao
while tentativas != numero_secreto:
    numero = int(input)('digite um numero'))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print('!!!!parabeNS!!!!. voce adivinha o numero secreto!')
        print(f"voce precisou de {contagem_tentaivas}")
        break
    elif numero < numero_secreto:
     print(! 0 numero sereto e maioe.")
    else: 
     print ("0 numero secreot e nemor")