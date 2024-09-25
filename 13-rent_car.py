# Função para calcular o preço a pagar pelo aluguel do carro
def calcular_preco(km_percorridos, dias_alugado):
    preco_por_dia = 60.00
    preco_por_km = 0.15
    
    total_dias = dias_alugado * preco_por_dia
    total_km = km_percorridos * preco_por_km
    
    total = total_dias + total_km
    return total

# Entrada de dados
km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugado = int(input("Digite a quantidade de dias que o carro foi alugado: "))

# Cálculo do preço
preco_total = calcular_preco(km_percorridos, dias_alugado)

# Saída do resultado
print(f"O total a pagar pelo aluguel do carro é: R$ {preco_total:.2f}")
