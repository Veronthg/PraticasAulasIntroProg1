print('Saudação condicional')
print('Informe o turno que você estuda: ')
resposta = input("M - matutino / V - vespertino / N - noturno ->: ")
if resposta == "M":
    print('Bom Dia!')
elif resposta == "V":
    print('Boa Tarde!')
elif resposta == "N":
    print('Boa Noite!')
else:
    print('Valor Inválido.')
