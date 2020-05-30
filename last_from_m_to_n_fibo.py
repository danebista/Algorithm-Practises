# Uses python3
import sys

def fibonacci_partial_sum(from_, to):
    if (from_ > to): return

    
    indexBase = from_ % 60
    
    indexLast = to % 60

    if (indexLast < indexBase):
        indexLast = (indexBase + indexLast) + 1

    numbers = [j for j in range(60)]
    
    for j in range(2, 60):
        numbers[j] = numbers[j-1] + numbers [j-2]

    return sum(numbers[indexBase : indexLast + 1]) % 10

if __name__ == '__main__':
    input = sys.stdin.readline()
    from_, to = map(int, input.split())
   
    print(fibonacci_partial_sum(from_, to))