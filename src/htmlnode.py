class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		string_to_return = ''
		if self.props == None or self.props == {}:
			return ""
		for key in self.props:
			val = self.props[key]
			string_to_return += " " + key + '="' + val + '"'
		return string_to_return

	def __repr__(self):
		str1 = "tag:" + self.tag if self.tag != None else "tag:None"
		str2 = "value:" + self.value if self.value != None else "value:None"
		str3 = "children:" + self.children if self.children != None else "children:None"
		str4 = "props:" + self.props if self.props != None else "props:None"
		return "HTMLNode(" + str1 + ", " + str2 + ", " + str3 + ", " + str4 + ")"
