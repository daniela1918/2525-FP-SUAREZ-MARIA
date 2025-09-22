#Crea una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.
    Retorna el monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
# 1ra llamada: solo monto_total (usa el valor por defecto 10%)
monto1 = 200
descuento1 = calcular_descuento(monto1)
total_a_pagar1 = monto1 - descuento1

print("Primera compra:")
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Total a pagar: ${total_a_pagar1}\n")

# 2da llamada: monto_total + porcentaje_descuento especificado
monto2 = 500
descuento2 = calcular_descuento(monto2, 20)  # 20% de descuento
total_a_pagar2 = monto2 - descuento2

print("Segunda compra:")
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Total a pagar: ${total_a_pagar2}")
