# test_script.py
"""
Este es un archivo de prueba para configurar y verificar VS Code con Python.
Incluye funciones básicas, estructuras de control, manejo de listas y salida en consola.
"""

import random  # Probar importaciones y coloreado de palabras clave
import sys  # Librería estándar para verificar imports múltiples

def generate_numbers(count):
    """
    Genera una lista de números aleatorios.

    Args:
        count (int): Cantidad de números a generar.

    Returns:
        list: Lista de números enteros aleatorios.
    """
    return [random.randint(1, 100) for _ in range(count)]

def display_numbers(numbers):
    """
    Imprime cada número de una lista junto con su índice.

    Args:
        numbers (list): Lista de números a imprimir.
    """
    for index, number in enumerate(numbers):
        print(f"Número {index + 1}: {number}")

def main():
    """
    Función principal para probar la ejecución del script.
    """
    print("=== Bienvenido al script de prueba de Python ===")

    # Probar entrada del usuario
    try:
        count = int(input("¿Cuántos números aleatorios quieres generar? (1-10): "))
        if count < 1 or count > 10:
            print("Por favor, ingresa un número entre 1 y 10.")
            sys.exit(1)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        sys.exit(1)

    # Generar y mostrar números
    numbers = generate_numbers(count)
    display_numbers(numbers)

    # Probar manejo de listas
    print(f"El número más alto es: {max(numbers)}")
    print(f"El número más bajo es: {min(numbers)}")
    print(f"Promedio de los números: {sum(numbers) / len(numbers):.2f}")

    # Probar depuración con un bloque condicional
    if sum(numbers) > 200:
        print("¡La suma de los números supera 200!")
    else:
        print("La suma de los números no supera 200.")

if __name__ == "__main__":
    main()
