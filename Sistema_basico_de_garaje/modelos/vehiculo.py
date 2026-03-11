class Vehiculo: #Representa un vehículo con su información básica.

    def __init__(self, placa: str, marca: str, propietario: str): #Inicializa un nuevo vehículo con su placa, marca y propietario.
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self): #Devuelve una representación en cadena del vehículo, mostrando su placa, marca y propietario.
        return f"{self.placa} - {self.marca} - {self.propietario}"

    def to_tuple(self): #Devuelve una tupla con los datos para insertar en la tabla de la UI
        return (self.placa, self.marca, self.propietario)