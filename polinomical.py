import tkinter as tk
from tkinter import messagebox
from ajustes import ajuste_polinomico
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from matplotlib.ticker import FuncFormatter

def main():
    global x_entry, y_entry, grado_entry, window, label_result, bondad_label, canvas
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
    
    save_button = tk.Button(window, text="Guardar Gráfica", command=guardar_grafica)
    save_button.pack(pady=10)

    copy_button = tk.Button(window, text="Copiar Fórmula", command=copiar_formula)
    copy_button.pack(pady=10)
    
    # Inicializar las referencias a los widgets dinámicos
    label_result = None
    bondad_label = None
    canvas = None

# Reescalar eje Y por 10^4
def reescalar_y(val, pos):
    return f"{val / 1e4:.1f}"

def ajustar():
    global label_result, bondad_label, canvas, fig, ax, coeficientes, bondad

    # Limpiar resultados anteriores si existen
    if label_result:
        label_result.destroy()
    if bondad_label:
        bondad_label.destroy()
    if canvas:
        canvas.get_tk_widget().destroy()
    
    # Obtener entradas del usuario
    x = list(map(float, x_entry.get().split(",")))
    y = list(map(float, y_entry.get().split(",")))
    grado = int(grado_entry.get())
    coeficientes, bondad = ajuste_polinomico(x, y, grado)
    
    # Mostrar resultados
    label_result = tk.Label(window, text=f"Coeficientes del polinomio: {coeficientes}")
    label_result.pack(pady=20)
    
    bondad_label = tk.Label(window, text=f"El coeficiente de bondad es: {bondad}")
    bondad_label.pack(pady=10)
    
    # Configurar estilo y fuente global
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams['font.family'] = 'Times New Roman'
    
    # Crear la figura de Matplotlib
    fig, ax = plt.subplots(figsize=(10, 5))  # Tamaño similar al ejemplo

    # Configurar el eje y para mostrar los valores divididos por 10^4
    ax.yaxis.set_major_formatter(FuncFormatter(reescalar_y))

    # Agregar nota sobre el reescalado
    ax.text(0.95, 0.02, "Valores reescalados (×10⁴)",
            transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right')

    ax.scatter(x, y, color='black', label='Datos', s=50)  # Tamaño del scatter igual al ejemplo
    x_line = np.linspace(min(x), max(x), 100)
    y_line = np.polyval(coeficientes, x_line)
    ax.plot(x_line, y_line, color='red', label=f'Ajuste Polinómico (grado {grado})', linestyle='-', linewidth=1.5)
    
    # Títulos y etiquetas
    ax.set_title(f"Gráfico de Ajuste Polinómico (grado {grado})", fontsize=14)
    ax.set_xlabel("Dia del mes", fontsize=12)  # Cambié el nombre del eje X a "e"
    ax.set_ylabel("Pico máximo de jugadores", fontsize=12)  # Cambié el nombre del eje Y

    # Ajuste de cuadrícula y límites
    ax.grid(True, linestyle='--', alpha=0.6)
    
    # Agregar leyenda
    ax.legend(loc='upper left', fontsize=10)
    
    # Aplicar diseño compacto
    plt.tight_layout()
    
    # Integrar la figura en Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

def guardar_grafica():
    if fig:
        try:
            fig.savefig('grado.png', dpi=300)  # Guardar la gráfica
            messagebox.showinfo("Guardar Gráfica", "La gráfica se guardó como 'grafica_ajuste.png'.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar la gráfica: {e}")

def copiar_formula():
    # Verificar que coeficientes no esté vacío y sea un array
    if coeficientes is not None and len(coeficientes) > 0:
        # Generar la fórmula polinómica en formato legible
        formula = "f(x) = "
        terms = []
        for i, coef in enumerate(coeficientes):
            if i == 0:
                terms.append(f"{coef:.3f}")
            else:
                terms.append(f"{coef:.3f}x^{len(coeficientes) - i - 1}")
        
        formula += " + ".join(terms)
        
        # Copiar la fórmula al portapapeles
        window.clipboard_clear()  # Limpiar portapapeles
        window.clipboard_append(formula)  # Copiar fórmula
        window.update()  # Actualizar el portapapeles
        messagebox.showinfo("Fórmula Copiada", f"La fórmula polinómica ha sido copiada al portapapeles:\n{formula}")
    else:
        messagebox.showerror("Error", "No se han calculado coeficientes válidos. Ajuste el polinomio primero.")


if __name__ == "__main__":
    main()
    tk.mainloop()
