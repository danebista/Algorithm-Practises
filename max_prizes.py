# Uses python3
import sys

def optimal_summands(n):
    summands = []
    left = 1
    right = n
    while (right != 0):
        if (2* left < right):
            summands.append(left)
            right = right - left
        else:
            summands.append(right)
            right = 0
        left = left + 1
    return summands
if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
