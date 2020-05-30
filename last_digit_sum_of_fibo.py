# Uses python3
import sys

def fibonacci_sum(n):
    index = n % 60

    numbers = [j for j in range(60)]

    for i in range(2, 60):
        numbers[i] = numbers[i-1] + numbers[i-2]

    return sum(numbers[:index+1]) % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    
    print(fibonacci_sum(n))
