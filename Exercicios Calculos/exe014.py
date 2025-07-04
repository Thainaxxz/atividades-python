#Leia o salario de um funcionario e mostre seu novo com 15% de desconto



sal = float(input('Qual o seu salário? '))
porc = (sal * 15) / 100
aum = sal + porc

print('O seu salario pós aumento de 15% será de R${:.2f}'.format(aum))