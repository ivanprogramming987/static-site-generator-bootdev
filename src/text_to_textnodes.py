from splitnodesdelimiter import *
from splitnodeslink import *
from splitnodesimage import *
from textnode import *

def text_to_text_nodes(text):
	text2 = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "**", TextType.BOLD)
	text3 = split_nodes_delimiter(text2, "_", TextType.ITALIC)
	text4 = split_nodes_delimiter(text3, "`", TextType.CODE)
	text5 = split_nodes_link(text4)
	final_text = split_nodes_image(text5)
	return final_text
