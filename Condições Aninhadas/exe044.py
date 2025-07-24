#Elabore um programa que calcule o valor a ser pago por um produto,
#Considerando o seu preço normal e condição de pagamento:

#À vista dinheiro/cheque: 10% de desconto
#À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

cores = {'limpa':'\033[m',
         'Amarelo':'\033[1;33m',
         'Vermelho':'\033[1;31m',
         'Azul':'\033[1;34m',
         'Branco bold':'\033[1;97m',
         'Branco':'\033[97m'}


print(f"{cores['Branco bold']}---CALCULADORA DE DESCONTO/JUROS---{cores['limpa']}")

valor = float(input(f"{cores['Branco']}Digite o valor do produto: "))
formaPag = int(input('Escolha a forma de pagamento\n'
                     '1- Á vista/cheque\n'
                     '2- Á vista no cartão\n'
                     '3- Em até 2x no cartão\n'
                     '4- 3x ou mais no cartão\n'))

if formaPag == 1:
    porc = (valor * 10) / 100
    desc = valor - porc
    print('O cliente receberá um desconto de 10% e o valor cairá de R${:.2f} para apenas R${}{:.2f}'.format( valor, cores['Amarelo'], desc, cores['limpa']))
elif formaPag == 2:
    porc = (valor * 2) / 100
    desc = valor - porc
    print('O cliente receberá um desconto de 2% e o valor cairá de R${:.2f} para apenas R${}{:.2f}'.format(valor, cores['Amarelo'], desc, cores['limpa']))
elif formaPag == 3:
    print('O cliente pagará o valor normal de R${}{:.2f}'.format(cores['Azul'], valor))
elif formaPag == 4:
    porc = (valor * 20) / 100
    juros = valor + porc
    print('O cliente pagara juros no valor de R${:.2f} e o valor final será de R${}{:.2f}'.format( porc, cores['Vermelho'], juros))
