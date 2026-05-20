import unittest
from parentnode import *
from leafnode import *

class TestParentNode(unittest.TestCase):
	# test a node with multiple children
	def test_1(self):
		expected = "<p><n>nose</n>frog<d>dipuh</d></p>"
		node = ParentNode("p",
		[LeafNode("n", "nose"),
		LeafNode(None, "frog"),
		LeafNode("d", "dipuh")
		])
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test a node with a grandchild
	def test_2(self):
		expected = "<p><x><i>italic from italy</i></x></p>"
		node = ParentNode("p",
		[ParentNode("x",[
		LeafNode("i", "italic from italy")
		])])
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test a node without children
	def test_3(self):
		node = ParentNode("error king", None)
		error = False
		try:
			actual = node.to_html()
		except Exception as e:
			error = True
		self.assertEqual(error, True)
	# test a node without a tag
	def test_4(self):
		node = ParentNode(None, [LeafNode("error", "error prince")])
		error = False
		try:
			actual = node.to_html()
		except Exception as e:
			error = True
		self.assertEqual(error, True)
	# test a node with a childless child
	def test_5(self):
		node = ParentNode("bad guy", [ParentNode("bad boy", None)])
		error = False
		try:
			actual = node.to_html()
		except Exception as e:
			error = True
		self.assertEqual(error, True)
	# test a node with a tagless child
	def test_6(self):
		node = ParentNode("green goblin", [
		ParentNode(None,
		[LeafNode("rhino", "doctor octopus")])
		])
		error = False
		try:
			actual = node.to_html()
		except Exception as e:
			error = True
		self.assertEqual(error, True)
	# test an html with two paragraphs, the first containing encrypted text
	def test_7(self):
		expected = "<html><p><e>hheelllloo</e></p>words</html>"
		node = ParentNode("html",
		[ParentNode("p",
		[LeafNode("e", "hheelllloo")
		]),
		LeafNode(None, "words")
		])
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test a node with a great-grandchild
	def test_8(self):
		expected = "<a><b><c><d>wedgie</d></c></b></a>"
		node = ParentNode("a",
		[ParentNode("b",
		[ParentNode("c",
		[LeafNode("d", "wedgie")
		])])])
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test an html with three paragraphs, the last containing super ugly text
	def test_9(self):
		expected = "<html><p>pants</p>caps for sale<s><u>you uglin</u></s></html>"
		node = ParentNode("html",
		[LeafNode("p", "pants"),
		LeafNode(None, "caps for sale"),
		ParentNode("s", [
		LeafNode("u", "you uglin")
		])])
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test an html with two paragraphs, the first containing very evil text, and the last containing super good text
	def test_10(self):
		expected = "<html><ve>we are thugs</ve><sg>fake fig newtons</sg></html>"
		node = ParentNode("html",
		[ParentNode("ve", [
		LeafNode(None, "we are thugs")
		]),
		ParentNode("sg", [
		LeafNode(None, "fake fig newtons")
		])])
		actual = node.to_html()
		self.assertEqual(expected, actual)


if __name__ == "__main__":
	unittest.main()
