# Proyecto: Barra de Sonido - Programación Orientada a Objetos (POO) y TDD

## 🎯 Objetivo

Diseñar y desarrollar una clase en Python que represente una barra de sonido, aplicando TDD (Desarrollo Guiado por Pruebas), conceptos de Programación Orientada a Objetos (POO), y asegurando una estructura de código limpia y mantenible.

## ⌨️​ Descripción del Código

La clase `BarraDeSonido` simula una barra de sonido con los siguientes comportamientos clave:

1. **Ajustar Volumen**: Permite aumentar o disminuir el volumen dentro de un rango de 0 a 100.
2. **Cambiar Entrada**: Cambia entre diferentes entradas de audio (`HDMI`, `Bluetooth`, `AUX`, `Optical`).
3. **Ajustar Modo de Sonido**: Ajusta el modo de sonido según el tipo de contenido (Música, Cine, Voz, Juegos).

Método estándar implementado:
- **`__str__`**: Devuelve una representación en cadena del estado actual de la barra de sonido.

## 💡 ​Principios Aplicados

- **Abstracción**: La clase `BarraDeSonido` abstrae los detalles internos de la manipulación del volumen, entradas y modos de sonido, proporcionando métodos claros para la interacción del usuario.
- **Encapsulamiento**: Los atributos como `__marca`, `__modelo`, `__precio`, `__volumenActual`, `__entradaActual` y `__modoSonido` están encapsulados dentro de la clase y solo son accesibles a través de métodos y propiedades que validan y controlan el acceso.

## 👩‍💻​ Desarrollo Guiado por Pruebas (TDD)

1. **Pruebas Unitarias**: Las pruebas se escribieron primero en el archivo `test_barrasonido.py`.
   - Por ejemplo, `test_ajustar_volumen` verifica que el método `ajustarVolumen` ajusta el volumen correctamente sin exceder los límites permitidos.
   - `test_cambiar_entrada` prueba que la barra cambia entre diferentes entradas de manera cíclica.
   - `test_ajustar_modo_sonido` asegura que los modos de sonido se ajustan correctamente según el tipo de contenido.
2. **Implementación de la Clase**: La clase `BarraDeSonido` en `barrasonido.py` se desarrolló para pasar todas las pruebas.
3. **Refactorización**: Después de cada prueba, el código fue refactorizado para mejorar la eficiencia y mantener un código limpio y fácil de entender.

## ​💻​ Base de Datos

La base de datos se diseñó para almacenar información sobre las barras de sonido disponibles.

- **Diseño**: Incluye la sentencia `CREATE TABLE` para la barra de sonido.
- **Datos de Ejemplo**: Incluye 10 sentencias `INSERT` con datos de prueba.
- **Consultas**: Contiene 5 consultas `SELECT` para extraer información.

## ⚠️​ Instalación y Ejecución

1. **Ejecutar el Código Principal**:
   ```bash
   python barrasonido.py
   ```

2. **Ejecutar las Pruebas Unitarias**:
   ```bash
   python -m pytest test-barradesonido.py
   ```

## 📷​ Video de Presentación

[Ver Video de Presentación](https://youtu.be/BADQmpgejzo)
