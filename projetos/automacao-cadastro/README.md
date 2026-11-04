# Automação de Cadastro de Produtos

Projeto desenvolvido em Python para automatizar o cadastro de produtos em um sistema web utilizando PyAutoGUI e Pandas.

O programa lê os dados de um arquivo CSV e preenche automaticamente os campos do formulário no navegador.

## Funcionalidades

- Abertura automática do Google Chrome
- Acesso à página de cadastro
- Preenchimento automático dos campos do formulário
- Leitura dos dados de um arquivo CSV
- Cadastro de vários produtos em sequência
- Preenchimento de observações quando disponíveis

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- CSV
- Pathlib

## Estrutura do projeto

```text
automacao-cadastro/
├── automacao.py
├── produtos.csv
├── README.md
└── requirements.txt
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/gustavo-gds-dias/python-projects.git
```

Acesse a pasta do projeto:

```bash
cd python-projects/projetos/automacao-cadastro
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python automacao.py
```

## Observações importantes

**Este projeto não é universal.**

A automação utiliza coordenadas de tela para identificar onde realizar os cliques. Essas coordenadas foram definidas com base na resolução e na configuração de tela utilizadas durante o desenvolvimento.

Por isso, pode ser necessário ajustar as coordenadas para funcionar em outros computadores.

Para executar corretamente:

- Utilize o Google Chrome.
- Mantenha a resolução e a escala de tela compatíveis com as utilizadas no desenvolvimento ou ajuste as coordenadas.
- Deixe a janela do navegador na posição esperada pelo código.
- Mantenha o arquivo `produtos.csv` na mesma pasta do script.
- Verifique se a página de cadastro está acessível.

**Atenção:** o programa realiza cliques e digitação automaticamente. Evite utilizar o computador durante a execução para não interferir na automação.

## Objetivo

Projeto desenvolvido durante meus estudos de Python para praticar automação de tarefas, manipulação de dados com Pandas, leitura de arquivos CSV e interação com interfaces gráficas utilizando PyAutoGUI.