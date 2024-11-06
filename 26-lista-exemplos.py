# Solicitar 5 números inteiros do usuário
numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

# Calcular o maior, menor e a soma
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)

# Imprimir os resultados
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"A soma de todos os números é: {soma}")
