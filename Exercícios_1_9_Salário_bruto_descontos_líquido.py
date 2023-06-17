# Definição das variáveis a serem utilizadas — Entrada
salario_hora = float(input("Informe quanto você recebe por hora trabalhada: "))
horas_trabalhadas = float(input("Informe quantas horas você trabalhou esse mês: "))
imposto_renda = 0.11
inss = 0.08
sindicato = 0.05
index = 0
# Procedimento
if salario_hora <= 0 or horas_trabalhadas <= 0:
    print('')
    print('As informações não podem ser menores ou iguais a zero, reinicie o código.')
    exit()
salario_total_bruto = salario_hora * horas_trabalhadas
print('Seu salário bruto esse mês resultou em R$ %2.f' % salario_total_bruto)
print('---------------------------------------------')
print('Descontos:')
valor_imposto_renda = salario_total_bruto * imposto_renda
salario_descontado = salario_total_bruto - valor_imposto_renda
print('O valor do seu imposto de renda foi: R$ %2.f' % valor_imposto_renda)
print('Seu salário após o desconto do imposto de renda: R$ %2.f' % salario_descontado)
valorinss = salario_total_bruto * inss
salario_descontado = salario_descontado - valorinss
print('INSS: R$ %2.f' % valorinss)
print('Seu salário após o desconto do INSS: R$ %2.f' % salario_descontado)
valorsindicato = salario_total_bruto * sindicato
salario_descontado = salario_descontado - valorsindicato
print('Sindicato: R$ %2.f ' % valorsindicato)
print('Seu salário após o desconto do Sindicato: R$ %2.f' % salario_descontado)
print('---------------------------------------------')
salario_liquido = salario_descontado
print('Seu salário líquido após todos os descontos é: R$ %2.f ' % salario_liquido)
