#Recebe um numero e retona o dobro o triplo e a raiz quadrada dele


n1 = int(input('Digite um numero: '))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1 ** (1/2)

print('O dobro de {} é {}, o triplO é {} e a raiz quadrada é {}'.format(n1, n2, n3, n4))