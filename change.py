# Uses python3
import sys

def get_change(m, coins):
	minCoins = (m+1) * [0]
	
	for i in range(1,m+1):
		minCoins[i] = sys.maxsize
		
		for j in range (0, len(coins)):
			
			if i< coins[j]: continue
			numCoins = minCoins[i-coins[j]] + 1
			
			if numCoins < minCoins[i]:
				minCoins[i] = numCoins
	return minCoins[m]
	
if __name__ == '__main__':
	# enter money to change, coin denominations
	input = sys.stdin.read()
	n, *A = list(map(int, input.split()))
	print(get_change(n, A))


