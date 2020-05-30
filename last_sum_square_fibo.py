# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    index = n % 60
    numbers = [j for j in range(60)]

    for j in range(2, 60):
        numbers[j] = numbers[j-1] + numbers[j-2]

    squareArray = [_**2 for _ in numbers]

    return sum(squareArray[:index + 1]) % 10
    
if __name__ == '__main__':
    n = int(stdin.readline())
    print(fibonacci_sum_squares_naive(n))
