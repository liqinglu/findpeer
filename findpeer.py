class FindPeer:

	PEER = 2
	RESULTNUM = 3

	def __init__(self):
		pass
		
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
		
	def MM(self,n):  
		if(type(n)!=int or n<2):
			print("input args is not INT type or is less than 2")
			return  
		return self.sortedlist(list(range(0,n)))