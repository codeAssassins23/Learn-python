datos = {"nombre": "Alice", "edad": 30, "ciudad": "Ejemplo"}
print(type(datos))

# Obtener una vista de los pares clave-valor en el diccionario
vista = datos.items()
print(type(vista))
# Iterar a través de la vista de pares clave-valor
for clave, valor in vista:
    print(f"Clave: {clave}, Valor: {valor}")

# Output:
# Clave: nombre, Valor: Alice
# Clave: edad, Valor: 30
# Clave: ciudad, Valor: Ejemplo
datos = {"nombre": "Alice", "edad": 30, "ciudad": "Ejemplo"}

# Eliminar la clave "edad" y obtener su valor
valor = datos.pop("edad")
print(valor)
print(datos)


######
diccionario = {"nombre": "victor", "estado": "activo"}

otro_diccionario = {"nombre": 50, "ciudad": "tarapoto"}
print(otro_diccionario)

diccionario.update({"nombre": 50})

print(diccionario)
