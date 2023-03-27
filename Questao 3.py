
## NÃO CONSEGUIR RECEBER O ARQUIVO, MAS RESOLVERIAMOS ASSIM:
import json

# ler os dados do arquivo JSON
with open("faturamento.json", "r") as f:
    dados = json.load(f)

# calcular o faturamento medio mensal
faturamento_mensal = sum(registro["valor"] for registro in dados) / len(dados)

# cria as variaveis para o menor e maior valor de faturamento
menor_faturamento = float("inf")
maior_faturamento = float("-inf")

# inicializa a variavel para o numero de dias com faturamento acima da media mensal
dias_acima_da_media = 0

# analisa a lista de dados e atualiza as variaveis conforme necessário
for registro in dados:
    # limpa os registros sem valor de faturamento para nao afetar a media
    if registro["valor"] is None:
        continue

    # regista os menor e o maior valor de faturamento atualizado
    if registro["valor"] < menor_faturamento:
        menor_faturamento = registro["valor"]
    if registro["valor"] > maior_faturamento:
        maior_faturamento = registro["valor"]

    # conta o numero de dias com faturamento acima da média mensal
    if registro["valor"] > faturamento_mensal:
        dias_acima_da_media += 1

# imprime os resultados
print(f"Menor valor de faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

# Imprime os resultados
print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_media}")

