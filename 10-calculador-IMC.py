# Função para calcular o IMC e determinar a classificação
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 34.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Solicitar ao usuário que insira o peso e a altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Classificar o IMC
classificacao = classificar_imc(imc)

# Exibir o resultado
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
