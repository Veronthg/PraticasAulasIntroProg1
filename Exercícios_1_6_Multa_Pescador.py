peso = float(input("Informe o peso do peixe: "))
excesso = float(0.0)
if peso > 50.0:
  excesso = peso - 50
  multa = excesso * 4
  print("O peso de peixes que você pescou passa do excesso regulamentado.")
  print("Pescou um total de: ", peso," quilos.")
  print("Resultando num excesso de: ", excesso," quilos.")
  print("O total da multa é: R$", multa)
elif peso <= 0 :
  print("Não pescou peixes hoje.")
else :
  print("O peso de peixes que você pescou não conta multa.")
  print("Pesando: ", peso," quilos.")