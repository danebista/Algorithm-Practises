#Uses python3
import sys
import random
def dist(x, y):
	return ((y[0]-x[0])**2 + (y[1]-x[1])**2)** 0.5

def calculate_min_dis(newpoints, n):
	min_val = float('inf')
	for i in range(n): 
		for j in range(i + 1, n): 
			newdist = dist(newpoints[i], newpoints[j])
			
			if newdist < min_val: 
				min_val = newdist
	return min_val 

def closestPoints(q_x, q_y, d):
	minVal = d
	mid = q_x[len(q_x)//2][0]
	new_array = [x for x in q_y if mid -minVal<= x[0] <= mid + minVal]
	for i in range(len(new_array)-1):
		for j in range(i+1, min(i+7, len(new_array))):
			distance = dist(new_array[i], new_array[j])
			if distance < minVal:
				minVal = distance
	return minVal

def minimum_distance(qx,qy, n):
	if n <=3:
		return calculate_min_dis(qx, n)
	mid = n // 2
	midPoint = qx[mid]
	bx = []
	by = []
	for x in qy:
		if x[0] <= midPoint[0]:
			bx.append(x)
		else:
			by.append(x)
	
	d1 = minimum_distance(qx[:mid], bx, mid)

	d2 = minimum_distance(qx[mid:], by,n- mid)

	minDist =min(d1,d2)
	return min(minDist, closestPoints(qx, qy, minDist))
if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n = data[0]
	x = data[1::2]
	y = data[2::2]
	point = [0]* n
	for i in range(n):
		point[i]= [x[i],y[i]]
	ax= sorted(point,key=lambda x: x[0])
	ay = sorted(point, key= lambda x:x[1])
	print("{0:.4f}".format(minimum_distance(ax, ay, n)))
