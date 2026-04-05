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

        #USD to PEN - Peruvian Sol
        pen = data["rates"]["PEN"]  # Peruvian Sol
        print(f"1 USD = S/. {pen:.2f}")

        #Conversion input - USD to BRL
        valor = float(input("Digite um valor em USD para conversão à BRL: "))
        print(f"Convertido: R$ {valor * cotacao:.2f}")

        #Conversion input - USD to EUR
        valor = float(input("Digite um valor em USD para conversão à EUR: "))
        print(f"Convertido: EUR {valor * eur:.2f}")

        #Conversion input - USD to PEN
        valor = float(input("Digite um valor em USD para conversão à PEN: "))
        print(f"Convertido: PEN {valor * pen:.2f}")

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    buscar_cotacao()
