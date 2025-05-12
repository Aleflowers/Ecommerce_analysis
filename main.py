import pandas as pd
# Carga del archivo Excel
df = pd.read_csv("data/Online_Retail.csv")

# Vista rápida de los datos
print(df.head())
print(df.info())

# Elimina filas con CustomerID nulo
df = df.dropna(subset=['CustomerID'])

# Elimina transacciones con cantidades o precios negativos o cero
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Crea columna de total por línea
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


# Convierte la columna de fecha si es necesario
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)

import matplotlib.pyplot as plt
import seaborn as sns

# Agrupa por país
ventas_pais = df[df['Country'] != 'United Kingdom'].groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

# Gráfico
plt.figure(figsize=(10,6))
sns.barplot(x=ventas_pais.values, y=ventas_pais.index, palette="viridis")
plt.title("Ventas totales por país (Top 10, sin Reino Unido)")
plt.xlabel("Ventas totales")
plt.ylabel("País")
plt.show()
