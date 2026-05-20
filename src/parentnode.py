from htmlnode import *

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag=tag, children=children, props=props)

	def to_html(self):
		if self.tag == None:
			raise ValueError("must have a tag")
		if self.children == None or self.children == []:
			raise ValueError("must have children")

		string_to_return = "<" + self.tag + self.props_to_html() + ">"
		suffix = "</" + self.tag + ">"
		for child in self.children:
			string_to_return += child.to_html()
		string_to_return += suffix
		return string_to_return
