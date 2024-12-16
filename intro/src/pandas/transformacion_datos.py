import pandas as pd
import numpy as np

# Crear un DataFrame con datos de ventas
data = {
    'Producto': ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartwatch', 'Smartphone', None],
    'Fecha de venta': ['2024-01-01', '2024-02-01', '2024-03-01', None, '2024-05-01', '2024-06-01', '2024-07-01'],
    'Precio': [1200, 800, 450, 1200, 200, 850, np.nan],
    'Unidades vendidas': [5, 10, 7, 5, 15, None, 10]
}

# Crear el DataFrame
df = pd.DataFrame(data)

print("Datos originales:")
print(df)

# 1. Eliminar filas con valores faltantes
df_limpio = df.dropna()

print("\nDespués de eliminar filas con valores faltantes:")
print(df_limpio)

# 2. Rellenar valores faltantes en la columna 'Precio' con el valor medio de la columna
df['Precio'] = df['Precio'].fillna(df['Precio'].mean())

# 3. Convertir la columna 'Fecha de venta' al formato datetime
df['Fecha de venta'] = pd.to_datetime(df['Fecha de venta'], errors='coerce')

# 4. Eliminar duplicados, en este caso, por las columnas 'Producto' y 'Fecha de venta'
df_sin_duplicados = df.drop_duplicates(subset=['Producto', 'Fecha de venta'])

# 5. Transformar la columna 'Unidades vendidas' a números enteros
df['Unidades vendidas'] = df['Unidades vendidas'].fillna(0).astype(int)

# 6. Crear una nueva columna con el total de ventas por producto (Precio * Unidades vendidas)
df['Total ventas'] = df['Precio'] * df['Unidades vendidas']

# Mostrar el DataFrame limpio y transformado
print("\nDespués de limpiar, transformar y generar nuevas columnas:")
print(df)

# Mostrar los productos con el mayor total de ventas
productos_top_ventas = df[['Producto', 'Total ventas']].sort_values(by='Total ventas', ascending=False)
print("\nProductos con mayor total de ventas:")
print(productos_top_ventas)