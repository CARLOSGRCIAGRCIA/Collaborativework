import tkinter as tk
from tkinter import ttk
from interfaz import CalculadoraGUI

root = tk.Tk()
root.title("Calculadora de Vectores y Matrices")

x_label = ttk.Label(root, text="Componente x:")
x_entry = ttk.Entry(root)
y_label = ttk.Label(root, text="Componente y:")
y_entry = ttk.Entry(root)
z_label = ttk.Label(root, text="Componente z:")
z_entry = ttk.Entry(root)

a_entries = []
for i in range(1, 4):
    for j in range(1, 4):
        label = ttk.Label(root, text=f"a{i}{j}:")
        entry = ttk.Entry(root)
        label.grid(row=i-1, column=2*(j+1), padx=10, pady=5)
        entry.grid(row=i-1, column=2*(j+1)+1, padx=10, pady=5)
        a_entries.append(entry)

operacion_label = ttk.Label(root, text="Operación:")
operacion_combobox = ttk.Combobox(root, values=["Sumar vectores", "Restar vectores", "Producto punto", "Magnitud", "Proyección", "Producto matriz-vector", "Producto matrices"])
operacion_combobox.current(0)

resultado_label = ttk.Label(root, text="")
calcular_button = ttk.Button(root, text="Calcular", command=lambda: CalculadoraGUI(operacion_combobox.get(), x_entry, y_entry, z_entry, a_entries, resultado_label))

x_label.grid(row=0, column=0, padx=10, pady=5)
x_entry.grid(row=0, column=1, padx=10, pady=5)
y_label.grid(row=1, column=0, padx=10, pady=5)
y_entry.grid(row=1, column=1, padx=10, pady=5)
z_label.grid(row=2, column=0, padx=10, pady=5)
z_entry.grid(row=2, column=1, padx=10, pady=5)

operacion_label.grid(row=3, column=0, padx=10, pady=5)
operacion_combobox.grid(row=3, column=1, padx=10, pady=5)

calcular_button.grid(row=4, column=0, columnspan=8, padx=10, pady=10)
resultado_label.grid(row=5, column=0, columnspan=8, padx=10, pady=10)

app = CalculadoraGUI(root)

