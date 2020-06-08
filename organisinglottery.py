# Uses python3
import sys
def fast_count_segments(starts, ends, points):
    newArray = []
    for i in range(len(starts)):
        newArray.append((starts[i], 'l'))
        newArray.append((ends[i]+ 1, 'r'))
    cnt= [0] * len(points)
    points = [(i,'p') for i in points]
    z = newArray + points
    count = 0
    m =sorted(z, key=lambda x: x[0])
    dictionary = {}
    for i in m:
        if 'l' in i[1]: count += 1
        elif 'r' in i[1]: count -=1
        else: 
            dictionary['{}{}'.format(i[0],i[1])] = count
    for i in range(len(cnt)):
        cnt[i] = dictionary['{}{}'.format(points[i][0],points[i][1])]
    return cnt
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
