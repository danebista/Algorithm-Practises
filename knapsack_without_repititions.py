# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w)
    new_w = [0] + w
    value = []
    for i in range (n+1):
        value.append([])
        for _ in range (W+1):
            value[i].append(0)
    for i in range(1, n+1):
        for w  in range (1, W+1):
            value[i][w] = value [i-1][w]
            
            if new_w[i] <= w:
                temp = value[i-1][w-new_w[i]] + new_w[i]
                
                if value[i][w] < temp:
                    value[i][w] = temp
    return value[-1][-1]
if __name__ == '__main__':
    input = sys.stdin.readline()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
