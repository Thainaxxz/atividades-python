#Recebe o nome do usuário e retorna uma mensagem de boas vindas

cores = {'limpa':'\033[m',
         'azul':'\033[0;34m',
         'fundovermelho':'\033[0;0;41m'}

nome = input('Qual o seu nome? ')
print('Bem vindo(a), {}{}{}{}'.format(cores['azul'], cores['fundovermelho'], nome, cores['limpa']))