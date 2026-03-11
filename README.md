# Sistema-de-Gestión-de-Garaje
Esta apllicación de escritorio desarrollada en Python utilizando la librería **Tkinter**. El sistema permite el registro de vehículos en un garaje, siguiendo una **arquitectura modular** para separar la lógica de negocio de la interfaz de usuario.

## Características
* **Registro de Vehículos:** Captura de placa, marca y nombre del propietario.
* **Visualización en Tiempo Real:** Los datos se muestran inmediatamente en una tabla (`Treeview`).
* **Limpieza de Formulario:** Botón dedicado para vaciar los campos de entrada.
* **Arquitectura Modular:** Separación clara entre Modelos, Servicios y UI.

## Estructura del Proyecto

El proyecto sigue una estructura organizada por capas para facilitar el mantenimiento, detallada de la siguiente forma:

```text
garaje_app/
├── modelos/           # Definición de clases de datos (Vehiculo)
├── servicios/         # Lógica de negocio y gestión de datos
├── ui/                # Componentes de la interfaz gráfica (Tkinter)
├── main.py            # Punto de entrada de la aplicación
└── README.md          # Documentación del proyecto


### Fin aplicación
