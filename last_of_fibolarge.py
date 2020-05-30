def fibonacci(n):
    index = n % 60

    number = [_ for _ in range(60)]
    
    for i in range(2, 60):
        number[i] = number[i-1] + number[i-2]
    
    return number[index] % 10

n = int(input())

print(fibonacci(n))