# -*- coding: utf8 -*-

import outilsINGE
import sys
attach("exo15.sage")
attach("exo11.sage")
attach("exo13.sage")
attach("exo65.sage")
attach("exo101.sage")
attach("exo103.sage")
attach("exo104.sage")
attach("exo105.sage")
attach("exo106.sage")
attach("exo109.sage")
attach("exo1011.sage")
attach("exoDV002.sage")

class DoubleStdout(object):
	def __init__(self,filename):
		self.exit_file = open(filename,"w")
	def run(self):
		print "From now, we are writing in the file",filename
		self.old_stdout = sys.stdout
		sys.stdout = self
	def stop(self):
		sys.stdout = self.old_stdout
		self.exit_file.close()
		print "From now, we are no more writing in the file",filename
	def write(self,text):
		self.old_stdout.write(text)
		self.exit_file.write(text)

def FunctionToFile(fun,filename):
	"""
	Launch the function <fun> and put the stdout in <filename> as well as on the current sys.stdout (usually : the screen)

	Be careful : this remove the content of <filename>
	"""
	X=DoubleStdout(filename)
	X.run()
	fun()
	X.stop()

FunctionToFile(exercise_10_1_A,"exo101A.txt")
FunctionToFile(exercise_10_1_B,"exo101B.txt")
FunctionToFile(exercise_10_1_C,"exo101C.txt")

FunctionToFile(exercise_10_3_A,"exo103A.txt")
FunctionToFile(exercise_10_3_H,"exo103H.txt")
FunctionToFile(exercise_10_3_Q,"exo103Q.txt")

FunctionToFile(exercise_10_4,"exo104.txt")
FunctionToFile(exercise_10_5,"exo105.txt")
FunctionToFile(exercise_10_6,"exo106.txt")
FunctionToFile(exercise_10_9,"exo109.txt")
FunctionToFile(exercise_10_11,"exo1011.txt")

FunctionToFile(exercise_1_1_bcdefhi,"exo11.txt")
FunctionToFile(exercise_1_3,"exo13.txt")
FunctionToFile(exercise_6_5,"exo65.txt")
FunctionToFile(exercise_1_5,"exo15.txt")
FunctionToFile(exercise_DV002,"exoDV002.txt")
