import re
from decimal import Decimal
from pathlib import Path

from playwright.sync_api import Page, expect


def test_cupom_valido(page: Page):
    page.goto(
        "https://verzel-store.qa-test-verzel-store.workers.dev/",
        wait_until="domcontentloaded",
    )

    produto = page.get_by_role("heading", name="Mochila Urbana 20L")
    expect(produto).to_be_visible()
    produto.locator("xpath=ancestor::article").get_by_role(
        "button", name="Adicionar ao carrinho"
    ).click()

    page.get_by_role("link", name=re.compile("Carrinho", re.IGNORECASE)).click()
    campo_cupom = page.get_by_label(
        re.compile("cupom", re.IGNORECASE)
    )
    campo_cupom.fill("BEMVINDO10")
    page.get_by_role(
        "button",
        name=re.compile("aplicar", re.IGNORECASE),
    ).click()

    expect(page.get_by_text("Mochila Urbana 20L")).to_be_visible()
    expect(page.get_by_text("Cupom BEMVINDO10 aplicado.")).to_be_visible()
    expect(page.locator('[data-valor="subtotal"]')).to_have_text("R$ 100,00")

    subtotal = Decimal("100.00")
    desconto = subtotal * Decimal("0.10")
    frete = Decimal("19.90")
    total = subtotal - desconto + frete
    desconto_exibido = f"- R$ {desconto:.2f}".replace(".", ",")
    total_exibido = f"R$ {total:.2f}".replace(".", ",")

    expect(page.locator('[data-valor="desconto"]')).to_have_text(desconto_exibido)
    expect(page.locator('[data-valor="frete"]')).to_have_text("R$ 19,90")
    valor_total = page.locator('[data-valor="total"]')
    expect(valor_total).to_have_text(total_exibido)

    pasta_evidencias = Path("evidencias")
    pasta_evidencias.mkdir(parents=True, exist_ok=True)
    valor_total.screenshot(path=str(pasta_evidencias / "total-com-cupom.png"))