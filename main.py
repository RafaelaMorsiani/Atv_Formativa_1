import requests

def buscar_cotacao():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    try:
        print("===== COTAÇÃO ATUAL =====")

        response = requests.get(url)
        data = response.json()

        #USD to BRL
        cotacao = data["rates"]["BRL"]
        print(f"1 USD = R$ {cotacao:.2f}")

        #USD to EUR 
        eur = data["rates"]["EUR"]
        print(f"1 USD = € {eur:.2f}")

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    buscar_cotacao()