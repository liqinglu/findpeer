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

class FindPeer(object):

    PEER = 2
    RESULTNUM = 3

    def __init__(self):
        self.possiblecomb = []
        self.possiblecombkv = {}
        self.maxv = 0
        
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

    def findmaxpeercomb(self):
        pass

    def getcombkv(self,record):
        for c in self.possiblecomb:
            weight = record[c[0]][c[1]] + record[c[1]][c[0]]
            self.possiblecombkv.setdefault(weight,[]).append(c)

        #for k,v in self.possiblecombkv.iteritems():
        #    print " ",k," ",v
        groupnumber = len(record[0])/self.PEER
        keys = sorted([x for x in self.possiblecombkv.iterkeys()],reverse=True)
        #print keys

        i = 0
        for skey in keys:
            for svalue in self.possiblecombkv[skey]:
                self.maxv += skey
                i += 1
                if i == groupnumber:
                    break

            if i == groupnumber:
                break
        #print self.maxv

    def newsortedlist(self,li):
        for c in gcomb(li,self.PEER):
            self.possiblecomb.append(c)

    def MM(self,n):  
        if(type(n)!=int or n<2):
            print("input args is not INT type or is less than 2")
            return  
        self.newsortedlist(list(range(0,n)))
