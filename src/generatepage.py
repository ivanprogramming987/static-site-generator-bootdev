import os
from extracttitle import *
from markdowntohtmlnode import *

def generate_page(from_path, template_path, dest_path):
	print(f"Generating a page from {from_path} to {dest_path} using {template_path}...")
	with open(from_path, "r") as f:
		markdown = f.read()
	with open(template_path, "r") as f:
		template = f.read()
	title = extract_title(markdown)
	html = markdown_to_htmlnode(markdown).to_html()
	full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
	# need to make directories
	directories = os.path.dirname(dest_path)
	os.makedirs(directories, exist_ok=True)
	with open(dest_path, "w") as f:
		f.write(full_html)



