print(" ")
print("Alvaro Campechano 3W")
print(" ")
def mayor_de_tres(num1, num2, num3):
    """
    Devuelve el mayor de tres números.
    
    Args:
    num1 (float): Primer número.
    num2 (float): Segundo número.
    num3 (float): Tercer número.
    
    Returns:
    float: El número mayor de los tres.
    """
    return max(num1, num2, num3)

# Ejemplo de uso
numero1 = 5
numero2 = 10
numero3 = 7

mayor = mayor_de_tres(numero1, numero2, numero3)
print(f"El mayor de los tres números es: {mayor}")
