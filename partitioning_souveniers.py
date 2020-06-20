# Uses python3
import sys
import itertools

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
    
def partition3(A):
    total = sum(A)
    number = len(A)
    
    if (total % 3 !=0 or number<=2): return 0
    
    firstList = total //3
    secondList = 2 * (total//3)
    optimal_weight1 = optimal_weight(firstList, A)
    optimal_weight2 = optimal_weight(secondList, A)
    optimal_weight3 = optimal_weight(total, A)

    return 1 if (firstList == optimal_weight1 and secondList == optimal_weight2 and total == optimal_weight3) else 0
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

