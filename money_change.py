# Uses python3
import sys
import math
def get_change(m):
    a = [10,5,1]
    t = 0
    for i in range(len(a)):
        if m<a[i] or m==0: continue
        t= t+ m//a[i]
        m = m%a[i]
    return t

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
