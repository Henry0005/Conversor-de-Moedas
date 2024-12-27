import requests

def convert_currency(amount, from_currency, to_currency):
    API_KEY = "3c8328e9c2e64402b63014720dbf8094"
    base_url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        exchange_rate = data["rates"][to_currency] / data["rates"][from_currency]
        return amount * exchange_rate
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

def usd_to_brl():
    amount = float(input("Digite o valor em Dólares: "))
    converted_amount = convert_currency(amount, "USD", "BRL")
    if converted_amount is not None:
        print(f"{amount} USD é igual a {converted_amount:.2f} BRL")

def brl_to_usd():
    amount = float(input("Digite a quantia em Reais: "))
    converted_amount = convert_currency(amount, "BRL", "USD")
    if converted_amount is not None:
        print(f"{amount} BRL é igual a {converted_amount:.2f} USD")

def brl_to_bitcoin():
    amount = float(input("Digite a quantia em Reais: "))
    converted_amount = convert_currency(amount, "BRL", "BTC")
    if converted_amount is not None:
        print(f"{amount} Reais é igual a {converted_amount:.8f} Bitcoins")

def bitcoin_to_brl():
    amount = float(input("Digite a quantidade de Bitcoins: "))
    converted_amount = convert_currency(amount, "BTC", "BRL")
    if converted_amount is not None:
        print(f"{amount} Bitcoin é igual a {converted_amount:.2f} BRL")

def bitcoin_to_usd():
    amount = float(input("Digite a quantidade de Bitcoins: "))
    converted_amount = convert_currency(amount, "BTC", "USD")
    if converted_amount is not None:
        print(f"{amount} Bitcoin é igual a {converted_amount:.2f} USD")

def usd_to_bitcoin():
    amount = float(input("Digite o valor em Dólares: "))
    converted_amount = convert_currency(amount, "USD", "BTC")
    if converted_amount is not None:
        print(f"{amount} USD é igual a {converted_amount:.8f} Bitcoins")

def main_menu():
    print("Obrigado por usar o conversor de moedas!")
    while True:
        print("\n--- Conversor de Moedas ---")
        print("1. Converter USD para BRL")
        print("2. Converter BRL para USD")
        print("3. Converter BRL para Bitcoin")
        print("4. Converter Bitcoin para BRL")
        print("5. Converter Bitcoin para USD")
        print("6. Converter USD para Bitcoin")
        print("7. Sair")
        
        choice = input("Escolha uma opção: ")
        if choice == "1":
            usd_to_brl()
        elif choice == "2":
            brl_to_usd()
        elif choice == "3":
            brl_to_bitcoin()
        elif choice == "4":
            bitcoin_to_brl()
        elif choice == "5":
            bitcoin_to_usd()
        elif choice == "6":
            usd_to_bitcoin()
        elif choice == "7":
            print("Obrigado por usar o conversor de moedas. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu principal
if __name__ == "__main__":
    main_menu()
