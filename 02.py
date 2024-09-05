def fibonacci(numero):
    a, b = 0, 1
    if numero == 0 or numero == 1:
        return True
    while b < numero:
        a, b = b, a + b
    return b == numero

numero_informado = int(input("Informe um número: "))

if fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")