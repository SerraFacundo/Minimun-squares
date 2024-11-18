import tkinter as tk
from ajustes import ajuste_polinomico
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def main():
    global x_entry, y_entry, grado_entry, window
    window = tk.Tk()
    window.title("Ajuste Polinómico")
    window.geometry("720x480")
    
    label = tk.Label(window, text="Ingrese los valores de x y y")
    label.pack(pady=20)
    
    x_entry = tk.Entry(window)
    x_entry.pack(pady=10)
    y_entry = tk.Entry(window)
    y_entry.pack(pady=10)
    
    label_grado = tk.Label(window, text="Ingrese el grado del polinomio")
    label_grado.pack(pady=10)
    
    grado_entry = tk.Entry(window)
    grado_entry.pack(pady=10)
    
    accept = tk.Button(window, text="Aceptar", command=ajustar)
    accept.pack(pady=10)
    
def ajustar():
    x = list(map(float, x_entry.get().split(",")))
    y = list(map(float, y_entry.get().split(",")))
    grado = int(grado_entry.get())
    coeficientes, bondad = ajuste_polinomico(x, y, grado)
    
    label_result = tk.Label(window, text=f"Coeficientes del polinomio: {coeficientes}")
    label_result.pack(pady=20)
    
    # Crear la figura de Matplotlib
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label='Datos')
    x_line = np.linspace(min(x), max(x), 100)
    y_line = np.polyval(coeficientes, x_line)
    ax.plot(x_line, y_line, color='red', label=f'Ajuste Polinómico (grado {grado})')
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