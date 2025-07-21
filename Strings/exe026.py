#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra A
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
print('A letra "A" apareceu {} vezes'.format(frase.count('A')))
print('Ela apareceu a primeira vez na posição {}'.format(frase.find('A')))
print('Ela apareceu a última vez na posição {}'.format(frase.rfind('A')))