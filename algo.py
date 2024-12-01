import matplotlib.pyplot as plt

# Configurar estilo y fuente global
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'Times New Roman'

# Datos
days = list(range(1, 25))
players = [1701, 2044, 2103, 1470, 1433, 1352, 1257, 1497, 2009, 2090, 
           1715, 1591, 5042, 7122, 9555, 13679, 15293, 10719, 10372, 
           10034, 8831, 9865, 12282, 8056]

# Conversión de jugadores a escala 10^4
players_scaled = [p / 1e4 for p in players]


# Crear el gráfico
plt.figure(figsize=(10, 5))
plt.scatter(days, players_scaled, color='black', label='Jugadores (x $10^4$)', s=50)
plt.plot(x, [yi / 1e4 for yi in y], color='red', linestyle='-', label=r'$y = 3658.3946 \cdot \frac{x}{1.9888 + x}$')

# Títulos y etiquetas
plt.title("Pico máximo de jugadores por día (Noviembre 2024)", fontsize=14)
plt.xlabel("Día del mes", fontsize=12)
plt.ylabel("Pico Máximo de Jugadores (x $10^4$)", fontsize=12)

# Ajuste de la cuadrícula y límites
plt.ylim(0, max(players_scaled) * 1.1)
plt.grid(True, linestyle='--', alpha=0.6)

# Leyenda
plt.legend(loc='upper left', fontsize=10)

# Ajuste final y mostrar
plt.tight_layout()
plt.show()
