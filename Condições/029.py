#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00 por cada km acima do limite


km = int(input('Qual a velocidade do carro: '))

if km > 80:
    multa = km * 7
    print('Você foi multado e terá que pagar R${} reais'.format(multa))
else:
    print('Você está dentro do limite de velocidade')