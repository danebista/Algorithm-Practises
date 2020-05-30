import sys

def largest_number(a):
    answer = ""
    cache = {}
    a.sort(reverse=1)
    while len(a) != 0:
        maxDigit = 0
        for digit in a:
            maxDigit = calculateMaxDigit(digit, maxDigit, cache)
        answer = answer + maxDigit
        a.remove(maxDigit)
    return answer

def calculateMaxDigit(digits, maxDigit, cache):
    
    if (cache.get("{}&{}".format(digits, maxDigit)) != None): return cache["{}&{}".format(digits, maxDigit)]

    comp1 = str(digits) + str(maxDigit)
    comp2 = str(maxDigit) + str(digits)

    greaterDigit = digits if int(comp1) > int(comp2) else maxDigit
    cache["{}&{}".format(digits, maxDigit)] = greaterDigit
    return greaterDigit

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))