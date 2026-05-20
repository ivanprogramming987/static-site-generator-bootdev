import unittest
from markdowntoblocks import *

class TestMarkdownToBlocks(unittest.TestCase):
	# test
	def test_1(self):
		md = """
# Frogs in Markdown

frogs are funny and
can be expressed
like this:

<f|<frogtext>|f>

- a list of frogs is
- <f|funny|f>
- and
- <f|cool|f>

wow
"""
		expected = [
		"# Frogs in Markdown",
		"frogs are funny and\ncan be expressed\nlike this:",
		"<f|<frogtext>|f>",
		"- a list of frogs is\n- <f|funny|f>\n- and\n- <f|cool|f>",
		"wow"
		]
		actual = markdown_to_blocks(md)
		self.assertEqual(expected, actual)
	# test with bad markdown
	def test_2(self):
		md = """
# Wedgies With Wild Woozles

alliterative angry avaricious alligator
zinger zings zebras


wer-e-wer-e-waah

!iscool when bigfatuglyredhotboilingnoses     

                                         are great

           wahoo               
"""
		expected = [
		"# Wedgies With Wild Woozles",
		"alliterative angry avaricious alligator\nzinger zings zebras",
		"wer-e-wer-e-waah",
		"!iscool when bigfatuglyredhotboilingnoses",
		"are great",
		"wahoo"
		]
		actual = markdown_to_blocks(md)
	# same
	def test_3(self):
		md = """
# Voyager 2 trip:


...empty space...


Jupiter
Saturn


...empty space...


Uranus

...a lot of emptiness...


Neptune

...to infinity and beyond...

 forever. 
"""
		expected = [
		"# Voyager 2 trip:",
		"...empty space...",
		"Jupiter\nSaturn",
		"...empty space...",
		"Uranus",
		"...a lot of emptiness...",
		"Neptune",
		"...to infinity and beyond...",
		"forever."
		]
		actual = markdown_to_blocks(md)
		self.assertEqual(expected, actual)
	# same
	def test_4(self):
		md = """
# Ugly Mario


ugly mario is so ugly that he is a freak
when he looks at anyone they X)


Ugly Mario is
- scary
- wild
- unpredictable
- EeEeEeEeEeEeK!

when you meet him
don't shake his hand


if you do he will kill you

         wow              
"""
		expected = [
		"# Ugly Mario",
		"ugly mario is so ugly that he is a freak\nwhen he looks at anyone they X)",
		"Ugly Mario is\n- scary\n- wild\n- unpredictable\n- EeEeEeEeEeEeK!",
		"when you meet him\ndon't shake his hand",
		"if you do he will kill you",
		"wow"
		]
		actual = markdown_to_blocks(md)
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()
