import unittest
import random
from retval import f1
from f2 import f2
from f3 import f3

class TestStringMethods(unittest.TestCase):
#	def test_upper(self):
#		self.assertEqual('foo'.upper(),'FOO')
#	def test_isUpper(self):
#		self.assertTrue('FOO'.isupper())
#		self.assertFalse('Foo'.isupper()) 
#	def test_test(self):
#		self.assertTrue(True)

#testy funkcji f1
	def test_f1(self):
		self.assertEqual(f1(0),0)
	def test_f1_1(self):
		self.assertEqual(f1(1),1)
	def test_f1_2(self):
		self.assertEqual(f1(2),4)
	def test_f1_3(self):
		self.assertEqual(f1(2,1),5)
	def test_f1_4(self):
		self.assertEqual(f1(2,3),7)
	
#testy funkcji f2
	def test_f2_1(self):
		self.assertEqual(f2("a","ala"),"a")
	def test_f2_2(self):
		self.assertEqual(f2(1,[1,2,3]),1)
	def test_f2_3(self):
		self.assertEqual(f2("BUUUUM",[]),"BUUUUM")
#testy funkcji f3
	def test_f3_1(self):
		self.assertEqual(f3(1),"jeden")
		self.assertEqual(f3(2),"dwa")
		self.assertEqual(f3(3),"trzy")
		self.assertEqual(f3(random.randint(4,1000)),"other")

if __name__ == "__main__":
	unittest.main()
