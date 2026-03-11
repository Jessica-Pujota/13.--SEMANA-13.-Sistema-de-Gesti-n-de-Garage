class Vehiculo: #Representa un vehículo con su información básica.

    def __init__(self, placa: str, marca: str, propietario: str):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self):
        return f"{self.placa} - {self.marca} - {self.propietario}"

    def to_tuple(self): #Devuelve una tupla con los datos para insertar en la tabla de la UI
        return (self.placa, self.marca, self.propietario)