#REALIZAR UNA HERENCIA EN UNA CLASE QUE CONTENGA VARIOS OBJETOS (2) Y OBJETOS DENTRO DE OBJETOS (2)
from vehiculo import Vehiculo
if __name__ == "__main__":

    print("Vehiculo:")
    vehiculo1 = Vehiculo(1, "Cristiano", 37, "cristino07@gmail.com", "0989565657")
    print(vars(vehiculo1))
