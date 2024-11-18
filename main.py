import tkinter as tk
from ajustes import * 
import lineal
import polinomical
import potencial
import exponencial
import cociente

root = tk.Tk()
root.title("Resolverdor de ajustes por minimos cuadrados") 
root.geometry("720x480")

label = tk.Label(root, text="Seleccione el tipo de ajuste que desea realizar")
label.pack(pady=20)

lineal_button = tk.Button(root, text="Ajuste Lineal", command=lineal.main)
lineal_button.pack(pady=10)
polinomical_button = tk.Button(root, text="Ajuste Polinómico", command=polinomical.main)
polinomical_button.pack(pady=10)
potential_button = tk.Button(root, text="Ajuste Potencial", command=potencial.main)
potential_button.pack(pady=10)
exponential_button = tk.Button(root, text="Ajuste Exponencial", command=exponencial.main)
exponential_button.pack(pady=10)
quotient_button = tk.Button(root, text="Ajuste Cociente", command=cociente.main)
quotient_button.pack(pady=10)

root.mainloop()