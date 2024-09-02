class ControlVolumen:
    def __init__(self):
        self.__volumen = 5  # Nivel medio de volumen al iniciar (5 de 10)

    def ajustarVolumen(self, cambio):
        nuevoVolumen = self.__volumen + cambio
        if 1 <= nuevoVolumen <= 10:
            self.__volumen = nuevoVolumen
            print(f"El volumen ha sido ajustado a {self.__volumen}.")
        else:
            print("El volumen no puede superar los límites (1 a 10).")

    def __str__(self):
        return f"El volumen actual es {self.__volumen}."

# APLICACIÓN DE CONSOLA
def main():
    control = ControlVolumen()

    while True:
        print("\nOpciones:")
        print("1. Subir el volumen")
        print("2. Bajar el volumen")
        print("3. Mostrar volumen actual")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            control.ajustarVolumen(1)

        elif opcion == "2":
            control.ajustarVolumen(-1)

        elif opcion == "3":
            print(control)  

        elif opcion == "4":
            print(control)
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()