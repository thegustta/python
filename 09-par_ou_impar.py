# Função para verificar se o número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Solicitar ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verificar se o número é par ou ímpar
resultado = verificar_par_ou_impar(numero)

# Exibir o resultado
print(f"O número {numero} é {resultado}.")
