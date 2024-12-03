# Request Time Analysis

Este projeto realiza testes de desempenho de várias rotas de uma API, coletando informações sobre o tempo de resposta e estatísticas, como mínimo, máximo, média, desvio padrão e percentis (P90, P95, P99). O script usa a biblioteca `requests` para enviar as requisições e salvar os resultados em um arquivo CSV.

## Funcionalidades

- Testa múltiplas rotas de uma API.
- Coleta estatísticas detalhadas dos tempos de resposta.
- Armazena os resultados em um arquivo CSV.
- Suporta requisições GET e POST, com a possibilidade de incluir um corpo de requisição.

## Como usar

### 1. Configuração do Ambiente Virtual

É recomendável criar um ambiente virtual para isolar as dependências do projeto. Para isso, siga os passos abaixo:

#### Criar o ambiente virtual
No terminal, navegue até a pasta do projeto e execute o comando para criar o ambiente virtual:

```bash
python3 -m venv venv

source venv/bin/activate

```

#### Dependencias

```bash
pip install -r requirements.txt
```

#### Dependencias
para executar o projeto só renomear o arquivo chamado routes_example.json para routes.json

executar o comando 
```bash
python3 main.json
```