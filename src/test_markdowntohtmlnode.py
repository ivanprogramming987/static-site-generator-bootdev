import unittest
from htmlnode import *
from leafnode import *
from parentnode import *
from markdowntohtmlnode import *

class TestMarkdownToHTMLNode(unittest.TestCase):
	# this test file tests that i can write easy-to-understand Markdown and poof! it is HTML ready for the computer
	# test all headings
	def test_1(self):
		md = """
# Gross Errors

## Errors are

### quite gross and disgusting

#### like this:

##### frogs are not funny

###### not good. the world will blow up.
"""
		expected = "<div><h1>Gross Errors</h1><h2>Errors are</h2><h3>quite gross and disgusting</h3><h4>like this:</h4><h5>frogs are not funny</h5><h6>not good. the world will blow up.</h6></div>"
		node = markdown_to_htmlnode(md)
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test code block
	def test_2(self):
		md = """
```
code **that** will obstinately
_not change_ no matter what.
even with a ![nose image](nose) or [nose link](nose)
```
"""
		expected = "<div><pre><code>code **that** will obstinately\n_not change_ no matter what.\neven with a ![nose image](nose) or [nose link](nose)\n</code></pre></div>"
		node = markdown_to_htmlnode(md)
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test unordered list and ordered list
	def test_3(self):
		md = """
- unordered
- list
- of
- mayhem

1. order
2. in
3. the
4. list
5. order!
"""
		expected = "<div><ul><li>unordered</li><li>list</li><li>of</li><li>mayhem</li></ul><ol><li>order</li><li>in</li><li>the</li><li>list</li><li>order!</li></ol></div>"
		node = markdown_to_htmlnode(md)
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test quote and paragraph
	def test_4(self):
		self.maxDiff = None
		md = """
To quote the King Of All Frogs:

> ribbit
> bibbit
> boing

**His royal highness** wants you
to come _this instant!_
And _watch out_, His majesty
has a **quick temper!**
He specifically said:

> come
> this
> instant
> or u r ded
"""
		expected = "<div><p>To quote the King Of All Frogs:</p><blockquote>ribbit bibbit boing</blockquote><p><b>His royal highness</b> wants you to come <i>this instant!</i> And <i>watch out</i>, His majesty has a <b>quick temper!</b> He specifically said:</p><blockquote>come this instant or u r ded</blockquote></div>"
		node = markdown_to_htmlnode(md)
		actual = node.to_html()
		self.assertEqual(expected, actual)
	# test a full document with every block type and every text type
	def test_5(self):
		md = """
# Finl Bos

###### Very Hard

> NPC777: This is it.
> NPC771: The Final Boss!

Game Stats:
Boss HP: **999999**
Boss Magic: _100%_
Boss Strength: `100%`

Other Stats:
Boss Appearance: ![finl bos](www.images.com/finlbos1234)
Link To Fight Boss: [finl bos fight](game0123.com/finlbosfight)

Boss Weaknesses:

- this boss
- is so strong
- that he has
- no weakness

Boss Attacks:

1. Super Swing
2. Crown Crush
3. Star Magic
4. Twitch Out Rage

```
**Wow!**
_This is the hardest Boss_
in history!
```
"""
		expected = '<div><h1>Finl Bos</h1><h6>Very Hard</h6><blockquote>NPC777: This is it. NPC771: The Final Boss!</blockquote><p>Game Stats: Boss HP: <b>999999</b> Boss Magic: <i>100%</i> Boss Strength: <code>100%</code></p><p>Other Stats: Boss Appearance: <img src="www.images.com/finlbos1234" alt="finl bos"></img> Link To Fight Boss: <a href="game0123.com/finlbosfight">finl bos fight</a></p><p>Boss Weaknesses:</p><ul><li>this boss</li><li>is so strong</li><li>that he has</li><li>no weakness</li></ul><p>Boss Attacks:</p><ol><li>Super Swing</li><li>Crown Crush</li><li>Star Magic</li><li>Twitch Out Rage</li></ol><pre><code>**Wow!**\n_This is the hardest Boss_\nin history!\n</code></pre></div>'
		node = markdown_to_htmlnode(md)
		actual = node.to_html()
		self.assertEqual(expected, actual)


if __name__ == "__main__":
	unittest.main()
