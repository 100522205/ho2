def format_time(numero):
    # 1. Convertimos a string para analizar la posición del primer dígito no cero
    # Usamos 20 decimales para asegurar que capturamos números pequeños
    texto_analisis = f"{numero:.20f}" 
    
    # 2. Separamos parte entera y decimal
    entero, decimal = texto_analisis.split('.')
    
    # 3. Buscamos el índice del primer número distinto de 0
    indice_no_cero = -1
    for i, digito in enumerate(decimal):
        if digito != '0':
            indice_no_cero = i
            break
    
    # Si todo son ceros (ej: 0.0), devolvemos "0.0"
    if indice_no_cero == -1:
        return f"{entero}.0"
    
    # 4. Calculamos la precisión necesaria para incluir el siguiente dígito
    # Queremos mantener los ceros iniciales + el primer no-cero + el siguiente.
    # El índice es basado en 0, así que sumamos 2 para obtener la longitud total.
    # Ejemplo: 0.003... -> índice 2. Queremos 2 + 2 = 4 decimales (0.003x)
    precision = indice_no_cero + 2
    
    # 5. Formateamos usando f-string, que aplica redondeo automáticamente
    return f"{numero:.{precision}f}"

