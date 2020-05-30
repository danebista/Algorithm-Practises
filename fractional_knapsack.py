import sys

def get_optimal_value(capacity, weights, values):
    maxlist = [(values[i]/weights[i], weights[i]) for i in range(len(values))]
    maxlist.sort(key = lambda x: x[0], reverse= True)
    v = 0
    for i in range(0, len(maxlist)):

       if capacity <= 0:
           return v
       temp = min(maxlist[i][1], capacity)

       v= v + temp * maxlist[i][0]
	
       capacity = capacity - temp
    return v

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))