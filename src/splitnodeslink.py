from textnode import *
from extractmarkdownlinks import *

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		nodes_to_extend = []
		markdown_links = extract_markdown_links(node.text)
		original_text = node.text
		if node.text_type != TextType.TEXT:
			nodes_to_extend.append(node)
		else:
			while True:
				if len(markdown_links) == 0:
					break
				link = markdown_links.pop(0)
				splitted = original_text.split(f"[{link[0]}]({link[1]})", 1)
				if len(splitted) != 2:
					break
				if splitted[0] != "":
					nodes_to_extend.append(TextNode(splitted[0], TextType.TEXT))
				if link[0] != "" and link[1] != "":
					nodes_to_extend.append(TextNode(link[0], TextType.LINK, link[1]))
				original_text = splitted[1]
			if original_text != "":
				nodes_to_extend.append(TextNode(original_text, TextType.TEXT))
		new_nodes.extend(nodes_to_extend)
	return new_nodes
# Iteration 1: find link1
# split on "![link1](url1)" with maxsplit=1
# left  = "Hello "
# right = " middle [link2](url2) end"
# append TextNode("Hello ", TEXT)
# append TextNode("link1", LINK, "url1")
# original_text = right  <-- move forward!

# Iteration 2: find link2
# split on "[link2](url2)" with maxsplit=1
# left  = " middle "
# right = " end"
# append TextNode(" middle ", TEXT)
# append TextNode("link2", LINK, "url2")
# original_text = right

# After loop: original_text = " end" (not empty, so append it)
# append TextNode(" end", TEXT)
