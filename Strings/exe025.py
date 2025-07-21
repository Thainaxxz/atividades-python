#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = input('Digite seu nome: ')
#valor = nome.find('SILVA')
valor = 'SILVA' in nome
if valor == 0:
    print('Sim, seu nome tem "SILVA"')
else:
    print('O nome digitado não tem "SILVA"')
