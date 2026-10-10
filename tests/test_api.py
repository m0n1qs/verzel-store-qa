import json
from decimal import Decimal
from urllib.request import Request, urlopen


URL_CALCULO = "https://verzel-store.qa-test-verzel-store.workers.dev/api/carrinho/calcular"


def test_api_calcula_carrinho_com_cupom():
    dados = {
        "itens": [{"produtoId": "P005", "quantidade": 1}],
        "cupom": "BEMVINDO10",
    }
    requisicao = Request(
        URL_CALCULO,
        data=json.dumps(dados).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )

    with urlopen(requisicao, timeout=30) as resposta:
        assert resposta.status == 200
        resultado = json.loads(resposta.read().decode("utf-8"))

    assert resultado["itens"][0]["produtoId"] == "P005"
    assert Decimal(str(resultado["subtotal"])) == Decimal("100.00")
    assert Decimal(str(resultado["desconto"])) == Decimal("10.00")
    assert Decimal(str(resultado["frete"])) == Decimal("19.90")
    assert Decimal(str(resultado["total"])) == Decimal("109.90")
    assert resultado["cupom"]["codigo"] == "BEMVINDO10"
    assert resultado["cupom"]["aplicado"] is True