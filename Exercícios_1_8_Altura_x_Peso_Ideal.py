altura = float(input('Informe a sua altura: '))
sexo = input('Informe seu sexo: M para masculino / F para feminino: ')
if sexo == "M":
    peso_ideal_masc = (72.7 * altura) - 58
    print('Seu peso ideal para a sua altura é: %2.f quilos'%(peso_ideal_masc))
elif sexo == "F":
    peso_ideal_fem = (62.1 * altura) - 44.7
    print('Seu peso ideal para a sua altura é: %2.f quilos' % (peso_ideal_fem))
else :
    print('Entrada incorreta de dados, revise as informações')