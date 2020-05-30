#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    s= 0
    n = len(a)
    for _ in range(n):
        highestList1 = max(a)
        highestList2 = max(b)
        s = s + highestList1 * highestList2
        a.remove(highestList1)
        b.remove(highestList2)
    return s

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
