#!/D:/Python27_64/python.exe

#################################################################################
#The purpose of this script is to process path_freq files for checking search  
#converting paths that have more than two genres.
#
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 10/15/2015, 10/21/15
# 
#
#################################################################################


import time as t
import re

##################################################################################
start = t.time()

fh_in = "E:\\users\\xchai\\UC\\search.txt" 
fh = open(fh_in,'r')

for line in fh.readlines():
	tokens = re.split(',|-', line)
	count = tokens[0]
	genre_count = 0
	touchpoints = []
		
		for token in tokens[1:]:
			try:
				if token == 'BRD':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'CON':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'RES':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'RTL':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'PRP':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'SMB':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'ACC':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'RLS':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'PRM':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'DVC':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'PLA':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'KCT':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'ICM':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'SCM':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'RMK':
					genre_count += 1
					touchpoints.append(token)
				elif token == 'ONL':
					genre_count += 1
					touchpoints.append(token)
			except:
				print tokens

		if genre_count > 1:
			print count +',' + ','.join(touchpoints)
			
#end of script actions
end = t.time()
elapsed = end - start


print "done process path_freq file"
print "Run time: ", elapsed, " seconds\n"
			
			
#execfile('E:/users/xchai/UC/search.py');
					
						
				
		