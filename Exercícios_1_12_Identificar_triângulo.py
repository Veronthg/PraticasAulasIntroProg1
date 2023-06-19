# Definição das variáveis a serem utilizadas — Entrada
print('Identificando se é um triângulo e qual tipo de triângulo é.')
print('-----------------------------------------------------------')
lado_1 = float(input('Informe o primeiro lado: '))
lado_2 = float(input('Informe o segundo lado: '))
lado_3 = float(input('Informe o terceiro lado: '))

soma_dos_lados_1_2 = lado_1 + lado_2

if soma_dos_lados_1_2 > lado_3:
    print('A soma dos dois primeiros lados é maior que o terceiro lado, logo é um triângulo.')
    print('lado 3: %2.f , soma dos dois primeiros: %2.f' % (lado_3, soma_dos_lados_1_2))

if soma_dos_lados_1_2 <= lado_3:
    print('A soma dos dois primeiros lados é menor ou igual que o terceiro lado, logo não é possível ser um triângulo.')
    print('Tente novamente.')
    exit()

if lado_1 == lado_2 == lado_3:
    print('O triângulo é equilátero.')

elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print('O triângulo é isóceles.')

elif lado_1 != lado_2 != lado_3:
    print('O triângulo é escaleno.')
