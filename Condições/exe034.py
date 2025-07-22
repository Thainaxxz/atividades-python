#Escreva um programa que pergunta o salário de um funcionário e calcule o valor do seu aumento
#Para salários superiores a R$1.250,00 calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%



print('-----CALCULADORA DE AUMENTO SALARIAL-----')
sal = float(input('Qual o valor do seu salário?(em reais) '))

if sal > 1250:
    soma = (sal * 10) / 100
    soma2 = soma + sal
    print('Você receberá um aumento de R${:.2f} e seu salario final será de R$${:.2f}'.format(soma, soma2))
elif sal <= 1250:
    soma = (sal * 15) / 100
    soma2 = soma = sal
    print('Você receberá um aumento de R${:.2f} e seu salario final será de R$${:.2f}'.format(soma, soma2))
