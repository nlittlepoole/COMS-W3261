#!/usr/bin/env python
import sys

def main(filename):
	text_file = open(filename)
	text_list = text_file.readlines()
	text_file.close()
	length = 0
	answer = ""
	for line in text_list:
		if len(line) > length:
		    length = len(line)
		    answer = line.rstrip()
	print(answer + ", " + str(length))

if __name__ == '__main__':
	main(sys.argv[1])