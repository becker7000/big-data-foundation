import pandas as pd

# Cargar un conjunto de datos en un DataFrame
data = {'Nombre': ['Laura', 'Carlos', 'Arely'],
        'Edad': [27, 24, 29],
        'Ciudad': ['CDMX', 'Monterrey', 'Guadalajara']}

df = pd.DataFrame(data)
print(df)
