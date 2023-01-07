def fibonacci(num: int):
    a = 0
    b = 1
    index = 0
    while index < num:
        result = a
        a, b = b, a+b
        yield result
        index += 1

f = fibonacci(10)

for i in f:
    print(i)