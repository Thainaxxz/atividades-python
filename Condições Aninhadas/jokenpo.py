#O Jokenpô é um jogo de dois jogadores, onde cada um faz um símbolo com a mão ao mesmo tempo. Cada símbolo tem um valor,
# e o objetivo é vencer o adversário de acordo com as seguintes regras: Pedra: Representada com o punho fechado.
# Papel: Representado com a mão aberta.

import random

cores = {
    'limpa': '\033[m',
    'preto': '\033[1;30m',
    'vermelho': '\033[1;31m',
    'verde': '\033[1;32m',
    'amarelo': '\033[1;33m',
    'azul': '\033[1;34m',
    'roxo': '\033[1;35m',
    'ciano': '\033[1;36m',
    'branco': '\033[1;37m',
    'cinza': '\033[0;37m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',
    'fundo_vermelho': '\033[1;41m',
    'fundo_verde': '\033[1;42m',
    'fundo_amarelo': '\033[1;43m',
    'fundo_azul': '\033[1;44m',
    'fundo_roxo': '\033[1;45m',
    'fundo_ciano': '\033[1;46m',
    'fundo_branco': '\033[1;47m'
}


print(f"{cores['vermelho']}******JOKENPO******{cores['limpa']}")
op = int(input(f"{cores['verde']}1 - SINGLE PLAYER\n{cores['limpa']}"
               f"{cores['verde']}2 - MULTIPLAYER\n{cores['limpa']}"))

if op == 1:
    op2 = int(input(f"{cores['vermelho']}******ESCOLHA******{cores['limpa']}\n"
                    f"{cores['verde']}1 - Pedra{cores['limpa']}\n"
                    f"{cores['verde']}2 - Papel{cores['limpa']}\n"
                    f"{cores['verde']}3 - Tesoura{cores['limpa']}\n"))
    bot = ['Pedra', 'Papel', 'Tesoura']
    sorteio = random.choice(bot)
    print('Joguei {}!'.format(sorteio))

    if (op2 == 1) and (sorteio == 'Tesoura'):
        print('Você ganhou!')
    elif (op2 == 1) and (sorteio == 'Papel'):
        print('Você perdeu!')
    elif (op2 == 1) and (sorteio == 'Pedra'):
        print('Empate!')
    elif (op2 == 2) and (sorteio == 'Tesoura'):
        print('Você perdeu!')
    elif (op2 == 2) and (sorteio == 'Papel'):
        print('Empate!')
    elif (op2 == 2) and (sorteio == 'Pedra'):
        print('Você ganhou!')
    elif (op2 == 3) and (sorteio == 'Tesoura'):
        print('Empate!')
    elif (op2 == 3) and (sorteio == 'Papel'):
        print('Você ganhou!')
    elif (op2 == 3) and (sorteio == 'Pedra'):
        print('Você perdeu!')
    else:
        print('Valor inválido!')





