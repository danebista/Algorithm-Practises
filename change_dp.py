# Uses python3
import sys

def get_change(m):
	minCoins = (m+1) * [0]
	coins = [1,3,4]
	for i in range(1,m+1):
		minCoins[i] = 100000000
		for j in range (0, len(coins)):
			if i< coins[j]: continue
			numCoins = minCoins[i-coins[j]] + 1
			if numCoins < minCoins[i]:
				minCoins[i] = numCoins
	return minCoins[m]
	
if __name__ == '__main__':
	m = int(sys.stdin.read())
	print(get_change(m))
