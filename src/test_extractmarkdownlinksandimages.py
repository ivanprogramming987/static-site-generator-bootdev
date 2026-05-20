import unittest
from extractmarkdownlinks import *
from extractmarkdownimages import *

class TestExtractMarkdownImages(unittest.TestCase):
	# test text with one image
	def test_1(self):
		expected = [("image of pants", "www.pantstime.com/everythingpants")]
		actual = extract_markdown_images(
		"Here is an ![image of pants](www.pantstime.com/everythingpants)"
		)
		self.assertEqual(expected, actual)
	# test text with two images
	def test_2(self):
		expected = [("goofy cat", "www.goofythings.org/cat"), ("goofy dog", "www.goofythings.org/dog")]
		actual = extract_markdown_images(
		"A ![goofy cat](www.goofythings.org/cat) and a ![goofy dog](www.goofythings.org/dog) are the goofiest pets you will ever seeeeeeeeeeeeeeeeeeeee!"
		)
		self.assertEqual(expected, actual)
	# test text with three images
	def test_3(self):
		expected = [("best picture ever", "https://bestpictures.gov/1stplace"), ("second best picture ever", "https://bestpictures.gov/2ndplace"), ("third best picture ever", "https://bestpictures.gov/3rdplace")]
		actual = extract_markdown_images(
		"![best picture ever](https://bestpictures.gov/1stplace) is 1st place, ![second best picture ever](https://bestpictures.gov/2ndplace) is 2nd place, and ![third best picture ever](https://bestpictures.gov/3rdplace) is 3rd place!!! Yay! [evil](evil.illuminadi)"
		)
		self.assertEqual(expected, actual)

class TestExtractMarkdownLinks(unittest.TestCase):
	# test text with one link
	def test_1(self):
		expected = [("Best Clown amazes 98.76% of grouchy people", "www.documentaries.com/bestclownamazes98%ofgrouchypeople")]
		actual = extract_markdown_links(
		"here is a documentary of the best clown in the world: [Best Clown amazes 98.76% of grouchy people](www.documentaries.com/bestclownamazes98%ofgrouchypeople)"
		)
		self.assertEqual(expected, actual)
	# test text with two links
	def test_2(self):
		expected = [("GooTwoO: official doc", "www.science/GooTwoOdoc"), ("The Gooiest Goo Ever", "https://slime.org/thegooiestslimeinhistory")]
		actual = extract_markdown_links(
		"if you want to learn more about Goo2O: check these out: [GooTwoO: official doc](www.science/GooTwoOdoc) and [The Gooiest Goo Ever](https://slime.org/thegooiestslimeinhistory)"
		)
		self.assertEqual(expected, actual)
	# test text with three links
	def test_3(self):
		expected = [("frogs", "www.funnythings.com/frogs"), ("noses", "www.funnythings.com/noses"), ("undies", "www.funnythings.com/undies")]
		actual = extract_markdown_links(
		"[frogs](www.funnythings.com/frogs), [noses](www.funnythings.com/noses), and [undies](www.funnythings.com/undies) are the clear winners, ![not funny](notfunny.illuminadi) each tying at 92.18% funny"
		)
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()
