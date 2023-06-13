#Definição das variáveis a serem utilizadas - Entrada
num1 = int(input("Informe o primeiro número inteiro: ")) #Inteiro 1
num2 = int(input("Informe o segundo número inteiro: "))  #Inteiro 2
num3f = float(input("Informe o número real: ")) #real

#Procedimentos
res1 = (num1 * 2) * (num2 / 2) #Primeiro
res2 = (num1 * 3) + num3f  #Segundo
res3 = pow(num3f,3)  #Terceiro

#Saída
print("O produto do dobro do primeiro com metade do segundo é: ", res1)
print("O resultado da soma do triplo do primeiro com o terceiro é: ", res2)
print("O terceiro número elevado ao cubo resulta em: ", res3)