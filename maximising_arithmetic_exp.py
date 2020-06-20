# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    operatorArray = []
    operandArray = []

    n = len(dataset)
    for i in range(n):
        if i % 2 ==0:
            operandArray.append(int(dataset[i]))
        else:
            operatorArray.append(dataset[i])
    minArray = []
    maxArray = []
    operator_number = len(operandArray)

    for i in range (operator_number+1):
        minArray.append([])
        maxArray.append([])
        for _ in range (operator_number+1):
            minArray[i].append(0)
            maxArray[i].append(0)
    
    for i in range(1, operator_number+1):
        minArray[i][i] = operandArray[i-1]
        maxArray[i][i] = operandArray[i-1]  
    
    for s in range(1, operator_number):
        for i in range(1, operator_number+1 - s):
            j = i + s
            minArray[i][j], maxArray[i][j] = min_and_max(i, j, operatorArray, maxArray, minArray)
    
    return maxArray[1][operator_number]

def min_and_max(i, j, operatorArray, maxArray, minArray):
    mini = 1000000000000
    maxi = -100000000000

    for k in range(i, j):
        a = evalt(maxArray[i][k], maxArray[k+1][j], operatorArray[k-1])
        b = evalt(maxArray[i][k], minArray[k+1][j], operatorArray[k-1])
        c = evalt(minArray[i][k], maxArray[k+1][j], operatorArray[k-1])
        d = evalt(minArray[i][k], minArray[k+1][j], operatorArray[k-1])

        mini = min(mini,a,b,c,d)
        maxi = max(maxi,a,b,c,d)
        
    return mini,maxi
if __name__ == "__main__":
    print(get_maximum_value(input()))
