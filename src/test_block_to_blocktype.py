import unittest
from blocktype import *
from block_to_blocktype import *

class TestBlockToBlockType(unittest.TestCase):
	# test fake heading
	def test_1(self):
		md = """####### Not a heading"""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# same
	def test_2(self):
		md = """#Still not a heading"""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test heading
	def test_3(self):
		md = """### Finally a heading"""
		expected = BlockType.HEADING
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test code block
	def test_4(self):
		md = """```
for funny in funnies {
print funny}

do{wow} while 1 < 2 - 1
```"""
		expected = BlockType.CODE
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test fake quote
	def test_5(self):
		md = """> Quote from
> the Communist
> dictator
> that is actually
- PROPAGANDA (so not a quote)"""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test quote
	def test_6(self):
		md = """> Finally
> a
> not fake
> quote
> !!
> YAHOO!"""
		expected = BlockType.QUOTE
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test fake unordered list
	def test_7(self):
		md = """- This is
- an unordered
- list that is
-fake"""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# same
	def test_8(self):
		md = """- Sigh.
- Try again.
- To make.
- An unordered.
- List.
1. TRAGEDY! We failed. Waaa."""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test unordered list
	def test_9(self):
		md = """- Big
- Fat
- Ugly
- Red
- Hot
- Boiling
- Nose
- Hooray! We made an unordered list!"""
		expected = BlockType.UNORDERED_LIST
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test fake ordered list
	def test_10(self):
		md = """1. C-3PO: R2, this is such a drag!
2. R2D2: weewahwoowuaaah
3. C-3PO: R2, this is a complete disaster!
> wind blows and C-3PO says R2!!!"""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# same
	def test_11(self):
		md = """1. a
2. b
3. c
5. d"""
		expected = BlockType.PARAGRAPH
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)
	# test ordered list
	def test_12(self):
		md = """1. One
2. Two
3. Three
4. Four
5. Five
6. Six"""
		expected = BlockType.ORDERED_LIST
		actual = block_to_blocktype(md)
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()
