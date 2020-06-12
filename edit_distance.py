# Uses python3
def edit_distance(s, t):
    slist = list(s)
    tlist = list(t)
    slist[1:] =slist[:]
    tlist[1:] = tlist[:]
    firstList = slist if len(slist) > len(tlist) else tlist
    secondList = slist if firstList!= slist else tlist
    first = len(firstList)
    second = len(secondList)
    D=[[]]

    for j in range(second):
        D[0].append(j)

    for i in range (1, first):
        D.append([i]+[0]*(first-1))

    for i in range(1, first):
        for j in range(1, second):
            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1]+ 1
            
            if firstList[i] == secondList[j]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    
    return D[first - 1][second-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
