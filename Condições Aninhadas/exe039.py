#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
#Se ele ainda vai se alistar no serviço militar
#Se é hora de se alistar
#Se já passou no tempo do alistamento

#O programa também deverá mostrar o tempo que falta ou que passou de prazo

ano = int(input('Digite seu ano de nascimento: '))

if ano > 2007:
    prazo = ano - 2007
    print('Você ainda não precisa se alistar, faltam {} anos'.format(prazo))
elif ano < 2007:
    prazo = 2007 - ano
    print('Você precisa se alistar, já se passaram {} anos desde a data correta do alistamento'.format(prazo))
elif ano == 2007:
    print('Você precisa se alistar esse ano!')