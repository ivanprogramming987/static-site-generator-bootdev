def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	finalized_blocks = []
	for block in blocks:
		block = block.strip()
		if block != "":
			finalized_blocks.append(block)
	return finalized_blocks
