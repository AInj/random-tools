# Recursively adds a header to all files (for copyright or so), optionally skips first lines containing a specific string (e.g `<?php`)

import sys
import os

def affect(file, find, apply):
	newlines = []

	with open(file, 'r') as fr:
		lines = fr.readlines()
		fl = False

		for line in lines:
			if len(find) > 0:
				if find in line:
					line = line.replace(find, apply)
			else:
				if fl == False:
					line = apply + line
					fl = True
			newlines.append(line)

	with open(file, 'w') as fw:
		for line in newlines:
			fw.write(line)

def main():
	argv = sys.argv
	if len(argv) < 4:
		print "USAGE: {} <working-dir> <file-ext> <file-to-apply> <(\"first-line\")>".format(argv[0])
		sys.exit(1)

	find = ''
	try: find = argv[4]
	except IndexError: find = ''

	apply = ''
	if os.path.isfile(argv[3]):
		af = open(argv[3], 'r')
		apply = find + af.read()
	else:
		print "ERROR: File `{}` is unreachable".format(argv[3])
		sys.exit(1)

	print "> Running application on `{}` -> `{}`...".format(argv[3], argv[1])
	if find != '':
		print "> Skipping first line containing `{}`".format(find)

	for dir_info in os.walk(argv[1]):
		for file in dir_info[2]:
			if file.endswith(argv[2]):
				abs = os.path.abspath(os.path.join(dir_info[0], file))
				print ">> Affecting `{}`".format(abs)
				affect(abs, find, apply)

if __name__ == '__main__':
	main()