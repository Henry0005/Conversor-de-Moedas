# Conversor de Moedas

Este é um programa interativo em Python que converte valores entre diferentes moedas utilizando a API Open Exchange Rates. O programa suporta conversões entre USD (Dólar), BRL (Real) e Bitcoin.

## Funcionalidades

- **USD para BRL**: Converte valores de dólares americanos para reais brasileiros.
- **BRL para USD**: Converte valores de reais brasileiros para dólares americanos.
- **BRL para Bitcoin**: Converte valores de reais brasileiros para Bitcoin.
- **Bitcoin para BRL**: Converte valores de Bitcoin para reais brasileiros.
- **Bitcoin para USD**: Converte valores de Bitcoin para dólares americanos.
- **USD para Bitcoin**: Converte valores de dólares americanos para Bitcoin.

## Pré-requisitos

- Python 3.x instalado no sistema.
- Biblioteca `requests` instalada. Para instalar, use o comando:

```bash
pip install requests
```

- Chave de API válida do Open Exchange Rates. Substitua o valor de `API_KEY` no código pela sua chave de API.

## Como usar

1. Clone ou baixe este repositório em seu computador.
2. Certifique-se de que todos os pré-requisitos estão atendidos.
3. Execute o arquivo Python com o comando:

```bash
python ConversorDeMoedas.py
```

4. Escolha a operação desejada no menu interativo:

```
--- Conversor de Moedas ---
1. Converter USD para BRL
2. Converter BRL para USD
3. Converter BRL para Bitcoin
4. Converter Bitcoin para BRL
5. Converter Bitcoin para USD
6. Converter USD para Bitcoin
7. Sair
```

5. Siga as instruções para inserir os valores e veja os resultados exibidos no console.

## Exemplo de saída

Ao selecionar a opção **1** (USD para BRL):

```
Digite o valor em Dólares: 100
100 USD é igual a 500.00 BRL
```

## Personalização

Para adicionar mais moedas ou ajustar as conversões existentes, altere os parâmetros de `from_currency` e `to_currency` na função `convert_currency`.
