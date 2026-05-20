from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		nodes_to_extend = []
		if node.text_type != TextType.TEXT:
			nodes_to_extend.append(node)
		else:
			if node.text.count(delimiter) % 2 == 1:
				raise Exception("invalid markdown syntax")
			text = node.text.split(delimiter)
			node_type = text_type if node.text.startswith(delimiter) else TextType.TEXT
			for item in text:
				if item != "":
					nodes_to_extend.append(TextNode(item, node_type))
					node_type = text_type if node_type == TextType.TEXT else TextType.TEXT
		new_nodes.extend(nodes_to_extend)
	return new_nodes
