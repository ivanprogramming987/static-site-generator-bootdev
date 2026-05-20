import unittest
from textnode import *
from splitnodeslink import *
from splitnodesimage import *

class TestSplitNodesLink(unittest.TestCase):
	# test text with a link at the beginning
	def test_1(self):
		expected = [
		TextNode("Everything Pants!", TextType.LINK, "https://everythingpants.com/homepage"),
		TextNode(" is the place to buy the best pants in the world and ", TextType.TEXT),
		TextNode("Everything Undies", TextType.LINK, "https://everythingundies.com/homepage"),
		TextNode(" is where you buy the best undies in the world", TextType.TEXT)
		]
		actual = split_nodes_link([TextNode("[Everything Pants!](https://everythingpants.com/homepage) is the place to buy the best pants in the world and [Everything Undies](https://everythingundies.com/homepage) is where you buy the best undies in the world", TextType.TEXT)])
		self.assertEqual(expected, actual)
	# same, but with a decoy image. text split into two text nodes
	def test_2(self):
		expected = [
		TextNode("Link", TextType.LINK, "link.com/howtohyperlink/hyper/link"),
		TextNode(" and ![Picture](scam.pic.com)", TextType.TEXT)
		]
		actual = split_nodes_link([TextNode("[Link](link.com/howtohyperlink/hyper/link)", TextType.TEXT),
		TextNode(" and ![Picture](scam.pic.com)", TextType.TEXT)])
		self.assertEqual(expected, actual)
	# test text with no link at the beginning
	def test_3(self):
		expected = [
		TextNode("how do you be ", TextType.TEXT),
		TextNode("funny?", TextType.LINK, "www.wikipedia.com/funny"),
		TextNode("Go to ", TextType.TEXT),
		TextNode("funny school", TextType.LINK, "www.funnyschool.com"),
		TextNode("! Pay only $99.99 a month!", TextType.TEXT)
		]
		actual = split_nodes_link([TextNode("how do you be [funny?](www.wikipedia.com/funny)Go to [funny school](www.funnyschool.com)! Pay only $99.99 a month!", TextType.TEXT)])
		self.assertEqual(expected, actual)
	# same, but text split into two text nodes
	def test_4(self):
		expected = [
		TextNode("bad boy land where ", TextType.TEXT),
		TextNode("bad boys", TextType.LINK, "badwiki.badboys"),
		TextNode(" are bad bad bad! ", TextType.TEXT),
		TextNode("bad", TextType.LINK, "badwiki.bad")
		]
		actual = split_nodes_link([TextNode("bad boy land where [bad boys](badwiki.badboys)", TextType.TEXT),
		TextNode(" are bad bad bad! [bad](badwiki.bad)", TextType.TEXT)
		])
		self.assertEqual(expected, actual)

class TestSplitNodesImage(unittest.TestCase):
	# test text with an image at the beginning and a faulty image
	def test_1(self):
		expected = [
		TextNode("wildwedgie", TextType.IMAGE, "www.images.com/wildwedgie0574"),
		TextNode(" is the wildest wedgie! [amazing](undies) prevent ", TextType.TEXT),
		TextNode("wildwedgies", TextType.IMAGE, "www.images.com/wildwedgies0575")
		]
		actual = split_nodes_image([TextNode("![wildwedgie](www.images.com/wildwedgie0574) is the wildest wedgie! [amazing](undies) prevent ![wildwedgies](www.images.com/wildwedgies0575)", TextType.TEXT)])
		self.assertEqual(expected, actual)
	# same, but with a decoy link and no faulty image. text split into two text nodes
	def test_2(self):
		expected = [
		TextNode("Picture", TextType.IMAGE, "picture.com/picture/!"),
		TextNode(" and [Link](scam.link.com)", TextType.TEXT)
		]
		actual = split_nodes_image([TextNode("![Picture](picture.com/picture/!)", TextType.TEXT),
		TextNode(" and [Link](scam.link.com)", TextType.TEXT)
		])
		self.assertEqual(expected, actual)
	# test text with no image at the beginning and two faulty images
	def test_3(self):
		expected = [
		TextNode("Store Eggs ", TextType.TEXT),
		TextNode("eggs!!!", TextType.IMAGE, "https://store.org/eggs"),
		TextNode(" for $5.99! !([!)] Store Cheese ", TextType.TEXT),
		TextNode("cheese!!!", TextType.IMAGE, "https://store.org/cheese"),
		TextNode(" for [!](!)! $5.99", TextType.TEXT)
		]
		actual = split_nodes_image([TextNode("Store Eggs ![eggs!!!](https://store.org/eggs) for $5.99! !([!)] Store Cheese ![cheese!!!](https://store.org/cheese) for [!](!)! $5.99", TextType.TEXT)])
		self.assertEqual(expected, actual)
	# same, but text split into two text nodes
	def test_4(self):
		expected = [
		TextNode("A Fashin Sho Invitation ", TextType.TEXT),
		TextNode("1st Fashin Sho", TextType.IMAGE, "www.images.com/fashinshoA001"),
		TextNode(" to go to a fashin sho (fashion show) where fashion people compete! ", TextType.TEXT),
		TextNode("come to the fashin sho", TextType.IMAGE, "www.images.com/fashinshoB001")
		]
		actual = split_nodes_image([TextNode("A Fashin Sho Invitation ![1st Fashin Sho](www.images.com/fashinshoA001)", TextType.TEXT),
		TextNode(" to go to a fashin sho (fashion show) where fashion people compete! ![come to the fashin sho](www.images.com/fashinshoB001)", TextType.TEXT)
		])
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()
