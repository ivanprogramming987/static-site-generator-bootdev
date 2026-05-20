from textnode import *
from extractmarkdownimages import *

def split_nodes_image(old_nodes):
        new_nodes = []
        for node in old_nodes:
                nodes_to_extend = []
                markdown_images = extract_markdown_images(node.text)
                original_text = node.text
                if node.text_type != TextType.TEXT:
                        nodes_to_extend.append(node)
                else:
                        while True:
                                if len(markdown_images) == 0:
                                        break
                                image = markdown_images.pop(0)
                                splitted = original_text.split(f"![{image[0]}]({image[1]})", 1)
                                if len(splitted) != 2:
                                        break
                                if splitted[0] != "":
                                        nodes_to_extend.append(TextNode(splitted[0], TextType.TEXT))
                                if image[0] != "" and image[1] != "":
                                        nodes_to_extend.append(TextNode(image[0], TextType.IMAGE, image[1]))
                                original_text = splitted[1]
                        if original_text != "":
                                nodes_to_extend.append(TextNode(original_text, TextType.TEXT))
                new_nodes.extend(nodes_to_extend)
        return new_nodes
