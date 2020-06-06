# Uses python3
import sys
def counter (a, num, left, right):
    count = 0
    for i in range(left, right+ 1):
        if a[i] == num:
            count = count + 1
    return count

def get_majority_element(a, left, right):
    c = divide_algo(a, left, right-1)
    count = counter(a, c, left, right-1)
    
    if (count <= len(a)/2) : return -1
    return count

def divide_algo(a, left, right):
    
    if left == right:
        return a[left]
    mid = (right - left) // 2 + left 

    firsthalf = divide_algo(a, left, mid)
    secondhalf = divide_algo(a, mid + 1, right)
    
    if firsthalf == secondhalf:
        return firsthalf
    leftCount = counter(a, firsthalf, left, right)
    rightCount = counter(a, secondhalf, left, right)
    
    return firsthalf if leftCount >= rightCount else secondhalf

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) == -1:
        print(0)
    else:
        print(1)
