import requests

def buscar_cotacao():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    try:
        response = requests.get(url)
        data = response.json()

        cotacao = data["rates"]["BRL"]

        print(f"1 USD = R$ {cotacao:.2f}")

        eur = data["rates"]["EUR"]
        print(f"1 USD = € {eur:.2f}")

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    buscar_cotacao()