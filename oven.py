#!/usr/bin/env python3
#####################################LICENCE#############################################
#Copyright (c) 2015 Faissal Bensefia							#
#											#
#Permission is hereby granted, free of charge, to any person obtaining a copy		#
#of this software and associated documentation files (the "Software"), to deal		#
#in the Software without restriction, including without limitation the rights		#
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell		#
#copies of the Software, and to permit persons to whom the Software is			#
#furnished to do so, subject to the following conditions:				#
#											#
#The above copyright notice and this permission notice shall be included in		#
#all copies or substantial portions of the Software.					#
#											#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR		#
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,		#
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE		#
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER			#
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,		#
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN		#
#THE SOFTWARE.										#
#########################################################################################


#####Import######
import os	
import subprocess
from datetime import datetime
#################

###Variable Declarations###
inputFolderContents	=[]
cmdToExec		=["cat ","'{fullPath}'"]
###########################

#Initialisation
if not os.path.exists("./input/"):
	os.makedirs("./input/")

if not os.path.exists("./output/"):
	os.makedirs("./output/")

#Main loop
while True:
	#Go through the input directory and save it in inputFolderContents
	inputFolderContents	=os.listdir("./input/")#list(os.walk("./input/"))[1:]#We're removing the first 2 items because they'll just be '.' and './input', neither of those are useful
	#print(inputFolderContents)
	if len(inputFolderContents)>0: #If there are any files than start processing them
		print("["+str(datetime.now())+"]Jobs found")
		for i in inputFolderContents: #Go through every file in the folder
			print("["+str(datetime.now())+"]Processing "+i)
			subprocess.call(cmdToExec[0]+cmdToExec[1].format(**{"filename":i,"fullPath":"./input/"+i}),shell=False) #Replace certain placeholders for things like the input filename
			os.remove("./input/"+i)
	#else:
		#print("["+str(datetime.now())+"]No jobs found")#Uncomment this if you want, I just commented it because I found it annoying, but you might find it useful, especially if you want to know that it's not frozen
