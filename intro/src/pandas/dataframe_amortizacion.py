import pandas as pd

# Crear un DataFrame con una tabla de amortización de pagos
data = {
    'Número de pago': [1, 2, 3, 4, 5],
    'Fecha de pago': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'Pago total': [1000, 1000, 1000, 1000, 1000],
    'Intereses': [50, 45, 40, 35, 30],
    'Amortización': [950, 955, 960, 965, 970],
    'Saldo restante': [9500, 8545, 7585, 6620, 5645]
}

# Convertir el diccionario a un DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame completo
print("Tabla de amortización completa:")
print(df)

# Selección de una columna (por ejemplo, 'Pago total')
print("\nSelección de la columna 'Pago total':")
print(df['Pago total'])

# Selección de una fila (por ejemplo, la fila con índice 2, es decir, el tercer pago)
print("\nSelección de la fila con índice 2 (tercer pago):")
print(df.iloc[2])

# Filtrado de datos (por ejemplo, seleccionar pagos donde la amortización es mayor que 960)
print("\nFiltrado de pagos donde la amortización es mayor que 960:")
filtered_df = df[df['Amortización'] > 960]
print(filtered_df)
