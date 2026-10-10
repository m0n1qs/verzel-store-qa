import re
from pathlib import Path

from playwright.sync_api import Page, expect


URL = "https://verzel-store.qa-test-verzel-store.workers.dev/"


def test_store_adiciona_produto_ao_carrinho(page: Page):
    resposta = page.goto(URL, wait_until="domcontentloaded")

    assert resposta is not None, "A página não retornou uma resposta."
    assert resposta.status == 200, (
        f"Status HTTP inesperado: {resposta.status}"
    )

    produto = page.get_by_role("heading", name="Camiseta Essencial")
    expect(produto).to_be_visible()
    produto.locator("xpath=ancestor::article").get_by_role(
        "button", name="Adicionar ao carrinho"
    ).click()

    page.get_by_role("link", name=re.compile("Carrinho", re.IGNORECASE)).click()
    expect(page.get_by_role("heading", name="Carrinho")).to_be_visible()
    expect(page.get_by_text("Camiseta Essencial")).to_be_visible()
    expect(page.locator('[data-valor="subtotal"]')).to_have_text("R$ 59,90")

    pasta_evidencias = Path("evidencias")
    pasta_evidencias.mkdir(parents=True, exist_ok=True)

    page.screenshot(
        path=str(pasta_evidencias / "carrinho-com-produto.png"),
        full_page=True,
    )

