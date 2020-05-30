# python3
import sys


def compute_min_refills(distance, tank, stops):
    x= [0 for _ in range(len(stops)+2)]
    x[1:-1] = stops
    x[-1] = distance
    refills = 0
    currentPosition = 0
    while currentPosition <= len(stops):
        lastPostion = currentPosition
        while (currentPosition <= len(stops) and x[currentPosition + 1]- x[lastPostion] <= tank):
            currentPosition = currentPosition + 1
        
        if (currentPosition == lastPostion):
            return -1
        if currentPosition <= len(stops):
            refills = refills + 1
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
