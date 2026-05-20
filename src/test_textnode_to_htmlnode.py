import unittest
from textnode import *
from leafnode import *
from textnode_to_htmlnode import *

class TestTextNodeToHTMLNode(unittest.TestCase):
	# test a text node with plain text
	def test_1(self):
		node = TextNode("plain", TextType.TEXT)
		htmlnode = text_node_to_html_node(node)
		self.assertEqual(htmlnode.tag, None)
		self.assertEqual(htmlnode.value, "plain")
	# test a text node with bold text
	def test_2(self):
		node = TextNode("bold", TextType.BOLD)
		htmlnode = text_node_to_html_node(node)
		self.assertEqual(htmlnode.tag, "b")
		self.assertEqual(htmlnode.value, "bold")
	# test a text node with italic text
	def test_3(self):
		node = TextNode("italic", TextType.ITALIC)
		htmlnode = text_node_to_html_node(node)
		self.assertEqual(htmlnode.tag, "i")
		self.assertEqual(htmlnode.value, "italic")
	# test a text node with code text
	def test_4(self):
		node = TextNode("code", TextType.CODE)
		htmlnode = text_node_to_html_node(node)
		self.assertEqual(htmlnode.tag, "code")
		self.assertEqual(htmlnode.value, "code")
	# test a text node with a hyperlink
	def test_5(self):
		node = TextNode("link", TextType.LINK, url="nosesandfrogs.com")
		htmlnode = text_node_to_html_node(node)
		self.assertEqual(htmlnode.tag, "a")
		self.assertEqual(htmlnode.value, "link")
		self.assertEqual(htmlnode.props, {"href": "nosesandfrogs.com"})
	# test a text node with an image
	def test_6(self):
		node = TextNode("frog logo", TextType.IMAGE, url="nosesandfrogs.com/froglogo")
		htmlnode = text_node_to_html_node(node)
		self.assertEqual(htmlnode.tag, "img")
		self.assertEqual(htmlnode.value, "")
		self.assertEqual(htmlnode.props, {"src": "nosesandfrogs.com/froglogo", "alt": "frog logo"})
	# test a text node with an error
	def test_7(self):
		node = TextNode("bad text node", "badcop")
		error = False
		try:
			html_node = text_node_to_html_node(node)
		except Exception as e:
			error = True
		self.assertEqual(error, True)

if __name__ == "__main__":
	unittest.main()
