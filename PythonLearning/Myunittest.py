# -*-coding:UTF-8-*-
import unittest


class IntegerArithmeticTestCase(unittest.TestCase):
	def test_Add(self):  # test method names begin 'test_*'
		"""
		test method for add function
		"""
		self.assertEqual((1 + 2), 3)
		self.assertEqual(0 + 1, 1)
	
	def test_Multiply(self):
		"""
		test method for multiply function
		"""
		self.assertEqual((0 * 10), 0)
		self.assertEqual((5 * 8), 40)


class TestStringMethods(unittest.TestCase):
	def test_upper(self):
		"""
		
		:return:
		"""
		self.assertEqual('foo'.upper(), 'FOO')
	
	def test_isupper(self):
		"""
		
		:return:
		"""
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
	
	def test_split(self):
		"""
		
		:return:
		"""
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		# check that s.split fails when the separator is not a string
		with self.assertRaises(TypeError):
			s.split(2)


if __name__ == '__main__':
	unittest.main()
