#Uses python3

import sys

def lcs2(a, b):
    D= []
    a[1:] = a[:]
    b[1:] = b[:]
    firstLength = len(a)
    secondLength = len(b)
    for i in range(firstLength):
        D.append([])
        for j in range(secondLength):
            D[i].append(0)
    for i in range(1, firstLength):
        for j in range(1, secondLength):
            if a[i] == b[j]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])
    return D[-1][-1]
if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
