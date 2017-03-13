# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
# MIPS Assembly to Hex Converter. 													 		     |
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
# Akshay Kashyap, Union College, Winter 2017. 										 			 |
# Built using code by Prof. John Rieffel, Union College, for CSC-270: Compiter Organization. 	 |
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

import sys

from InstructionParser import InstructionParser

class Assembler(object):
	def __init__(self, infilename, outfilename):
		self.infilename = infilename
		self.outfilename = outfilename

		self.parser = InstructionParser()

	def AssemblyToHex(self):
		'''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
		then save that machinecode to an outputfile'''
		outlines = []
		with open(self.infilename) as f:
			lines = [line.rstrip() for line in f.readlines()]  #get rid of \n whitespace at end of line
			#if you are a python ninja, use list comprehension. and replace the for loop below
			# with this expression
			#outlines = [ConvertAssemblyToMachineCode(curline) for curline in lines]
			# but, no judgement if you prefer explicit for loops
			for curline in lines:
				print curline
				outstring = self.parser.convert(curline, format='hex')
				if outstring != '':
					outlines.append(outstring)

		f.close()

		with open(self.outfilename,'w') as of:
			of.write('v2.0 raw\n')
			for outline in outlines:
				of.write(outline)
				of.write("\n")
		of.close()

if __name__ == "__main__":
	#in order to run this with command-line arguments
	# we need this if __name__ clause
	# and then we need to read in the subsequent arguments in a list.

	#### These two lines show you how to iterate through arguments ###
	#### You can remove them when writing your own assembler
	print 'Number of arguments:', len(sys.argv), 'arguments.'
	print 'Argument List:', str(sys.argv)

	## This is error checking to make sure the correct number of arguments were used
	## you'll have to change this if your assembler takes more or fewer args
	if (len(sys.argv) != 3):
		print('usage: python akshay-assembler.py inputfile.asm outputfile.hex')
		exit(0)
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]

	assembler = Assembler(inputfile, outputfile)
	assembler.AssemblyToHex()
