# importando bibliotecas
from random import randint

# escolhendo o númeoro do computador
computador = randint(0, 10)

# interface
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinhar qual foi?')

# palpite do usuario
op = int(input('Qual é seu palpite? '))

# calculos
cont = 1
while op != computador:
    cont += 1
    if op < computador:
        print('Mais... tente mais uma vez.')
        op = int(input('Qual é seu palpite? '))
    if op > computador:
        print('Menos... tente mais uma vez.')
        op = int(input('Qual é seu palpite? '))

# resposta
print(f'\033[1;35mParabens! Você conseguiu, mas precisou de {cont} tentativas.')

