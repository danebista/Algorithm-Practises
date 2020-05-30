def Fibonacci(n):
    number = [j for j in range(n+1)]

    for i in range(2, n + 1):
        number[i] = number[i - 1] + number[i - 2]
    
    return number[n]

n = int(input ())
print (Fibonacci(n))