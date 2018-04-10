#-*- coding:utf-8 -*-
import sys
import os

def cr(filepath, encoding='utf-8'):
	try:
		f = ""
		with open(filepath, 'r', encoding=encoding) as f:
			f = f.read()

		lines = f.splitlines()
		strip_lines = map(lambda x:x.strip(), lines)
		ret = "  \n".join(strip_lines)
		ret = ret.strip()

		with open(filepath, 'w', encoding=encoding) as f:
			f.write(ret)

		print ("success cr ", filepath)

	except Exception as ex:
		print ("cr error", ex)


# test
"""
filename = "README.md"
filepath = r"D:\_my\git\selfhow\md-to-gfm"
fullpath = os.path.join(filepath, filename)

cr(fullpath)
exit()
"""

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("invalid parameter. usage :  md_to_gfm FILEPATH ")		
		exit()

	cr(sys.argv[1])