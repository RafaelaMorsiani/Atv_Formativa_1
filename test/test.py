from unittest.mock import patch, Mock
from src.main import buscar_cotacao


def criar_mock_api(brl=5.00, eur=0.90, pen=3.70):
    mock_response = Mock()
    mock_response.json.return_value = {
        "rates": {
            "BRL": brl,
            "EUR": eur,
            "PEN": pen
        }
    }
    return mock_response


@patch("builtins.input", side_effect=["10", "20", "30"])
@patch("src.main.requests.get")
def test_mostra_cotacao_brl(mock_get, mock_input, capsys):
    mock_get.return_value = criar_mock_api()

    buscar_cotacao()

    output = capsys.readouterr().out
    assert "1 USD = R$ 5.00" in output


@patch("builtins.input", side_effect=["10", "20", "30"])
@patch("src.main.requests.get")
def test_mostra_cotacao_eur(mock_get, mock_input, capsys):
    mock_get.return_value = criar_mock_api()

    buscar_cotacao()

    output = capsys.readouterr().out
    assert "1 USD = € 0.90" in output


@patch("builtins.input", side_effect=["10", "20", "30"])
@patch("src.main.requests.get")
def test_mostra_cotacao_pen(mock_get, mock_input, capsys):
    mock_get.return_value = criar_mock_api()

    buscar_cotacao()

    output = capsys.readouterr().out
    assert "1 USD = S/. 3.70" in output


@patch("builtins.input", side_effect=["10", "20", "30"])
@patch("src.main.requests.get")
def test_conversao_usd_para_brl(mock_get, mock_input, capsys):
    mock_get.return_value = criar_mock_api()

    buscar_cotacao()

    output = capsys.readouterr().out
    assert "Convertido: R$ 50.00" in output


@patch("src.main.requests.get")
def test_erro_na_api(mock_get, capsys):
    mock_get.side_effect = Exception("Falha na API")

    buscar_cotacao()

    output = capsys.readouterr().out
    assert "Erro:" in output