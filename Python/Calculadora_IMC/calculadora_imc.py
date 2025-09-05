print("Calculadora de IMC") 
print(" ")
print("-" * 30)
print(" ")

# Pede dados do usuário
peso = float(input("Digite seu peso em kg: ").replace(",", "."))
altura = float(input("Digite sua altura em metros: ").replace(",", "."))

print(" ")
print("-" * 30)
print(" ")

# Calcula IMC
imc = peso / (altura ** 2)

# Mostra o resultado
print(f"Seu IMC é: {imc:.2f}")

print(" ")
print("-" * 30)
print(" ")

# Classificação simples
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")