estado= ["SP", "RJ", "MG", "ES","OUTROS"]
valores= [67836.43,36678.66,29229.88,27165.48,19849.53]

soma_total =sum(valores)

for Estado, valor in enumerate(valores):
    percentual = valor / soma_total * 100
    print(f" {''.join(estado[Estado]):<6}: {percentual:.2f}%")