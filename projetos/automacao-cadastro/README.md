# Automação de Cadastro

Automação desenvolvida em Python para realizar o cadastro de produtos em um sistema web a partir de dados armazenados em um arquivo CSV.

O projeto foi desenvolvido como exercício prático de automação durante meus estudos de Python.

## Tecnologias utilizadas

* Python
* PyAutoGUI
* Pandas
* CSV

## Como funciona

1. Abre o navegador e acessa o sistema de cadastro.
2. Realiza o login utilizando dados fictícios fornecidos para o exercício.
3. Lê os produtos armazenados no arquivo `produtos.csv`.
4. Percorre cada registro da tabela.
5. Preenche os campos do formulário automaticamente utilizando PyAutoGUI.
6. Envia cada cadastro para o sistema.

## Estrutura do projeto

```text
automacao-cadastro/
├── automacao.py
├── produtos.csv
├── requirements.txt
└── README.md
```

## Instalação

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Execução

Execute o arquivo:

```bash
python automacao.py
```

Durante a execução, o PyAutoGUI controla o mouse e o teclado para preencher o formulário automaticamente.

## Observações

A automação foi desenvolvida especificamente para a interface utilizada no exercício. Por utilizar coordenadas da tela e depender dos campos e da estrutura da página, alterações no site ou na resolução/layout da tela podem fazer com que o código precise ser ajustado.

O site utilizado no exercício pode ser desativado ou alterado no futuro, portanto o projeto pode não ser executável atualmente. O código e o arquivo CSV são mantidos como registro do projeto e dos conceitos de automação praticados.

## Objetivo

Praticar automação de tarefas repetitivas utilizando Python, trabalhando com leitura de dados através do Pandas e interação automatizada com interfaces utilizando PyAutoGUI.
