def calcular_movimientos_hanoi(n):
    """
    Calcula el número de movimientos necesarios para resolver la Torre de Hanói para n piedras.

    Parámetros:
    n -- número de piedras
    """
    return 2**n - 1

# Imprimir el número de movimientos para cada cantidad de piedras del 1 al 73
for i in range(1, 74):
    movimientos = calcular_movimientos_hanoi(i)
    print(f"Piedras: {i}, Movimientos necesarios: {movimientos}")
