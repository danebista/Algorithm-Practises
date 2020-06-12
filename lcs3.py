#Uses python3

import sys

def lcs3(a, b, c):
    a[1:] = a[:]
    b[1:] = b[:]
    c[1:] = c[:]
    D= []
    firstLength = len(a)
    secondLength = len(b)
    thirdLength = len(c)
    for i in range(firstLength):
        D.append([])
        for j in range(secondLength):
            D[i].append([])
            for _ in range(thirdLength):
                D[i][j].append(0)
    for i in range(1,firstLength):
        for j in range(1,secondLength):
            for m in range(1,thirdLength):
                if a[i] == b[j] == c[m]:
                    D[i][j][m] = D[i-1][j-1][m-1] + 1
                else:
                    D[i][j][m] = max(D[i-1][j][m],D[i][j-1][m],D[i][j][m-1], D[i-1][j-1][m],D[i-1][j][m-1], D[i][j-1][m-1])
    return D[-1][-1][-1]
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
