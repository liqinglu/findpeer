def gcomb(x, k):
    if k > len(x):
        return
    if k == 0:
        yield []
    else:
        first, rest = x[0], x[1:]
        # A combination does or doesn't contain first.
        # If it does, the remainder is a k-1 comb of rest.
        for c in gcomb(rest, k-1):
            c.insert(0, first)
            yield c
        # If it doesn't contain first, it's a k comb of rest.
        for c in gcomb(rest, k):
            yield c

def candidate(lst):
    if len(lst)%2 != 0:
        return

    if len(lst) == 0:
        yield []
    else:
        first,rest = lst[0],lst[1:]
        for j in rest:
            tmp = rest[:]
            tmp.remove(j)
            if len(tmp) == 0:
                yield [[first,j]]
            else:
                for restcandidate in candidate(tmp):
                    restcandidate.insert(0,[first,j])
                    yield restcandidate

def isok(lst):
    newlst = {}
    for i in lst:
        for j in i:
            if j not in newlst.keys():
                newlst.setdefault(j,0)
            else:
                return False

    return True 

def candidatecomb(testlist,k):
    if k > len(testlist):
        return

    if k == 0:
        yield []
    else:
        first,rest = testlist[0],testlist[1:]
        for c in candidatecomb(rest,k-1):
            c.insert(0,first)
            if len(c) == k:
                if isok(c):
                    yield c
            else:
                yield c
        for c in candidatecomb(rest,k):
            if len(c) == k:
                if isok(c):
                    yield c
            else:
                yield c

class FindPeer(object):

    PEER = 2
    RESULTNUM = 3

    def __init__(self):
        self.possiblecomb = []
        self.possiblecombvp = {}
        self.possiblecombpv = {}
        self.maxv = 0
        self.groupnumber = 0
        self.keysv = []
        self.finalresult = {}
        
    def findidx(self,cm,max):
        level = self.RESULTNUM
        for id in range(0,len(max)):
            if(cm>max[id]):
                return id
    
        if(id==level-1):
            return -1
        elif(id<level-1):
            return id+1
        else:
            return -1
        
    def calmax(self,cm,max,el,maxp):
        level=self.RESULTNUM
        if(len(max)==0): # max is null
            max.append(cm)
            maxp.append(el)
        else:
            insert_id = self.findidx(cm,max)
            if(insert_id>=0):
                max.insert(insert_id,cm)
                maxp.insert(insert_id,el)
        
        if(len(max)>level):
            max.pop()
            maxp.pop()
            
    def findmaxpeer(self,cand,pp,rec):
        maxpeer = []
        max = []
        curmax = 0
        peer = self.PEER
        
        for elem in cand:
            for num in range(1,int(len(elem)/peer)+1):  #peer
                x = elem[(num-1)*2]
                y = elem[(num-1)*2+1]
                if rec[x][y] == '':
                    pass
                else:
                    curmax += int(rec[x][y])
                if rec[y][x] == '':
                    pass
                else:
                    curmax += int(rec[y][x])
            
            self.calmax(curmax,max,elem,maxpeer)
            curmax = 0
        
        print
        print("#####TOP %d result : " % len(max))
        for id in range(0,len(max)):
            print
            print("  POINT %d : " % max[id])
            for num in range(1,int(len(maxpeer[id])/peer)+1): #peer
                if ( pp[maxpeer[id][(num-1)*2]]=="NULL" ):
                    print("  "+pp[maxpeer[id][(num-1)*2+1]])
                elif ( pp[maxpeer[id][(num-1)*2+1]]=="NULL" ):
                    print("  "+pp[maxpeer[id][(num-1)*2]])
                else:
                    print("  %8s<==>%8s" % (pp[maxpeer[id][(num-1)*2]],pp[maxpeer[id][(num-1)*2+1]]) )
        
        
    def sortedlist(self,li):
        if (type(li)!=list):
            return
        li.sort()
        if (len(li)==2):
            return [li]
        
        result = []
        
        bak = li[:]
        head = bak.pop(0)
        for i in range(0,len(bak)):
            second = bak.pop(i)
            for j in self.sortedlist(bak):
                tmp = j[:]
                tmp.insert(0,second)
                tmp.insert(0,head)
                result.append(tmp)
            bak.insert(i,second)
        
        return result 

    def findmaxpeercomb(self,pp):
        for i in candidatecomb(self.possiblecomb,self.groupnumber):
            high = 0
            for j in i:
                high += self.possiblecombpv[str(j)]
            self.finalresult.setdefault(high,[]).append(i)

        isexit = 0
        for k in sorted(self.finalresult.iterkeys(),reverse=True):
            for item in self.finalresult[k]:
                print "%s  :::  %s" % (k,item)
                self.RESULTNUM -= 1
                if self.RESULTNUM == 0:
                    isexit = 1
                    break
            if isexit:
                break

    def getcombkv(self,record):
        for c in self.possiblecomb:
            weight = record[c[0]][c[1]] + record[c[1]][c[0]]
            self.possiblecombvp.setdefault(weight,[]).append(c)
            self.possiblecombpv.setdefault(str(c),weight)
        #for c in self.possiblecomb:
        #    weight = record[c[0]][c[1]] + record[c[1]][c[0]]
        #    self.possiblecombvp.setdefault(weight,[]).append(c)
        #    self.possiblecombpv.setdefault(str(c),weight)

        #print self.possiblecomb
        self.possiblecomb = []
        #for k,v in self.possiblecombvp.iteritems():
        #    print " ",k," ",v
        self.groupnumber = len(record[0])/self.PEER
        self.keysv = sorted([x for x in self.possiblecombvp.iterkeys()],reverse=True)
        for keysv in self.keysv:
            if keysv == 0:
                continue
            for candidatepair in self.possiblecombvp[keysv]:
                self.possiblecomb.append(candidatepair)

        #print self.possiblecomb
        #i = 0
        #print self.possiblecomb
        #for skey in self.keysv:
        #    for svalue in self.possiblecombvp[skey]:
        #        self.maxv += skey
        #        i += 1
        #        if i == self.groupnumber:
        #            break
        #    if i == self.groupnumber:
        #        break
        #print self.maxv

    def newsortedlist(self,li):
        for c in gcomb(li,self.PEER):
            self.possiblecomb.append(c)

    def MM(self,n):  
        if(type(n)!=int or n<2):
            print("input args is not INT type or is less than 2")
            return  
        self.newsortedlist(list(range(0,n)))
        #self.sortedlist(list(range(0,n)))
