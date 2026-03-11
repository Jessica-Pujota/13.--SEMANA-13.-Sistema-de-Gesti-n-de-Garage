import tkinter as tk
from tkinter import ttk, messagebox
from servicios.garaje_servicio import GarajeServicio

class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Vehículos - Garaje")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Instancia del servicio
        self.servicio = GarajeServicio()

        # Variables para los campos de entrada
        self.placa_var = tk.StringVar()
        self.marca_var = tk.StringVar()
        self.propietario_var = tk.StringVar()

        self._crear_widgets()
        self._actualizar_tabla()

    def _crear_widgets(self):
        # Frame para el formulario de entrada
        frame_form = ttk.LabelFrame(self.root, text="Datos del vehículo", padding=10)
        frame_form.pack(fill="x", padx=10, pady=5)

        # Etiquetas y campos de entrada
        ttk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.placa_var, width=20).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.marca_var, width=20).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        ttk.Entry(frame_form, textvariable=self.propietario_var, width=20).grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        frame_botones = ttk.Frame(frame_form)
        frame_botones.grid(row=3, column=0, columnspan=2, pady=10)

        ttk.Button(frame_botones, text="Agregar vehículo", command=self._agregar_vehiculo).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Limpiar", command=self._limpiar_campos).pack(side="left", padx=5)

        # Frame para la tabla de vehículos
        frame_tabla = ttk.LabelFrame(self.root, text="Vehículos registrados", padding=10)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)

        # Crear Treeview con scrollbar
        columnas = ("Placa", "Marca", "Propietario")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=10)

        # Definir encabezados
        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")

        # Ajustar ancho de columnas
        self.tabla.column("Placa", width=100)
        self.tabla.column("Marca", width=150)
        self.tabla.column("Propietario", width=150)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _agregar_vehiculo(self): #Toma los datos del formulario y los envía al servicio para agregar el vehículo.
        placa = self.placa_var.get().strip()
        marca = self.marca_var.get().strip()
        propietario = self.propietario_var.get().strip()

        if self.servicio.agregar_vehiculo(placa, marca, propietario):
            messagebox.showinfo("Éxito", "Vehículo agregado correctamente.")
            self._actualizar_tabla()
            self._limpiar_campos()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    def _limpiar_campos(self): #Limpia los campos de entrada del formulario.
        self.placa_var.set("")
        self.marca_var.set("")
        self.propietario_var.set("")

    def _actualizar_tabla(self): #Limpia y vuelve a cargar los vehículos en la tabla.
        # Borrar todas las filas actuales
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Obtener vehículos del servicio
        vehiculos = self.servicio.obtener_vehiculos()

        # Insertar cada vehículo en la tabla
        for v in vehiculos:
            self.tabla.insert("", "end", values=v.to_tuple())