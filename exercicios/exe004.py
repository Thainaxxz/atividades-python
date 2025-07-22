#int() inteiro (7, -4, 0, 7458)
#float() flutuante/números reais (4.5, 0.076, -15.223, 0.7)
#bool() booleano/números lógicos (True, False)
#str() caracteres/strings ('Olá', '7,5, '')

#Recebe dois números e executa a soma de ambos

cores = {'vermelho':'\033[0;31m',
         'limpa':'\033[m'}

n1 = int (input('Digite um numero: '))
n2 = int (input('Digite um numero: '))
soma = n1 + n2
#print('A soma vale', soma)
#OU
print('A soma vale: {}{}{}'.format(cores['vermelho'] ,soma, cores['limpa']))


