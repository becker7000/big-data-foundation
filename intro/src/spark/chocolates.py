import sys
import matplotlib.pyplot as plt  # Importación de Matplotlib para la visualización

# Importación de SparkSession de PySpark para trabajar con DataFrames
from pyspark.sql import SparkSession

# Importamos la función 'count' de PySpark para contar elementos en una columna
from pyspark.sql.functions import count

# Punto de entrada del script, asegurando que se ejecute solo cuando el script sea llamado directamente
if __name__ == "__main__":

    # Verificamos que el número de argumentos proporcionados sea 2 (script y archivo CSV)
    if len(sys.argv) != 2:
        # Si no es correcto, mostramos un mensaje de uso adecuado
        print("Usage: mnmcount <file>", file=sys.stderr)
        # Salimos del script con un código de error
        sys.exit(-1)

    # Creamos la sesión de Spark, que es necesaria para trabajar con DataFrames en PySpark
    spark = (SparkSession
        .builder
        .appName("PythonMnMCount")  # Definimos el nombre de la aplicación de Spark
        .getOrCreate())  # Obtiene una sesión existente o crea una nueva si no existe

    # Obtenemos el nombre del archivo CSV que se pasa como argumento
    mnm_file = sys.argv[1]

    # Leemos el archivo CSV en un DataFrame de Spark
    mnm_df = (spark.read.format("csv")  # Especificamos que el archivo es de tipo CSV
        .option("header", "true")  # Indicamos que el archivo tiene una fila de encabezado
        .option("inferSchema", "true")  # Permitimos que Spark infiera el tipo de los datos automáticamente
        .load(mnm_file))  # Cargamos el archivo en un DataFrame

    # Mostramos las primeras 5 filas del DataFrame cargado para ver un resumen de los datos
    print("Primeras 5 filas del CSV: ")
    mnm_df.show(n=5, truncate=False)

    # Realizamos una agregación de los datos para contar la cantidad de cada color en cada estado
    count_mnm_df = (mnm_df.select("State", "Color", "Count")  # Seleccionamos las columnas relevantes
                    .groupBy("State", "Color")  # Agrupamos por 'State' (Estado) y 'Color'
                    .agg(count("Count")  # Usamos la función 'count' para contar los elementos de 'Count'
                    .alias("Total"))  # Renombramos la columna resultante como 'Total'
                    .orderBy("Total", ascending=False))  # Ordenamos por la cantidad total, de mayor a menor

    # Mostramos los primeros 60 resultados de la agregación
    print("Primeras 60 lineas de los resultados de agregación que cuenta la cantidad de cada color por estado")
    count_mnm_df.show(n=60, truncate=False)

    # Mostramos el número total de filas en el DataFrame resultante de la agregación
    print("Total Rows = %d" % (count_mnm_df.count()))

    # Filtramos los datos para obtener las estadísticas solo para California (CA)
    ca_count_mnm_df = (mnm_df.select("*")  # Seleccionamos todas las columnas
                       .where(mnm_df.State == 'CA')  # Filtramos solo las filas donde 'State' sea igual a 'CA' (California)
                       .groupBy("State", "Color")  # Agrupamos por 'State' y 'Color'
                       .agg(count("Count")  # Contamos los elementos en la columna 'Count'
                            .alias("Total"))  # Renombramos la columna agregada a 'Total'
                       .orderBy("Total", ascending=False))  # Ordenamos el resultado por 'Total', de mayor a menor

    # Mostramos los primeros 10 resultados de California
    print("Primero 10 resultados de la agregación para California: ")
    ca_count_mnm_df.show(n=10, truncate=False)

    # Convertimos el DataFrame de Spark en un DataFrame de Pandas para crear la gráfica
    pandas_df = count_mnm_df.toPandas()

    # Crear la gráfica de barras con Matplotlib
    plt.figure(figsize=(10, 6))

    # Se agrupan los resultados por estado, y luego se crea una barra para cada color en cada estado
    for state in pandas_df['State'].unique():
        # Filtramos los datos por estado
        state_data = pandas_df[pandas_df['State'] == state]
        # Dibujamos una barra para cada color
        plt.bar(state_data['Color'], state_data['Total'], label=state)

    # Configuramos las etiquetas y el título de la gráfica
    plt.xlabel('Color')
    plt.ylabel('Total Count')
    plt.title('Count of M&M Colors by State')
    plt.legend(title="States")

    # Configuramos la visualización
    plt.xticks(rotation=45)  # Rotamos las etiquetas del eje X para mejorar la legibilidad
    plt.tight_layout()  # Ajustamos la disposición para que todo encaje bien en la gráfica

    # Mostramos la gráfica
    plt.show()

"""
TX - Texas
NV - Nevada
CO - Colorado
OR - Oregon
WA - Washington
WY - Wyoming
CA - California
AZ - Arizona
NM - New Mexico
"""

"""
posibles requerimientos:
pip install numpy
pip install matplotlib
pip install setuptools
"""