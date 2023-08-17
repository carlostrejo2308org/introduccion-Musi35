def fibo(n):
    n = int(n)  # Convertir el valor ingresado a un número entero
    fib_sequence = [0, 1]  # Inicializamos la secuencia con los primeros dos números

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Calculamos el siguiente número
        fib_sequence.append(next_number)  # Agregamos el siguiente número a la secuencia

    return fib_sequence

# Solicitar al usuario que ingrese la cantidad de números de Fibonacci que desea calcular
n = input("Ingrese cuántos números de Fibonacci desea calcular: ")

# Calcular y mostrar la secuencia de Fibonacci
fib_sequence = fibo(n)
print(f"Los primeros {n} números de Fibonacci son: {fib_sequence}")