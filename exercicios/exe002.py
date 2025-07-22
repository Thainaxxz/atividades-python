#Recebe o nome do usuário e retorna uma mensagem de saudação

cores = {'limpa':'\033[m',
        'laranja':'\033[0;33m'}

nome = input('Digite seu nome ')
print('Prazer! {}{}{}'. format(cores ['laranja'],nome, cores['limpa']))