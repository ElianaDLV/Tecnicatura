class BarraDeSonido:
    def __init__(self, marca, modelo, precio):
        self._marca = marca
        self._modelo = modelo
        self._precio = precio
        self._volumenActual = 50
        self._entradaActual = 'HDMI'
        self._modoSonido = 'Standard'

    # Propiedades y setters
    @property
    def marca(self):
        return self._marca

    @property
    def modelo(self):
        return self._modelo

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevoPrecio):
        if nuevoPrecio > 0:
            self._precio = nuevoPrecio
        else:
            raise ValueError("El precio debe ser un valor positivo.")

    @property
    def volumenActual(self):
        return self._volumenActual

    @volumenActual.setter
    def volumenActual(self, volumen):
        if 0 <= volumen <= 100:
            self._volumenActual = volumen
        else:
            raise ValueError("El volumen debe estar entre 0 y 100.")

    @property
    def entradaActual(self):
        return self._entradaActual

    @entradaActual.setter
    def entradaActual(self, entrada):
        entradasValidas = ['HDMI', 'Bluetooth', 'AUX', 'Optical']
        if entrada in entradasValidas:
            self._entradaActual = entrada
        else:
            raise ValueError("Entrada no válida.")

    @property
    def modoSonido(self):
        return self._modoSonido

    @modoSonido.setter
    def modoSonido(self, modo):
        modosValidos = ['Standard', 'Bass Boost', 'Surround', 'Vocal Clarity', 'Dynamic']
        if modo in modosValidos:
            self._modoSonido = modo
        else:
            raise ValueError("Modo de sonido no válido.")

    # Métodos
    def ajustarVolumen(self, cambio):
        try:
            cambio = int(cambio)  # Asegura que el cambio sea un entero
        except ValueError:
            raise ValueError("El cambio debe ser un número entero.")

        nuevoVolumen = self._volumenActual + cambio
        if nuevoVolumen > 100:
            nuevoVolumen = 100
        elif nuevoVolumen < 0:
            nuevoVolumen = 0

        self.volumenActual = nuevoVolumen
        return self._volumenActual

    def cambiarEntrada(self):
        entradas = ['HDMI', 'Bluetooth', 'AUX', 'Optical']
        indiceActual = entradas.index(self._entradaActual)
        self.entradaActual = entradas[(indiceActual + 1) % len(entradas)]
        return self._entradaActual

    def ajustarModoSonido(self, tipoContenido):
        modos = {
            'musica': 'Bass Boost',
            'cine': 'Surround',
            'voz': 'Vocal Clarity',
            'juegos': 'Dynamic'
        }
        self.modoSonido = modos.get(tipoContenido, 'Standard')
        return self._modoSonido

    def __str__(self):
        return (f"Barra de Sonido {self.marca} {self.modelo} - Precio: ${self.precio}\n"
                f"Volumen={self.volumenActual}, Entrada={self.entradaActual}, Modo de Sonido={self.modoSonido}")

def mostrarMenu():
    print("\n--- Menú de Barra de Sonido ---")
    print("🔊 1. Ajustar Volumen")
    print("🔄 2. Cambiar Entrada")
    print("🎵 3. Ajustar Modo de Sonido")
    print("📋 4. Mostrar Estado Actual")
    print("🚪 5. Salir")

def main():
    barraSonido = BarraDeSonido("Samsung", "A500 TB", 299.99)
    while True:
        mostrarMenu()
        opcion = input("Elige una opción (1-5): ").strip()
        
        if opcion == '1':
            cambio = input("Ingresa el cambio en el volumen (+ para subir, - para bajar): ").strip()
            try:
                nuevoVolumen = barraSonido.ajustarVolumen(cambio)
                print(f"🔊 Volumen ajustado a: {nuevoVolumen}")
            except ValueError as e:
                print(f"❌ Error: {e}")
        
        elif opcion == '2':
            nuevaEntrada = barraSonido.cambiarEntrada()
            print(f"🔄 Entrada cambiada a: {nuevaEntrada}")
        
        elif opcion == '3':
            tipoContenido = input("Ingresa el tipo de contenido (musica, cine, voz, juegos): ").strip().lower()
            if tipoContenido in ['musica', 'cine', 'voz', 'juegos']:
                nuevoModo = barraSonido.ajustarModoSonido(tipoContenido)
                print(f"🎵 Modo de sonido ajustado a: {nuevoModo}")
            else:
                print("❌ Tipo de contenido no válido. Usa 'musica', 'cine', 'voz', o 'juegos'.")
        
        elif opcion == '4':
            print(f"📋 {barraSonido}")
        
        elif opcion == '5':
            print("🚪 Saliendo del programa...")
            break
        
        else:
            print("❌ Opción no válida. Por favor, elige una opción entre 1 y 6.")

if __name__ == "__main__":
    main()