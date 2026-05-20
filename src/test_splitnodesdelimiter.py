import unittest
from textnode import *
from splitnodesdelimiter import *

class TestSplitNodesDelimiter(unittest.TestCase):
	# test the text "oh _my!_ this is _terrible!_"
	def test_1(self):
		expected = [
		TextNode("oh ", TextType.TEXT),
		TextNode("my!", TextType.ITALIC),
		TextNode(" this is ", TextType.TEXT),
		TextNode("terrible!", TextType.ITALIC)
		]
		text = TextNode("oh _my!_ this is _terrible!_", TextType.TEXT)
		actual = split_nodes_delimiter([text], "_", TextType.ITALIC)
		self.assertEqual(expected, actual)
	# test the text "give that to me **right now!!** or **die.**"
	def test_2(self):
		expected = [
		TextNode("give that to me ", TextType.TEXT),
		TextNode("right now!!", TextType.BOLD),
		TextNode(" or ", TextType.TEXT),
		TextNode("die.", TextType.BOLD)
		]
		text = TextNode("give that to me **right now!!** or **die.**", TextType.TEXT)
		actual = split_nodes_delimiter([text], "**", TextType.BOLD)
		self.assertEqual(expected, actual)
	# test two nodes. text: "`for uglin in uglins print uglin`you stinky `secret word`"
	def test_3(self):
		expected = [
		TextNode("for uglin in uglins print uglin", TextType.CODE),
		TextNode("you stinky ", TextType.TEXT),
		TextNode("secret word", TextType.CODE)
		]
		text1 = TextNode("for uglin in uglins print uglin", TextType.CODE)
		text2 = TextNode("you stinky `secret word`", TextType.TEXT)
		actual = split_nodes_delimiter([text1, text2], "`", TextType.CODE)
		self.assertEqual(expected, actual)
	# test three nodes. text: "waluwedgie**@waluwedgie.com** waluigi gets a wedgie **or else**"
	def test_4(self):
		expected = [
		TextNode("waluwedgie", TextType.TEXT),
		TextNode("@waluwedgie.com", TextType.BOLD),
		TextNode(" waluigi gets a wedgie ", TextType.TEXT),
		TextNode("or else", TextType.BOLD)
		]
		text1 = TextNode("waluwedgie**@waluwedgie.com**", TextType.TEXT)
		text2 = TextNode(" waluigi gets a wedgie ", TextType.TEXT)
		text3 = TextNode("or else", TextType.BOLD)
		actual = split_nodes_delimiter([text1, text2, text3], "**", TextType.BOLD)
		self.assertEqual(expected, actual)
	# test the text "_yikes!_ A monster _broke open the door_ and came in!"
	def test_5(self):
		expected = [
		TextNode("yikes!", TextType.ITALIC),
		TextNode(" A monster ", TextType.TEXT),
		TextNode("broke open the door", TextType.ITALIC),
		TextNode(" and came in!", TextType.TEXT)
		]
		text = TextNode("_yikes!_ A monster _broke open the door_ and came in!", TextType.TEXT)
		actual = split_nodes_delimiter([text], "_", TextType.ITALIC)
		self.assertEqual(expected, actual)
	# test a node with an error
	def test_6(self):
		text = TextNode("**error text?!", TextType.TEXT)
		error = False
		try:
			actual = split_nodes_delimiter([text], "**", TextType.TEXT)
		except Exception as e:
			error = True
		self.assertEqual(error, True)

if __name__ == "__main__":
	unittest.main()
