import sys
from copypaste_directories import *
from generatepages_recursive import *

basepath = "/"
if len(sys.argv) > 1:
	basepath = sys.argv[1]

def main():
	copy_paste_directories("static", "docs")
	generate_pages_recursive("content", "template.html", "docs", basepath)

main()
