import math

# Definição das variáveis a serem utilizadas — Entrada
area_para_pintar = float(input('Informe a área em metros quadradas a ser pintada:'))
litros_metro = 6
litros_lata = 18
valor_unit_lata = 80
litros_galao = 3.6
valor_unit_galao = 25

# Procedimentos
area_folga = area_para_pintar * 1.1
litros_usados = area_folga / litros_metro

# Saída 1 - Apenas latas de 18L
# quantidade de latas e valor total de latas
numero_latas = math.ceil(litros_usados / litros_lata)
valor_apenas_latas = numero_latas * valor_unit_lata
print(
    'O cliente deverá usar %d latas de 18 litros, resultando no valor de R$ %2.f' % (numero_latas, valor_apenas_latas))

# Saída 2 — Apenas galões de 3,6L
# quantidade de galões e valor total de galões
numero_galoes = math.ceil(litros_usados / litros_galao)
valor_apenas_galoes = numero_galoes * valor_unit_galao

print('O cliente deverá usar %d galões de 3,6 litros, resultando no valor de R$ %2.f' % (
    numero_galoes, valor_apenas_galoes))

# Saída 3 — Mistura de latas e galões com folga de 10% arrendondando
# compra misturada
numero_latas = math.floor(litros_usados / litros_lata)
valor_com_latas = numero_latas * valor_unit_lata
faltam_litros = litros_usados % litros_lata
numero_galoes = math.ceil(faltam_litros / litros_galao)
valor_com_galoes = numero_galoes * valor_unit_galao
valortotal = valor_com_latas + valor_com_galoes

print('O cliente deverá usar %d latas de 18 litros mais %d galões de 3,6 litros, resultando no valor de R$ %2.f'%(numero_latas, numero_galoes, valortotal))