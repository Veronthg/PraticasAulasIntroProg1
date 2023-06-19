# Definição das variáveis a serem utilizadas — Entrada
print('------------REAJUSTE DE SALÁRIO-------------------')
print('Para salários até R$280,00 o aumento será de 20%')
print('Para salários entre R$280,00 e R%700,00 o aumento será de 15%')
print('Para salários entre R$700,00 e R$1.500,00 o aumento será de 10%')
print('Para salários de R$1.500,00 em diante o aumento será de 5%')
salario_colaborador = float(input('Informe o salário atual do colaborador: '))
print('_____________________________________________________________')

if salario_colaborador <= 0:
    print('O salário a ser reajustado não pode ser zero ou negativo, tente novamente.')
    exit()
elif salario_colaborador <= 280:
    aumento_percentual = 0.2
    reajuste_salario = salario_colaborador * aumento_percentual
    salario_reajustado = salario_colaborador + reajuste_salario
    print('O salário do colaborador antes do reajuste era: R$ %2.f' % salario_colaborador)
    aumento_percentual = aumento_percentual * 100
    print('O aumento aplicado será de:', aumento_percentual, '%')
    print('O total do aumento é: R$ %2.f' % reajuste_salario)
    print('O salário do colaborador após reajuste finaliza em: R$ %2.f' % salario_reajustado)
elif 280 < salario_colaborador < 700:
    aumento_percentual = 0.15
    reajuste_salario = salario_colaborador * aumento_percentual
    salario_reajustado = salario_colaborador + reajuste_salario
    print('O salário do colaborador antes do reajuste era: R$ %2.f' % salario_colaborador)
    aumento_percentual = aumento_percentual * 100
    print('O aumento aplicado será de:', aumento_percentual, '%')
    print('O total do aumento é: R$ %2.f' % reajuste_salario)
    print('O salário do colaborador após reajuste finaliza em: R$ %2.f' % salario_reajustado)
elif 700 <= salario_colaborador < 1500:
    aumento_percentual = 0.1
    reajuste_salario = salario_colaborador * aumento_percentual
    salario_reajustado = salario_colaborador + reajuste_salario
    print('O salário do colaborador antes do reajuste era: R$ %2.f' % salario_colaborador)
    aumento_percentual = aumento_percentual * 100
    print('O aumento aplicado será de:', aumento_percentual, '%')
    print('O total do aumento é: R$ %2.f' % reajuste_salario)
    print('O salário do colaborador após reajuste finaliza em: R$ %2.f' % salario_reajustado)
elif salario_colaborador >= 1500:
    aumento_percentual = 0.05
    reajuste_salario = salario_colaborador * aumento_percentual
    salario_reajustado = salario_colaborador + reajuste_salario
    print('O salário do colaborador antes do reajuste era: R$ %2.f' % salario_colaborador)
    aumento_percentual = aumento_percentual * 100
    print('O aumento aplicado será de:', aumento_percentual, '%')
    print('O total do aumento é: R$ %2.f' % reajuste_salario)
    print('O salário do colaborador após reajuste finaliza em: R$ %2.f' % salario_reajustado)
else:
    print('Revise as informações!')
