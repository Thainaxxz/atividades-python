#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "santo".

print('-------- O NOME DA CIDADE COMEÇA COM "Santo"? ---------')
cidade = input("Digite o nome da cidade: ")
valor = cidade.find('Santo')

if valor == 0:
    print('O nome da cidade digitado acima começa com "Santo"')
else:
    print('O nome da cidade digitado acima NÃO começa com "Santo"')