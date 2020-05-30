# Uses python3
import sys

def gcd(a, b):
    
    while (a):
        a,b = b%a, a
    
    return b

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())

    print (gcd(a, b))
