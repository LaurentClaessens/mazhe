#!/usr/bin/python3

"""
Replace a $math content$ text sequence into an equivalent \( math content\)

The script expects a file name as first argument. Optional output file name can be the 2nd argument.

Usage : sys.argv[0] input_file [output_file]

Author: Alain Vigne
"""

import  sys
# Importing regex module
import  re

# Creating a function to replace the text
def replacetext(file_in, file_out):

  data_out  = [None, None]
  # Opening the files in read and write mode
  with open(file_in, 'r') as f:

    # Reading the file data and store it in a variable
    data  = f.read()

    # Replacing the pattern with the string in the file data
    data_out  = re.subn('\$(?P<content>[^\$]*)\$', r'\( \g<content>\)', data, flags=re.DOTALL)

    # Writing replaced data in the output file
    fout = open(file_out, 'w')
    fout.write(data_out[0])

  return  data_out[1]

# Main function
def main(argv):
  inputfile   = None
  outputfile  = None
  l           = len(sys.argv)

  # Check arguments
  if l == 2:
    inputfile   = sys.argv[1]
    outputfile  = inputfile + ".new"
  elif l == 3:
    inputfile   = sys.argv[1]
    outputfile  = sys.argv[2]

  if inputfile is None:
    print ('Error: no input filename.')
    print ('  No change occured.')
  else:
    print ('Input filename   : ', str(inputfile))
    print ('Output filename  : ', str(outputfile))
    nb_subst = replacetext (inputfile, outputfile)
    print (str(nb_subst) + ' substitution(s).')


if __name__ == "__main__":
  main(sys.argv[1:])
