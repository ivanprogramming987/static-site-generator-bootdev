import unittest
from extracttitle import *

class TestExtractTitle(unittest.TestCase):
	# test that extracting a title returns the title with all whitespace and "#" characters stripped
	def test_1(self):
		md = """# Title
text of murderous intent
"""
		expected = "Title"
		actual = extract_title(md)
		self.assertEqual(expected, actual)
	# same
	def test_2(self):
		md = """# Also a title.                      
more text of murderous intent
"""
		expected = "Also a title."
		actual = extract_title(md)
		self.assertEqual(expected, actual)
	# test text with an invalid title
	def test_3(self):
		md = "The world will blow up if this text does not raise an error."
		error = False
		try:
			actual = extract_title(md)
		except Exception as e:
			error = True
		self.assertEqual(error, True)
	# same
	def test_4(self):
		md = """###### Spiffy Pair of Pants
dis teksst no hav no ty till
"""
		error = False
		try:
			actual = extract_title(md)
		except Exception as e:
			error = True
		self.assertEqual(error, True)
	# test text with an empty first line
	def test_5(self):
		md = """
# Teacher: Title, if you move ONE INCH out of line, the school will blow up!
KA BOOM
"""
		error = False
		try:
			actual = extract_title(md)
		except Exception as e:
			error = True
		self.assertEqual(error, True)

if __name__ == "__main__":
	unittest.main()
