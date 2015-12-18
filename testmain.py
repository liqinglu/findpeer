lst = [[2, 4], [1, 3], [0, 1], [0, 2], [2, 5], [3, 5], [1, 2], [1, 4], [0, 3], [0, 4], [2, 3], [4, 5]]

number = 3

def isok(lst):
    newlst = {}
    for i in lst:
        for j in i:
            if j not in newlst.keys():
                newlst.setdefault(j,0)
            else:
                return False

    return True 

def candidate(testlist,k):
    if k > len(testlist):
        return

    if k == 0:
        yield []
    else:
        first,rest = testlist[0],testlist[1:]
        for c in candidate(rest,k-1):
            c.insert(0,first)
            if len(c) == number:
                if isok(c):
                    yield c
            else:
                yield c
        for c in candidate(rest,k):
            if len(c) == number:
                if isok(c):
                    yield c
            else:
                yield c

def main():
    output = []
    for i in candidate(lst,number):
        print i
        #output.append(i)

    #print list(set(output))

if __name__ == "__main__":
    main()
