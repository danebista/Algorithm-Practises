import sys

def get_majority_element(a, left, right):
    max = a[0]
    count = 1
    maxcount = 0
    
    for i in range(right+1):
        if max == a[i]:
            count = count +1
        count = count -1
        if (count == 0): max = a[i]
    
    for i in range (right + 1):
        if max == a[i]:
            maxcount = maxcount + 1

    if (maxcount > len(a)/2): return 0
    return -1
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) == -1:
        print(0)
    else:
        print(1)