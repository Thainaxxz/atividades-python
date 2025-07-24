#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de atleta
#E mostre sua categoria, de acordo com a idade:

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

ano = int(input('Digite o ano de nascimento do atleta: '))
if ano >= 2016:
    print('MIRIM')
elif (ano < 2016) and (ano > 2011):
    print('INFANTIL')
elif (ano < 2011) and (ano > 2006):
    print('JUNIOR')
elif (ano < 2006) and (ano > 2005):
    print('SENIOR')
elif (ano < 2005):
    print('MASTER')