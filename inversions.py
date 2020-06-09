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

def closestPoints(array, d):
	minVal = d
	size = len(array)

	for i in range(size):
		j = i + 1
		while j < size and (array[j][1]-array[i][1])< minVal:
			if (dist(array[i], array[j]) < minVal):
				minVal = dist(array[i], array[j])
			j= j+ 1
	return minVal

def minimum_distance(qx,qy, n):
	if n <=3:
		return calculate_min_dis(qx, n)
	mid = n // 2
	midPoint = ax[mid]
	#print (midPoint)
	bx = []
	by = []
	for x in qy:
		if x[0] < midPoint[0]:
			bx.append(x)
		else:
			by.append(x)
	#print(bx)
	#print (by)
	d1 = minimum_distance(qx[:mid], bx, mid)
	d2 = minimum_distance(qx[mid:], by,n- mid)
	#print (d1)
	#print (d2)
	minDist =min(d1,d2)
	newArray = []
	for i in range(n):
		if abs(qy[i][0] - midPoint[0]) < minDist:
			newArray.append(qy[i])
	return closestPoints(newArray, minDist)
if __name__ == '__main__':
	#input = sys.stdin.readline()
	#data = list(map(int, input.split()))
	#n = data[0]
	
	n = 7
	x= [8,4,1,5,6,8,8]
	y = [6,3,7,9,9,6,7]
	point = n * [0]
	for i in range(n):
		point[i]= [x[i],y[i]]
	ax= sorted(point,key=lambda x: x[0])
	ay = sorted(point, key= lambda x:x[1])
	a= calculate_min_dis(ax, n)
	b = minimum_distance(ax, ay, n)
	if a == b:
		print("Ok")
	else:
		print ('{}', point)
		print ('{}',a)
		print ('{}',b)
		print ('{}',n)
		


