import unittest
from text_to_textnodes import *
from textnode import *

class TestTextToTextNodes(unittest.TestCase):
	# test text with bold, italic, and code text
	def test_1(self):
		expected = [
		TextNode("a ", TextType.TEXT),
		TextNode("crazy chimp", TextType.BOLD),
		TextNode(" that acts like ", TextType.TEXT),
		TextNode("such a chump", TextType.ITALIC),
		TextNode(" that i scream like this: ", TextType.TEXT),
		TextNode("scream.play(scream)", TextType.CODE)
		]
		actual = text_to_text_nodes("a **crazy chimp** that acts like _such a chump_ that i scream like this: `scream.play(scream)`")
		self.assertEqual(expected, actual)
	# same
	def test_2(self):
		expected = [
		TextNode("you are so annoying", TextType.ITALIC),
		TextNode(" when you ", TextType.TEXT),
		TextNode("button:onpress:play.thucco:end", TextType.CODE),
		TextNode("thucco thucco that i ", TextType.TEXT),
		TextNode("burp!!!!!", TextType.BOLD)
		]
		actual = text_to_text_nodes("_you are so annoying_ when you `button:onpress:play.thucco:end`thucco thucco that i **burp!!!!!**")
		self.assertEqual(expected, actual)
	# test text with image and link text
	def test_3(self):
		expected = [
		TextNode("if you want to code do the code website oogabooga ", TextType.TEXT),
		TextNode("ooga booga guy", TextType.IMAGE, "www.oogabooga.com/logo"),
		TextNode(" with this link: ", TextType.TEXT),
		TextNode("ooga booga: learn to code", TextType.LINK, "www.oogabooga.com/code"),
		TextNode(" where you Kode like a King!", TextType.TEXT)
		]
		actual = text_to_text_nodes("if you want to code do the code website oogabooga ![ooga booga guy](www.oogabooga.com/logo) with this link: [ooga booga: learn to code](www.oogabooga.com/code) where you Kode like a King!")
		self.assertEqual(expected, actual)
	# same
	def test_4(self):
		expected = [
		TextNode("link to images: ", TextType.TEXT),
		TextNode("link to images", TextType.LINK, "link.image.illuminadi"),
		TextNode(" and image of links: ", TextType.TEXT),
		TextNode("image of links", TextType.IMAGE, "image.link.illuminadi")
		]
		actual = text_to_text_nodes("link to images: [link to images](link.image.illuminadi) and image of links: ![image of links](image.link.illuminadi)")
		self.assertEqual(expected, actual)
	# test text with every type
	def test_5(self):
		expected = [
		TextNode("text", TextType.TEXT),
		TextNode("bold", TextType.BOLD),
		TextNode("italic", TextType.ITALIC),
		TextNode("code", TextType.CODE),
		TextNode("image", TextType.IMAGE, "image.net"),
		TextNode("link", TextType.LINK, "link.net")
		]
		actual = text_to_text_nodes("text**bold**_italic_`code`![image](image.net)[link](link.net)")
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()
