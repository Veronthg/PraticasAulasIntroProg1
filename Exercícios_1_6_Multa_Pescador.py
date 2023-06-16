# Definição das variáveis a serem utilizadas - Entrada
peso = float(input("Informe o peso do peixe: "))
excesso = float(0.0)
# Procedimentos
if peso > 50.0:
    excesso = peso - 50
    multa = excesso * 4
    # Saída 1 - Com multa
    print("O peso de peixes que você pescou passa do excesso regulamentado.")
    print("Pescou um total de: ", peso, " quilos.")
    print("Resultando num excesso de: ", excesso, " quilos.")
    print("O total da multa é: R$", multa)
elif peso <= 0:
    # Saída 2 - nenhum peixe
    print("Não pescou peixes hoje.")
else:
    # Saída 3 - dentro do limite
    print("O peso de peixes que você pescou não conta multa.")
    print("Pesando: ", peso, " quilos.")