import unittest
from leafnode import *

class TestLeafNode(unittest.TestCase):
	# test without a tag
	def test_1(self):
		expected_node = "This is raw text"
		leaf_node = LeafNode(None, "This is raw text")
		actual_node = leaf_node.to_html()
		self.assertEqual(expected_node, actual_node)
	# test with a tag and without props
	def test_2(self):
		expected_node = "<p>This is a paragraph of text</p>"
		leaf_node = LeafNode("p", "This is a paragraph of text")
		actual_node = leaf_node.to_html()
		self.assertEqual(expected_node, actual_node)
	# test with a tag and with props
	def test_3(self):
		expected_node = '<a href="supersonicpants.com">Click to order pants</a>'
		leaf_node = LeafNode("a", "Click to order pants", props={"href": "supersonicpants.com"})
		actual_node = leaf_node.to_html()
		self.assertEqual(expected_node, actual_node)

if __name__ == "__main__":
	unittest.main()
