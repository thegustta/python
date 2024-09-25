def calcular_reducao_tempo_vida():
    # Solicita a quantidade de cigarros fumados por dia
    cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
    # Solicita a quantidade de anos fumando
    anos_fumando = int(input("Digite quantos anos você fumou: "))

    # Cálculo dos minutos perdidos
    minutos_por_cigarro = 10
    total_cigarros = cigarros_por_dia * 365 * anos_fumando
    minutos_perdidos = total_cigarros * minutos_por_cigarro

    # Convertendo minutos perdidos em dias
    dias_perdidos = minutos_perdidos / (60 * 24)

    # Exibe o resultado
    print(f"Você perderá aproximadamente {dias_perdidos:.2f} dias de vida.")

# Executa a função
calcular_reducao_tempo_vida()
