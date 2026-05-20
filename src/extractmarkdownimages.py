import re

def extract_markdown_images(text):
	matches = re.findall(r"!\[.*?\]\(.*?\)", text)
	tuples = []
	for match in matches:
		alt_txt = ""
		url = ""
		transfer = ""
		for i in range(2, len(match)-1):
			char = match[i]
			if char == "]" or char == "(":
				transfer += char
			elif transfer != "](":
				alt_txt += char
			else:
				url += char
		tuples.append((alt_txt, url))
	return tuples
