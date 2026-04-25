from unittest.mock import patch, Mock
from src.main import buscar_cotacao


@patch("builtins.input", side_effect=["10", "20", "30"])
@patch("src.main.requests.get")
def test_buscar_cotacao_sucesso(mock_get, mock_input, capsys):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {
            "BRL": 5.00,
            "EUR": 0.90,
            "PEN": 3.70
        }
    }

    mock_get.return_value = mock_response

    buscar_cotacao()

    output = capsys.readouterr().out

    assert "===== COTAÇÃO ATUAL =====" in output
    assert "1 USD = R$ 5.00" in output
    assert "1 USD = € 0.90" in output
    assert "1 USD = S/. 3.70" in output
    assert "Convertido: R$ 50.00" in output
    assert "Convertido: EUR 18.00" in output
    assert "Convertido: PEN 111.00" in output


@patch("src.main.requests.get")
def test_buscar_cotacao_erro_api(mock_get, capsys):
    mock_get.side_effect = Exception("Falha na API")

    buscar_cotacao()

    output = capsys.readouterr().out

    assert "Erro:" in output
    assert "Falha na API" in output