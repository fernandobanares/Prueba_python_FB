def choose_level(n_pregunta, p_level):
    if p_level == 2:
        if 1 <= n_pregunta <= 2:
            level = 'básicas'
        elif 3 <= n_pregunta <= 4:
            level = 'intermedias'
        elif 5 <= n_pregunta <= 6:
            level = 'avanzadas'
        else:
            level = 'fuera de rango'
    
    elif p_level == 3:
        if 1 <= n_pregunta <= 3:
            level = 'básicas'
        elif 4 <= n_pregunta <= 6:
            level = 'intermedias'
        elif 7 <= n_pregunta <= 9:
            level = 'avanzadas'
        else:
            level = 'fuera de rango'
    
    else:
        level = 'valor de p_level no válido'
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias