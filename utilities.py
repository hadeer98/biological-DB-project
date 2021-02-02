#This file contains basic functions, such as: file choosers, openers, info inputs and similar.
import numpy as np

#CHOOSERS
def file_chooser():
	print("Insert filename")
	name= "E:/fourth year/first semester/biological database/ptoject/matrices/pam250.txt"
	if(name.find('.txt') == -1):
		print("Not a valid option. Try again.")
		return file_chooser()
	else:
		return name

def match_mis_gap_chooser(opt):
	print("Do you want to manually choose values for match, mismatch and gap?")
	m = "no"
	if m not in {"yes","y","no","n"}:
		print("Invalid answer.Try again.")
		return match_mis_gap_chooser(opt)
	if m in {"yes","y"}:
		print("Match:")
		match = input_check()
		print("Mismatch:")
		mismatch = input_check()
		print("Gap:")
		gap = input_check()
		ind = 1
		return match, mismatch, gap, ind
	elif opt == "g":
		match = 5
		mismatch = -1
		gap = -2
		ind = 0
	elif opt == "l":
		match = 1
		mismatch = -1
		gap = -1
		ind = 0
	return match, mismatch, gap, ind

#INPUT CHECKS
def input_check():
	val = input()
	v = val
	if v.lstrip('-').isdigit():
		return int(val)
	else:
		print("Not a number. Try again.")
		return input_check()

def sequence_input_check(allowed,seq):
	print("Enter 1 for a file name or 2 for DNA/protein sequence:")
	a = "2"
	if a not in {"1","2"}:
		print("Not a valid option.Try again.")
		return sequence_input_check(allowed)
	elif a == "1":
		print("Enter file name:")
		filename = input()
		if(filename.find('.txt') == -1):
			print("Not a valid option. Try again.")
			return sequence_input_check(allowed)
		else:
			sequence = file_opener(filename)
			sequence = sequence.upper()
			print(sequence)
			for i in range(len(sequence)):
				if sequence[i] not in allowed:
					print("Invalid sequence.Try again.")
					return sequence_input_check(allowed)
			return sequence
	else:
		print("Insert sequences for alignment made of:" + str(allowed))
		sequence = seq
		sequence = seq.upper()
		print(sequence)
		for i in range(len(sequence)):
			if sequence[i] not in allowed:
				raise Exception("Invalid sequence.")
		return sequence

#FILE OPENERS - WRITERS
def file_opener(filename):
	try:
		dna = open(filename, 'r')
		content = dna.read()
		content = content.replace('\n','')
		return content
	except FileNotFoundError:
		print("The file does not exist.")
		exit()

def rna_file_writer(content):
	print("Do you want to have RNA info written in a file?")
	answer = "no"
	if answer not in ["Yes","y", "yes", "No", "n", "no"]:
		print("Not a valid answer. Try again.")
		return rna_file_writer(content)
	elif answer in ["Yes","y", "yes"]:
		print("Insert file name:")
		filename = input()
		filename = filename + ".txt"
		print(filename)
		rna = open(filename, 'w')
		rna.write(content)
		print("Writing in " + filename + "successfully finished.")
		return
	else:
		return
