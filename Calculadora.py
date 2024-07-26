import sys

def obtener_opcion_valida():
    while True:
        try:
            opcion = int(input("Introduce el número de la opción: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, introduce un número.")

def obtener_numero_valido(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            verificar_numero_negativo(num)
            return num
        except ValueError:
            print("Error: Entrada no válida. Por favor, introduce un número.")
        except Exception as e:
            print(e)

def verificar_numero_negativo(num):
    if num < 0:
        raise Exception("Error: No se permiten números negativos.")

def main():
    print("Calculadora Simple")

    while True:
        print("Selecciona una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = obtener_opcion_valida()

        if opcion == 5:
            print("Saliendo del programa...")
            sys.exit()

        num1 = obtener_numero_valido("Introduce el primer número: ")
        num2 = obtener_numero_valido("Introduce el segundo número: ")

        if opcion == 1:
            print(f"Resultado de la suma: {int(num1 + num2)}")
        elif opcion == 2:
            print(f"Resultado de la resta: {int(num1 - num2)}")
        elif opcion == 3:
            print(f"Resultado de la multiplicación: {int(num1 * num2)}")
        elif opcion == 4:
            if num2 != 0:
                print(f"Resultado de la división: {int(num1 / num2)}")
            else:
                print("Error: División por cero no permitida.")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
