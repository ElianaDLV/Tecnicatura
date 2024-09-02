import pytest
from barrasonido import BarraDeSonido

@pytest.fixture
def barra():
    # Se inicializa una barra de sonido para ser utilizada en las pruebas
    return BarraDeSonido("Samsung", "A500 TB", 299.99)

def test_ajustar_volumen(barra):
    barra.ajustarVolumen(10)
    assert barra.volumenActual == 60
    
    # Probar volumen máximo
    barra.ajustarVolumen(50)
    assert barra.volumenActual == 100

def test_cambiar_entrada(barra):
    barra.cambiarEntrada()
    assert barra.entradaActual == 'Bluetooth'
    barra.cambiarEntrada()
    assert barra.entradaActual == 'AUX'

def test_ajustar_modo_sonido(barra):
    barra.ajustarModoSonido('musica')
    assert barra.modoSonido == 'Bass Boost'

    barra.ajustarModoSonido('cine')
    assert barra.modoSonido == 'Surround'

    # Probar ajuste de un modo de sonido no especificado
    barra.ajustarModoSonido('deportes')
    assert barra.modoSonido == 'Standard'

def test_str(barra):
    # Probar la representación en cadena de la barra de sonido
    resultado = str(barra)
    assert "Samsung A500 TB" in resultado
    assert "Volumen=50" in resultado
    assert "Entrada=HDMI" in resultado
    assert "Modo de Sonido=Standard" in resultado