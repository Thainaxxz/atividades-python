#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
#o primeiro e o último nome separadamente.


nome = input('Digite seu nome completo: ')
div = nome.split()
print('O seu primeiro nome é: ', div[0])
print('O seu ultimo nome é: ', div[-1])