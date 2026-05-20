from blocktype import *

def block_to_blocktype(block):
	if block.startswith("#") and not block.startswith("#######") and block.lstrip("#").startswith(" "):
		return BlockType.HEADING
	elif block.startswith("```\n") and block.endswith("```"):
		return BlockType.CODE
	else:
		quote, u_list, o_list = True, True, 0
		for line in block.splitlines():
			if line.startswith(">"):
				u_list = False
				o_list = -123456789
			elif line.startswith("- "):
				quote = False
				o_list = -123456789
			elif line.startswith(str(o_list+1) + ". "):
				quote = False
				u_list = False
				o_list += 1
			else:
				quote = False
				u_list = False
				o_list = -123456789

		if quote:
			return BlockType.QUOTE
		elif u_list:
			return BlockType.UNORDERED_LIST
		elif o_list > 0:
			return BlockType.ORDERED_LIST
	return BlockType.PARAGRAPH
