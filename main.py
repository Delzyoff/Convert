import requests


def get_exchange_rate(base_currency, target_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['rates'][target_currency]
    else:
        return None


def main():
    print("Конвертация валют")
    print("Валюты: RUB, USD")

    base_currency = "RUB"
    target_currency = "USD"

    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        print(f"Курс {base_currency} к {target_currency}: {exchange_rate}")

        amount_rub = float(input("Сумма в рублях: "))
        amount_usd = amount_rub * exchange_rate
        print(f"Сумма в долларах: {amount_usd}")
    else:
        print("Ошибка получения данных")


if __name__ == "__main__":
    main()
