class Carta:
    palos = ['Espada', 'Basto', 'Oro', 'Copa']
    valores = ['1','2','3','4','5','6','7','8','9','10','11','12']

    @property
    def palo(self):
        return self.__palo

    @property
    def valor(self):
        return self.__valor

    def __init__(self, palo, valor):
        if palo in Carta.palos and valor in Carta.valores:
            self.__palo = palo
            self.__valor = valor
        else:
            raise ValueError("Palo o valor no válido")
        
    def __str__(self) -> str:
        return f"{self.__valor} de {self.__palo}"
    
    def __getitem__(self, key):
        return getattr(self, key)

carta = Carta('Oro', '12')
print(carta) 

print(carta['palo'])
print(carta['valor'])