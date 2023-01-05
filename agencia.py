#CREACION DE UNA CLASE QUE CONTENGA UN METODO Y SU OBJETO IMPRESO EJECUTANDO EL METODO __str__
class Agencia:
    nombre   = str
    modelo   = int
    año      = str
    costo  = str
    
    def __init__(self, nombre, modelo, año, costo):
        self.nombre  = nombre
        self.modelo  = modelo
        self.año     = año
        self.costo   = costo

    def __str__(self):
        return f"El señor {self.nombre} adquirio su auto {self.modelo} el dia 25 de agosto del año {self.año} y el precio fue de:{self.costo} "
    
agencia1 = Agencia("Armando", "Mazda", 2018, 15000)

print(agencia1)
