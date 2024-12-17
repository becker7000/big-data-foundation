
Ajustar variables de entorno temporalmente:
```shell
set JAVA_HOME=C:\Program Files\Java\jdk-8
set PATH=%JAVA_HOME%\bin;%PATH%
```

Comprobar:
```shell
echo %JAVA_HOME%
java -version
```


> ## Ejemplos extras:

Modelo embebido:

```js
{
  "_id": 1,
  "fecha": "2024-12-15",
  "cliente": "Juan Pérez",
  "productos": [
    { "producto_id": 101, "nombre": "Camiseta", "precio": 15.00 },
    { "producto_id": 102, "nombre": "Pantalón", "precio": 30.00 }
  ]
}
```

Modelo referenciado:

```js
{
  "_id": 1,
  "nombre": "Juan Pérez",
  "correo": "juanperez@email.com"
}
```

```js
{
  "_id": 101,
  "nombre": "Camiseta",
  "precio": 15.00
}
```

```js
{
  "_id": 5001,
  "fecha": "2024-12-15",
  "cliente_id": 1,
  "productos": [
    { "producto_id": 101, "cantidad": 2 }
  ]
}
```


> ## Solución del ejercicio:

Modelo embebido: 

```js
{
  "_id": "alquiler123",
  "usuario": {
    "id": "usuario001",
    "nombre": "Juan Pérez",
    "genero": "M",
    "edad": 30
  },
  "bicicleta": {
    "id": "bici001",
    "ubicacion": "Estación A"
  },
  "estacion_retiro": {
    "id": "estacion001",
    "nombre": "Estación A",
    "ubicacion": {
      "latitud": 19.4326,
      "longitud": -99.1332
    }
  },
  "estacion_arribo": {
    "id": "estacion002",
    "nombre": "Estación B",
    "ubicacion": {
      "latitud": 19.4336,
      "longitud": -99.1423
    }
  },
  "fecha_retiro": "2024-10-01T10:00:00Z",
  "fecha_arribo": "2024-10-01T10:30:00Z"
}

```

Modelo referenciado: 

Coleccion usuarios:

```js
{
  "_id": "usuario001",
  "nombre": "Juan Pérez",
  "genero": "M",
  "edad": 30
}
```

Colección estaciones:

```js
{
  "_id": "estacion001",
  "nombre": "Estación A",
  "ubicacion": {
    "latitud": 19.4326,
    "longitud": -99.1332
  }
}
```

```js
{
  "_id": "bici001",
  "estacion_id": "estacion001"
}
```

Colección alquileres:

```js
{
  "_id": "alquiler123",
  "usuario_id": "usuario001",
  "bicicleta_id": "bici001",
  "estacion_retiro_id": "estacion001",
  "estacion_arribo_id": "estacion002",
  "fecha_retiro": "2024-10-01T10:00:00Z",
  "fecha_arribo": "2024-10-01T10:30:00Z"
}
```