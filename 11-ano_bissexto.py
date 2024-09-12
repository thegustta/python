def eh_bissexto(ano):
    # Verifica se o ano é divisível por 400
    if ano % 400 == 0:
        return True
    # Verifica se o ano é divisível por 100, mas não por 400
    elif ano % 100 == 0:
        return False
    # Verifica se o ano é divisível por 4
    elif ano % 4 == 0:
        return True
    else:
        return False

# Solicitar ao usuário que insira um ano
ano = int(input("Digite um ano: "))

# Verificar se o ano é bissexto
if eh_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
