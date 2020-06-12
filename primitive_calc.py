# Uses python3
import sys

def optimal_sequence(n):
    minValue = [-1,0,1,1] + (n-3) * [[0,0]]
    copy = n
    sequence = []
    for i in range(4, n+1):
        minValue[i]= 1000000000000
        for j in range(1,4):
            if i< j: continue
            if j ==1:
                minNumber = minValue[i-1]+ 1 
            elif i % j == 0 and j != 1:
                minNumber = minValue[i//j]+ 1
            if minNumber< minValue[i]:
                minValue[i] = minNumber
    sequence.append(n)
    
    while copy > 1:
        minimum = 10000000000
        temp = copy-1
        for i in range (1, 4):
            if i==1:
                minimum = minValue[copy-1]
            elif copy % i == 0 and i != 1:
                if minValue[copy//i]< minimum:
                    minimum = minValue[copy//i]
                    temp = temp * 0 + copy//i
        sequence.append(temp)
        copy = temp
    return sequence[::-1]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
