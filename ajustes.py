import numpy as np

def ajuste_lineal(x, y) -> float:
    n: int = len(x)
    suma_x: float = sum(x)
    suma_y: float = sum(y)
    suma_x2: float = sum([xi**2 for xi in x])
    suma_xy: float = sum([xi*yi for xi, yi in zip(x, y)])
    
    determinante_general: float = n * suma_x2 - suma_x**2  # Obtenemos el determinante general de la matriz A
    
    b: float = (suma_y * suma_x2 - suma_x * suma_xy) / determinante_general
    m: float = (n * suma_xy - suma_x * suma_y) / determinante_general
    
    y_promedio: float = suma_y / n
    st: float = sum([(yi - y_promedio)**2 for yi in y])
    sr: float = sum([(yi - m*xi - b)**2 for xi, yi in zip(x, y)])
    bondad: float = (st - sr) / st
    return b, m, bondad

def ajuste_polinomico(x, y, grado) -> float:
    # Ajuste polinómico de grado especificado
    coeficientes = np.polyfit(x, y, grado)
    p = np.poly1d(coeficientes)
    
    # Calcular la bondad del ajuste
    y_promedio = np.mean(y)
    st = sum([(yi - y_promedio)**2 for yi in y])
    sr = sum([(yi - p(xi))**2 for xi, yi in zip(x, y)])
    bondad = (st - sr) / st
    
    return coeficientes, bondad

def ajuste_potencial(x, y) -> float:
    # Transformar los datos
    x_log = np.log(x)
    y_log = np.log(y)
    
    # Ajuste lineal a los datos transformados
    b_log, m_log, bondad = ajuste_lineal(x_log, y_log)
    
    # Transformar los coeficientes de vuelta
    a = np.exp(b_log)
    b = m_log
    
    return a, b, bondad

def ajuste_exponencial(x, y) -> float:
    # Transformar los datos
    y_log = np.log(y)
    
    # Ajuste lineal a los datos transformados
    b_log, m_log, bondad = ajuste_lineal(x, y_log)
    
    # Transformar los coeficientes de vuelta
    a = np.exp(b_log)
    b = m_log
    
    return a, b, bondad

def ajuste_cociente(x, y) -> float:
    # Transformar los datos
    y_inv = [1 / yi for yi in y]
    
    # Ajuste lineal a los datos transformados
    b_inv, m_inv, bondad = ajuste_lineal(x, y_inv)
    
    # Transformar los coeficientes de vuelta
    a = 1 / b_inv
    b = m_inv / b_inv
    
    return a, b, bondad