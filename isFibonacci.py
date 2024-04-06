def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_sequence(n):
    fib_seq = []
    for i in range(n):
        fib_seq.append(fibonacci(i))
    return fib_seq

numero = int(input("Digite um numero para verificar se pertence a sequencia de fibonacci: "))
if(numero in fibonacci_sequence(numero)):
    print("Numero " + str(numero) + " pertence a sequencia de fibonacci!")
else:
    print("Numero " + str(numero) + " nao pertence a sequencia de fibonacci !")