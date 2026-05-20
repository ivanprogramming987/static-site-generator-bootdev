import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
	# Check if two nodes are equal
	def test_1(self):
		node = TextNode("Dummy italic node", TextType.ITALIC)
		node2 = TextNode("Dummy italic node", TextType.ITALIC)
		self.assertEqual(node, node2)
	# Check if two nodes are inequal because of different type
	def test_2(self):
		node = TextNode("Bold node", TextType.BOLD)
		node2 = TextNode("Bold node", TextType.TEXT)
		self.assertNotEqual(node, node2)
	# Check if two nodes are inequal because of different alt text
	def test_3(self):
		node = TextNode("Node 1", TextType.TEXT)
		node2 = TextNode("Node 2", TextType.TEXT)
		self.assertNotEqual(node, node2)
	# Check if two nodes are inequal because of different URL
	def test_4(self):
		node = TextNode("Cat website", TextType.LINK, "cats.com")
		node2 = TextNode("Cat website", TextType.LINK, "cats.org")
		self.assertNotEqual(node, node2)

if __name__ == "__main__":
	unittest.main()
