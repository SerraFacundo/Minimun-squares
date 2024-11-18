import tkinter as tk
from ajustes import ajuste_exponencial
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

import matplotlib.pyplot as plt

def main():
    global x_entry, y_entry, window
    window = tk.Tk()
    window.title("Ajuste Exponencial")
    window.geometry("720x480")
    
    label = tk.Label(window, text="Ingrese los valores de x y y")
    label.pack(pady=20)
    
    x_entry = tk.Entry(window)
    x_entry.pack(pady=10)
    y_entry = tk.Entry(window)
    y_entry.pack(pady=10)
    
    accept = tk.Button(window, text="Aceptar", command=ajustar)
    accept.pack(pady=10)
    
def ajustar():
    x = list(map(float, x_entry.get().split(",")))
    y = list(map(float, y_entry.get().split(",")))
    a, b, bondad = ajuste_exponencial(x, y)
    
    label_result = tk.Label(window, text=f"La ecuación de la curva es: y = {a} * e^({b} * x)")
    label_result.pack(pady=20)
    
    # Crear la figura de Matplotlib
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Datos')
    x_line = np.linspace(min(x), max(x), 100)
    y_line = a * np.exp(b * x_line)
    ax.plot(x_line, y_line, color='red', label='Ajuste Exponencial')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    
    bondad_label = tk.Label(window, text=f"El coeficiente de bondad es: {bondad}")
    bondad_label.pack(pady=10)
    
    # Integrar la figura en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

if __name__ == "__main__":
    main()
    tk.mainloop()