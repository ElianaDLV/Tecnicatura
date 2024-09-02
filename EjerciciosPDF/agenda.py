class Contacto:
    def __init__(self, telefono, email):
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Número de teléfono: {self.telefono} - Email: {self.email}"
    
    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"El atributo '{key}' no existe.")

contacto = Contacto('3512560055', 'elianadlv@gmail.com')
print(contacto)

# Modificar teléfono
contacto['telefono'] = '3512594444'
print(contacto)  

# Modificar email
contacto['email'] = 'nuevo.email@email.com'
print(contacto)  