from block_to_blocktype import *
from blocktype import *
from htmlnode import *
from leafnode import *
from markdowntoblocks import *
from parentnode import *
from textnode import *
from textnode_to_htmlnode import *
from text_to_textnodes import *

def markdown_to_htmlnode(markdown):
	blocks = markdown_to_blocks(markdown)
	nodes = []
	for block in blocks:
		type = block_to_blocktype(block)
		block_node = create_block_node(type, block)
		nodes.append(block_node)
	return ParentNode("div", [node for node in nodes], None)

def find_tag(type, block):
	num = 0
	while block.startswith("#"):
		num += 1
		block = block.removeprefix("#")
	types = {
	BlockType.PARAGRAPH: "p",
	BlockType.QUOTE: "blockquote",
	BlockType.UNORDERED_LIST: "ul",
	BlockType.ORDERED_LIST: "ol",
	BlockType.CODE: "pre",
	BlockType.HEADING: f"h{num}"
	}
	return types[type]

def text_to_children(text):
	html_nodes = []
	text_nodes = text_to_text_nodes(text)
	for text_node in text_nodes:
		html_nodes.append(text_node_to_html_node(text_node))
	return html_nodes

def remove_prefixes(value):
	return value.lstrip("->#1234567890. ")

def create_block_node(type, block):
	tag = find_tag(type, block)
	if tag == "pre":
		sliced = block[4:-3]
		text_node = TextNode(sliced, TextType.CODE)
		html_node = text_node_to_html_node(text_node)
		return ParentNode(tag, [html_node])
	elif tag == "ul" or tag == "ol":
		node = ParentNode(tag, [])
		for line in block.split("\n"):
			children = text_to_children(remove_prefixes(line))
			node.children.append(ParentNode("li", children))
		return node
	elif tag == "blockquote":
		split_block = block.split("\n")
		clean = [remove_prefixes(line) for line in split_block]
		clean_block = " ".join(clean)
		children = text_to_children(clean_block)
		result = ParentNode(tag, children)
		return result
	elif tag == "p":
		children = text_to_children(block.replace("\n", " "))
		return ParentNode(tag, children)
	else:
		children = text_to_children(remove_prefixes(block.replace("\n", " ")))
		return ParentNode(tag, children)
