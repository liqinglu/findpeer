import unittest
import findpeer

class testfindpeer(unittest.case.TestCase):
	def setUp(self):
		self.tclass = findpeer.FindPeer()
	
	def tearDown(self):
		pass
		
	def testfindidx1(self):
		print("#####test1 func findidx#####")
		self.assertEqual(self.tclass.findidx(38,[36]),0)
	
	def testfindidx2(self):
		print("#####test2 func findidx#####")
		self.assertEqual(self.tclass.findidx(35,[36]),1)
		
	def testfindidx3(self):
		print("#####test3 func findidx#####")
		self.assertEqual(self.tclass.findidx(38,[36,33]),0)
	
	def testfindidx4(self):
		print("#####test4 func findidx#####")
		self.assertEqual(self.tclass.findidx(30,[36,33]),2)
	
	def testfindidx5(self):
		print("#####test5 func findidx#####")
		self.assertEqual(self.tclass.findidx(35,[36,33]),1)

	def testfindidx6(self):
		print("#####test6 func findidx#####")
		self.assertEqual(self.tclass.findidx(30,[36,33,30]),-1)

	def testfindidx7(self):
		print("#####test7 func findidx#####")
		self.assertEqual(self.tclass.findidx(38,[36,33,30]),0)

	def testfindidx8(self):
		print("#####test8 func findidx#####")
		self.assertEqual(self.tclass.findidx(35,[36,33,30]),1)

	def testfindidx9(self):
		print("#####test9 func findidx#####")
		self.assertEqual(self.tclass.findidx(31,[36,33,30]),2)
	
	def testsortedlist1(self):
		print("#####test1 func sortedlist#####")
		self.assertEqual( len(self.tclass.sortedlist([0,1])) , 1 )
	
	def testsortedlist2(self):
		print("#####test2 func sortedlist#####")
		self.assertEqual( len(self.tclass.sortedlist([0,1,2,3])) , 3 )

	def testsortedlist3(self):
		print("#####test3 func sortedlist#####")
		self.assertEqual( len(self.tclass.sortedlist([0,1,2,3,4,5])) , 15 )
		
if __name__=='__main__':
	unittest.main()