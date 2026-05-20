def extract_title(markdown):
	lines = markdown.split("\n")
	first_line = lines.pop(0)
	markdown = "\n".join(lines[1:])
	if first_line.startswith("# "):
		return first_line.strip("# ")
	raise Exception("no title to extract")
