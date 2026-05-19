import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

output = Path('output')
output.mkdir(exist_ok=True)

data = [
    ['2026-01', 'Notebook', 'Eletrônicos', 12, 3500],
    ['2026-01', 'Mouse', 'Eletrônicos', 45, 79],
    ['2026-01', 'Cadeira', 'Móveis', 9, 899],
    ['2026-02', 'Notebook', 'Eletrônicos', 10, 3600],
    ['2026-02', 'Monitor', 'Eletrônicos', 14, 1150],
    ['2026-02', 'Mesa', 'Móveis', 7, 1220],
    ['2026-03', 'Notebook', 'Eletrônicos', 15, 3420],
    ['2026-03', 'Teclado', 'Eletrônicos', 28, 160],
    ['2026-03', 'Cadeira', 'Móveis', 11, 950],
    ['2026-04', 'Mesa', 'Móveis', 10, 1250],
    ['2026-04', 'Monitor', 'Eletrônicos', 17, 1090],
    ['2026-04', 'Mouse', 'Eletrônicos', 62, 82],
]

df = pd.DataFrame(data, columns=['mes', 'produto', 'categoria', 'quantidade', 'preco_unitario'])
df['faturamento'] = df['quantidade'] * df['preco_unitario']
mensal = df.groupby('mes', as_index=False)['faturamento'].sum()
categoria = df.groupby('categoria', as_index=False).agg(
    faturamento=('faturamento', 'sum'),
    quantidade=('quantidade', 'sum')
)
categoria['ticket_medio_item'] = (categoria['faturamento'] / categoria['quantidade']).round(2)

df.to_csv(output / 'vendas_tratadas.csv', index=False)
mensal.to_csv(output / 'faturamento_mensal.csv', index=False)
categoria.to_csv(output / 'resumo_categoria.csv', index=False)

plt.figure(figsize=(9, 5))
plt.plot(mensal['mes'], mensal['faturamento'], marker='o', linewidth=2.5)
plt.title('Faturamento Mensal')
plt.xlabel('Mês')
plt.ylabel('Faturamento')
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(output / 'faturamento_mensal.png', dpi=180)
