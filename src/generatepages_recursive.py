import os
import pathlib
from generatepage import *

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
	entries = []
	objects = os.listdir(dir_path_content)
	for obj in objects:
		path = os.path.join(dir_path_content, obj)
		if os.path.isfile(path) and path.endswith(".md"):
			generate_page(path, template_path, f"{dest_dir_path}/{obj.replace('.md', '.html')}", basepath)
		elif os.path.isdir(path):
			os.makedirs(obj, exist_ok=True)
			generate_pages_recursive(path, template_path, f"{dest_dir_path}/{obj}", basepath)
