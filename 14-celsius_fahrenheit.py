# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius / 5) + 32
    return fahrenheit

# Entrada de dados
celsius = float(input("Digite a temperatura em °C: "))

# Cálculo da conversão
fahrenheit = celsius_para_fahrenheit(celsius)

# Saída do resultado
print(f"A temperatura em °F é: {fahrenheit:.2f}")
