##################################################################################
# ab_signup_conv.py
# The purpose of this script is to create daily conversion number
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 07/21/2015
#
##################################################################################


#import glob
import os
import sys
import re
import time as t

start = t.time()

#############################
verbose = True

out = open("E:/users/xchai/ab/"+ "ab number of conversion" + '.txt','w')
for filename in os.listdir("E:/users/xchai/ab/temp"):
	if filename.startswith('a_'):
		fh = open("E:/users/xchai/ab/temp/" + filename,'r')
		number_signup = 0
		number_booking = 0
		for line in fh:
			event = line.strip().split('|')		
			if event[3] == "conve0":
				number_signup += 1
			elif event[3] == "reser0":
				number_booking += 1
		out.write(filename + "|" + str(number_signup) + "|" + str(number_booking) + "\n")
out.close()
fh.close()
	
		
#end of script actions
end = t.time()
elapsed = end - start


print "done creating daily conversion number"
print "Run time: ", elapsed, " seconds\n"