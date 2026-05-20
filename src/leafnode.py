from htmlnode import HTMLNode

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag=tag, value=value, props=props)

	def to_html(self):
		if self.value == None:
			raise ValueError("leaf nodes must have a value")
		if self.tag == None:
			return self.value
		prefix = "<" + self.tag + self.props_to_html() + ">"
		suffix = "</" + self.tag + ">"
		return prefix + self.value + suffix

	def __repr__(self):
		str1 = "tag:" + self.tag if self.tag != None else "tag:None"
		str2 = "value:" + self.value if self.value != None else "value:None"
		str3 = "props:" + self.props if self.props != None else "props:None"
		return "HTMLNode(" + str1 + ", " + str2 + ", " + str3 + ")"
