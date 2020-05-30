# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    index = []
    segments.sort(key = lambda x: x.end)
    while (segments):
        test = segments[0].end
        for s in segments:
            if (s.start <= test <= s.end):
                index.append(s)
        if len(index) >= 0:
            points.append(test)
            for i in index:
                segments.remove(i) 
        index = []      
    return points    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
