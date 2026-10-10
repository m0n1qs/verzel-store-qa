# Verzel Store QA — Automação de Testes

## 1. Apresentação do projeto

Projeto de automação para validar a vitrine, o carrinho, o cupom de desconto e o cálculo do pedido na loja de testes da Verzel.

**Aplicação testada:** https://verzel-store.qa-test-verzel-store.workers.dev/

### Tecnologias utilizadas

- **Python:** 
- **Playwright:** 
- **pytest:** 
- **Chromium:** 

## 2. Pré-requisitos

Para executar o projeto em um computador Windows, instale:

1. Python 3: https://www.python.org/downloads/windows/
2. Git para Windows: https://git-scm.com/downloads/win
3. Visual Studio Code: https://code.visualstudio.com/Download


Durante a instalação do Python, marque a opção `Add python.exe to PATH`, caso ela apareça.

Para conferir as instalações, abra o terminal e execute:

```powershell
python --version
python -m pip --version
git --version
```

Os comandos devem exibir as versões instaladas.

## 3. Baixar e abrir o projeto

Baixe o repositório pelo GitHub, extraia os arquivos e abra a pasta do projeto no VS Code.

No VS Code, abra o terminal em **Terminal → New Terminal**.

Todos os comandos das próximas etapas devem ser executados na pasta raiz do projeto.

## 4. Preparar o ambiente de execução

### 4.1. Criar o ambiente virtual

Execute:

```powershell
python -m venv .venv
```

### 4.2. Ativar o ambiente virtual

No PowerShell, execute:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando a ativação funcionar, normalmente aparecerá `(.venv)` no início da linha do terminal.

Se o PowerShell bloquear a ativação, execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois, tente ativar novamente.

### 4.3. Instalar as dependências

Com o ambiente virtual ativado, execute:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Caso o arquivo ainda não contenha as dependências necessárias, utilize:

```powershell
python -m pip install pytest playwright pytest-playwright
```

### 4.4. Instalar o navegador

Execute:

```powershell
python -m playwright install chromium
```

**Por que fazer isso?**

O Playwright precisa de um navegador compatível para executar as ações automatizadas. Esse comando instala o Chromium utilizado pelo projeto.

## 5. Executar um cenário por vez

Use o caminho abaixo para executar apenas um cenário com o Chromium visível:

```powershell
python -m pytest tests/test_store.py::test_store_adiciona_produto_ao_carrinho --headed -s --slowmo 700
```

Para executar o cenário de cupom com o navegador visível:

```powershell
python -m pytest tests/test_cupom.py::test_cupom_valido --headed -s --slowmo 700
```

Para executar somente o cenário da API (não abre navegador):

```powershell
python -m pytest tests/test_api.py::test_api_calcula_carrinho_com_cupom
```

Cada comando seleciona apenas um cenário. Os testes de interface abrem o Chromium com `--headed`; o teste da API usa a biblioteca padrão do Python.


## 6. Cenários automatizados

- `tests/test_store.py::test_store_adiciona_produto_ao_carrinho`: abre a loja, adiciona a Camiseta Essencial ao carrinho, valida o subtotal e registra uma captura de tela.
- `tests/test_cupom.py::test_cupom_valido`: adiciona a Mochila Urbana, aplica o cupom, valida o desconto de 10% e registra o valor total.
- `tests/test_api.py::test_api_calcula_carrinho_com_cupom`: valida o cálculo do carrinho e do cupom pelo endpoint da API.

## 7. Testes manuais de API

Os testes manuais de API podem ser realizados gratuitamente pelo Hoppscotch:

-Acesse https://hoppscotch.io/.
-Abra o cliente REST/HTTP.
-Selecione o método HTTP correspondente ao cenário (GET ou POST).

Os endpoints e formatos de requisição devem ser confirmados no ambiente de teste antes da execução.

## 8. Consultar as evidências

Os cenários de interface registram capturas de tela na pasta `evidencias/`.

Após uma execução bem-sucedida, verifique:

```text
evidencias/
├── carrinho-com-produto.png
└── total-com-cupom.png
```

As imagens mostram o carrinho com o produto adicionado e o valor final após a aplicação do cupom.

## 9. Solução de problemas

| Problema | Solução |
|---|---|
| `python` não é reconhecido | Verifique a instalação do Python ou tente utilizar `py`. |
| `No module named pytest` | Ative o ambiente virtual e instale as dependências. |
| `No module named playwright` | Execute `python -m pip install -r requirements.txt`. |
| `Executable doesn't exist` | Execute `python -m playwright install chromium`. |
| Erro ao ativar `.venv` | Utilize a configuração temporária de execução do PowerShell descrita na seção 4. |
| Timeout ou erro de conexão | Verifique a conexão com a internet e a disponibilidade da loja. |
| Status HTTP diferente de `200` | Registre o resultado e investigue a causa; não altere o teste apenas para fazê-lo passar. |
| O Chrome não abre | Tente executar com Chromium, sem `--browser-channel chrome`. |
| A captura de tela não aparece | Confira se o teste chegou à etapa de screenshot e se a pasta `evidencias` foi criada. |

## 11. Executar novamente

Nas próximas execuções, não é necessário recriar o ambiente virtual se ele continuar instalado e funcionando.

Abra o terminal na raiz do projeto e execute o cenário desejado, por exemplo:

```powershell
\.venv\Scripts\python.exe -m pytest tests/test_store.py::test_store_adiciona_produto_ao_carrinho --headed -s --slowmo 700
```

Para executar o cupom ou a API, use os comandos individuais da seção 5. O teste da API não usa navegador; os cenários da loja usam Chromium visível.


## 12. Uso de IA

Foi utilizado IA como auxílio para:

Escrita de cenários 
Automação de cenários 

IA's utilizadas: Copilot e ChatGPT


## 13. Acesso aos cenários/evidências/bug report

Copie e cole o link no browser para acessar a planilha:
https://1drv.ms/x/c/f4711bc1f24dfffd/IQC597VlhwGQS63M50vXieWnAU6yQCndclZqxfyc70jklPk?e=a1wE3i