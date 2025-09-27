#Crea un diccionario llamado informacion_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
informacion_personal= {
    "nombre":"Daniela", "edad": 25,"ciudad":"Cuenca", "profesion": "Biloga Marina"
}
print("Primer Diccionario")
print("informacion_personal")

#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"] = "Macas"
print("\nDespues de cambiar la ciudad")
print(informacion_personal)

#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["profesion"] = "Medico Veterinaria"
print("\nDespues de cambiar la profesion")
print(informacion_personal)

#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992706946"
print("\nDespues de agregar el  telefono:")
print(informacion_personal)

#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal["edad"]
print("\nDespues de eliminar la edad:")
print(informacion_personal)



