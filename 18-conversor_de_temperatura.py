def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def main():
    while True:
        print("\nMenu de Conversão de Temperaturas:")
        print("1. Converter de Celsius para Fahrenheit")
        print("2. Converter de Celsius para Kelvin")
        print("3. Converter de Fahrenheit para Celsius")
        print("4. Converter de Fahrenheit para Kelvin")
        print("5. Converter de Kelvin para Celsius")
        print("6. Converter de Kelvin para Fahrenheit")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '0':
            print("Saindo do programa.")
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            temp = float(input("Digite a temperatura a ser convertida: "))

            if choice == '1':
                print(f"{temp} °C é igual a {celsius_to_fahrenheit(temp):.2f} °F")
            elif choice == '2':
                print(f"{temp} °C é igual a {celsius_to_kelvin(temp):.2f} K")
            elif choice == '3':
                print(f"{temp} °F é igual a {fahrenheit_to_celsius(temp):.2f} °C")
            elif choice == '4':
                print(f"{temp} °F é igual a {fahrenheit_to_kelvin(temp):.2f} K")
            elif choice == '5':
                print(f"{temp} K é igual a {kelvin_to_celsius(temp):.2f} °C")
            elif choice == '6':
                print(f"{temp} K é igual a {kelvin_to_fahrenheit(temp):.2f} °F")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
