# Uses python3
import sys

def get_fibonacci_huge(n, m):
   array = [0,1]

   if (n <= 1): return array[n]
   p =0
   c = 1
   for j in range(n-1):
       t = p
       p = c % m
       c = (t+c) % m
       array.append(c)

       if (p == 0 and c == 1):
           index = n % (j+1)
           
           return array[index] 
    
   return c

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n,m))