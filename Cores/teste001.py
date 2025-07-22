#print('\033[4;30;43mOlá mundo\033[m')
nome = 'Thaina'
cores = {'limpa':'\033[m',
         'azul':'\033[94m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito prazer em te conhecer {}{}{}!!'.format(cores['pretoebranco'],nome, cores['limpa']))