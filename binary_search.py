theList = [4, 1, 43, 34, 32, 3, 78, 43, 10]
theList.sort()

print(theList)


def find(number):
    first = 0
    last = len(theList) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        print(theList[midpoint])
        if theList[midpoint] == number:
            found = True
        else:
            if number < theList[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


print(find(34))
