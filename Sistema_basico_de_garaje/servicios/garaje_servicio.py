from modelos.vehiculo import Vehiculo
class GarajeServicio: #Servicio que gestiona los vehículos del garaje.

    def __init__(self): #Inicializa la lista de vehículos vacía.
        self._vehiculos = []

    def agregar_vehiculo(self, placa: str, marca: str, propietario: str) -> bool:
        """
        Agrega un nuevo vehículo si los datos son válidos.
        Retorna True si se agregó correctamente, False en caso contrario.
        """
        if not placa or not marca or not propietario: #Validación básica: ningún campo puede estar vacío.
            return False
        # Podríamos agregar validaciones adicionales (ej. placa única)
        vehiculo = Vehiculo(placa, marca, propietario)
        self._vehiculos.append(vehiculo)
        return True

    def obtener_vehiculos(self): #Devuelve la lista de vehículos registrados.
        return self._vehiculos.copy()