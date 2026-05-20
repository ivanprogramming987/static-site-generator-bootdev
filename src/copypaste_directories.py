import os
import shutil

def copy_paste_directories(source, destination, dirs=[]): # makes destination an exact copy of source
	if not os.path.exists(source):
		raise Exception(f"directory {source} does not exist")
	if not os.path.exists(destination):
		raise Exception(f"directory {destination} does not exist")
	shutil.rmtree(destination)
	os.mkdir(destination)
	items = os.listdir(source)
	for item in items:
		if os.path.isdir(f"{source}/{item}") and f"{source}/{item}" not in dirs:
			os.mkdir(f"{destination}/{item}")
			dirs.append(f"{source}/{item}")
			copy_paste_directories(os.path.join(source, item), os.path.join(destination, item))
		else:
			shutil.copy(f"{source}/{item}", destination)


"""
steps:
destroy destination
make destination again without any files
copy all files from source to destination
"""
