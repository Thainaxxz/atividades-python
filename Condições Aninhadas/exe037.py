#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão

#1 para binário
#2 para octal
#3 para hexadecimal


print('---CALCULADORA DE BASES---')
num = int(input('Digite um número: '))
op = int(input('\033[1;31mVocê deseja converter esse número para a base:\033[m\n'
               '\033[1;36m1 - Binária\n'
               '2 - Octal\n'
               '3 - Hexadecimal\033[m\n'))

if op == 1:
   num_binario = bin(num)
   print('O número {} na base binária é \033[1;36m{}'.format(num, num_binario))
elif op == 2:
    num_octal = oct(num)
    print('O número {} na base octal é \033[1;036m{}'.format(num, num_octal))
elif op == 3:
    num_hexa = hex(num)
    print('O número {} na base Hexadecimal é \033[1;36m{}'.format(num, num_hexa))
else:
    print('Opção inválida')







