from copypaste_directories import *
from generatepages_recursive import *

def main():
	copy_paste_directories("static", "public")
	generate_pages_recursive("content", "template.html", "public")

main()
