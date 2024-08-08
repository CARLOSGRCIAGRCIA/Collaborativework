import tkinter as tk
from tkinter import ttk
from calculos import *
from graficos import *

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Vectores y Matrices")

        # Crear los widgets
        self.x1_label = ttk.Label(master, text="Componente x (vector 1):")
        self.x1_entry = ttk.Entry(master)
        self.y1_label = ttk.Label(master, text="Componente y (vector 1):")
        self.y1_entry = ttk.Entry(master)
        self.z1_label = ttk.Label(master, text="Componente z (vector 1):")
        self.z1_entry = ttk.Entry(master)
        self.x2_label = ttk.Label(master, text="Componente x (vector 2):")
        self.x2_entry = ttk.Entry(master)
        self.y2_label = ttk.Label(master, text="Componente y (vector 2):")
        self.y2_entry = ttk.Entry(master)
        self.z2_label = ttk.Label(master, text="Componente z (vector 2):")
        self.z2_entry = ttk.Entry(master)

        # Campos de entrada para la matriz 1
        self.a_entries_1 = []
        for i in range(1, 4):
            for j in range(1, 4):
                label = ttk.Label(master, text=f"a{i}{j} (matriz 1):")
                entry = ttk.Entry(master)
                label.grid(row=i-1, column=2*(j+1), padx=10, pady=5)
                entry.grid(row=i-1, column=2*(j+1)+1, padx=10, pady=5)
                self.a_entries_1.append(entry)

        # Campos de entrada para la matriz 2 (solo para producto de matrices)
        self.a_entries_2 = []
        for i in range(1, 4):
            for j in range(1, 4):
                label = ttk.Label(master, text=f"a{i}{j} (matriz 2):")
                entry = ttk.Entry(master)
                label.grid(row=i+2, column=2*(j+1), padx=10, pady=5)
                entry.grid(row=i+2, column=2*(j+1)+1, padx=10, pady=5)
                self.a_entries_2.append(entry)

        self.operacion_label = ttk.Label(master, text="Operación:")
        self.operacion_combobox = ttk.Combobox(master, values=["Sumar vectores",
                                                               "Restar vectores",
                                                               "Producto punto",
                                                               "Magnitud",
                                                               "Proyección",
                                                               "Producto matriz-vector",
                                                               "Producto matrices"])
        self.operacion_combobox.current(0)
        self.operacion_combobox.bind("<<ComboboxSelected>>", self.habilitar_entradas)

        self.resultado_label = ttk.Label(master, text="")
        self.calcular_button = ttk.Button(master, text="Calcular", command=self.calcular)

        # Ubicar los widgets en la ventana
        self.x1_label.grid(row=0, column=0, padx=10, pady=5)
        self.x1_entry.grid(row=0, column=1, padx=10, pady=5)
        self.y1_label.grid(row=1, column=0, padx=10, pady=5)
        self.y1_entry.grid(row=1, column=1, padx=10, pady=5)
        self.z1_label.grid(row=2, column=0, padx=10, pady=5)
        self.z1_entry.grid(row=2, column=1, padx=10, pady=5)
        self.x2_label.grid(row=0, column=2, padx=10, pady=5)
        self.x2_entry.grid(row=0, column=3, padx=10, pady=5)
        self.y2_label.grid(row=1, column=2, padx=10, pady=5)
        self.y2_entry.grid(row=1, column=3, padx=10, pady=5)
        self.z2_label.grid(row=2, column=2, padx=10, pady=5)
        self.z2_entry.grid(row=2, column=3, padx=10, pady=5)
        self.operacion_label.grid(row=3, column=0, padx=10, pady=5)
        self.operacion_combobox.grid(row=3, column=1, padx=10, pady=5)
        self.calcular_button.grid(row=4, column=0, columnspan=8, padx=10, pady=10)
        self.resultado_label.grid(row=5, column=0, columnspan=8, padx=10, pady=10)

    def habilitar_entradas(self, event):
        operacion = self.operacion_combobox.get()
        if operacion in ["Sumar vectores", "Restar vectores", "Producto punto", "Magnitud", "Proyección"]:
            self.x1_entry.config(state="normal")
            self.y1_entry.config(state="normal")
            self.z1_entry.config(state="normal")
            self.x2_entry.config(state="normal")
            self.y2_entry.config(state="normal")
            self.z2_entry.config(state="normal")
            for entry in self.a_entries_1:
                entry.config(state="disabled")
            for entry in self.a_entries_2:
                entry.config(state="disabled")
        elif operacion in ["Producto matriz-vector"]:
            self.x1_entry.config(state="normal")
            self.y1_entry.config(state="normal")
            self.z1_entry.config(state="normal")
            self.x2_entry.config(state="disabled")
            self.y2_entry.config(state="disabled")
            self.z2_entry.config(state="disabled")
            for entry in self.a_entries_1:
                entry.config(state="normal")
            for entry in self.a_entries_2:
                entry.config(state="disabled")
        elif operacion in ["Producto matrices"]:
            self.x1_entry.config(state="disabled")
            self.y1_entry.config(state="disabled")
            self.z1_entry.config(state="disabled")
            self.x2_entry.config(state="disabled")
            self.y2_entry.config(state="disabled")
            self.z2_entry.config(state="disabled")
            for entry in self.a_entries_1:
                entry.config(state="normal")
            for entry in self.a_entries_2:
                entry.config(state="normal")

    def calcular(self):
        operacion = self.operacion_combobox.get()
        self.habilitar_entradas(None)

        if operacion == "Sumar vectores":
            vector1 = leer_vector(self.x1_entry.get(), self.y1_entry.get(), self.z1_entry.get())
            vector2 = leer_vector(self.x2_entry.get(), self.y2_entry.get(), self.z2_entry.get())
            resultado = sumar_vectores(vector1, vector2)
            self.mostrar_resultado(resultado)
            graficar_vector(vector1)
            graficar_vector(vector2)
            graficar_vector(resultado)
        elif operacion == "Restar vectores":
            vector1 = leer_vector(self.x1_entry.get(), self.y1_entry.get(), self.z1_entry.get())
            vector2 = leer_vector(self.x2_entry.get(), self.y2_entry.get(), self.z2_entry.get())
            resultado = restar_vectores(vector1, vector2)
            self.mostrar_resultado(resultado)
            graficar_vector(vector1)
            graficar_vector(vector2)
            graficar_vector(resultado)
        elif operacion == "Producto punto":
            vector1 = leer_vector(self.x1_entry.get(), self.y1_entry.get(), self.z1_entry.get())
            vector2 = leer_vector(self.x2_entry.get(), self.y2_entry.get(), self.z2_entry.get())
            resultado = producto_punto(vector1, vector2)
            self.mostrar_resultado(resultado)
            graficar_vector(vector1)
            graficar_vector(vector2)
        elif operacion == "Magnitud":
            vector = leer_vector(self.x1_entry.get(), self.y1_entry.get(), self.z1_entry.get())
            resultado = magnitud(vector)
            self.mostrar_resultado(resultado)
            graficar_vector(vector)
        elif operacion == "Proyección":
            vector1 = leer_vector(self.x1_entry.get(), self.y1_entry.get(), self.z1_entry.get())
            vector2 = leer_vector(self.x2_entry.get(), self.y2_entry.get(), self.z2_entry.get())
            resultado = proyeccion(vector1, vector2)
            self.mostrar_resultado(resultado)
            graficar_vector(vector1)
            graficar_vector(vector2)
            graficar_vector(resultado)
        elif operacion == "Producto matriz-vector":
            matriz = leer_matriz(*[entry.get() for entry in self.a_entries_1])
            vector = leer_vector(self.x1_entry.get(), self.y1_entry.get(), self.z1_entry.get())
            resultado = producto_matriz_vector(matriz, vector)
            self.mostrar_resultado(resultado)
            graficar_matriz(matriz)
            graficar_vector(vector)
            graficar_vector(resultado)
        elif operacion == "Producto matrices":
            matriz1 = leer_matriz(*[entry.get() for entry in self.a_entries_1])
            matriz2 = leer_matriz(*[entry.get() for entry in self.a_entries_2])
            resultado = producto_matrices(matriz1, matriz2)
            self.mostrar_resultado(resultado)
            graficar_matriz(matriz1)
            graficar_matriz(matriz2)
            graficar_matriz(resultado)

    def mostrar_resultado(self, resultado):
        if isinstance(resultado, np.ndarray):
            if resultado.ndim == 1:
                self.resultado_label.config(text=f"[{resultado[0]:.2f}, {resultado[1]:.2f}, {resultado[2]:.2f}]")
            else:
                self.resultado_label.config(text=f"{resultado}")
        else:
            self.resultado_label.config(text=f"{resultado:.2f}")

root = tk.Tk()
app = CalculadoraGUI(root)
root.mainloop()