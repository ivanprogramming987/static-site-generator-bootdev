import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
	# test the props_to_html method
	def test_1(self):
		expected_props = ' href="wedgie.com" target="atomic wedgie"'
		html_node = HTMLNode(props={"href": "wedgie.com", "target": "atomic wedgie"})
		actual_props = html_node.props_to_html()
		self.assertEqual(expected_props, actual_props)
	# same
	def test_2(self):
		expected_props = ' href="tootyfrooty.gov" target="secret stinkbomb"'
		html_node = HTMLNode(props={"href": "tootyfrooty.gov", "target": "secret stinkbomb"})
		actual_props = html_node.props_to_html()
		self.assertEqual(expected_props, actual_props)
	# test if the props_to_html method works without props
	def test_3(self):
		expected_props = ''
		html_node = HTMLNode()
		actual_props = html_node.props_to_html()
		self.assertEqual(expected_props, actual_props)
