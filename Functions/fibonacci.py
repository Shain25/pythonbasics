def fibonacci(n: int):
    sequence = []
    a=0
    b=1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(10))
print(fibonacci(5))