import unittest
import testfindpeer

def suite():
	suite = unittest.TestSuite()
	suite.addTest(testfindpeer.testfindpeer("testfindidx1"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx2"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx3"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx4"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx5"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx6"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx7"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx8"))
	suite.addTest(testfindpeer.testfindpeer("testfindidx9"))
	suite.addTest(testfindpeer.testfindpeer("testsortedlist1"))
	suite.addTest(testfindpeer.testfindpeer("testsortedlist2"))
	suite.addTest(testfindpeer.testfindpeer("testsortedlist3"))
	return suite
	
if __name__ == "__main__":
	unittest.main(defaultTest="suite")