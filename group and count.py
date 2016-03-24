
##################################################################################
# Fractional_Credit_by_Publisher.py
# The purpose of this script is to count monthly impressions by event type
#Author: Xiaomeng Chai 
#Date: 03/21/2016
#
##################################################################################

METHOD = 1


#############
#METHOD 1--Pandas (this method ignore blank event_type)
#############

if METHOD == 1:
	import time as t
	import pandas as pd

	#set to True if printing progress to screen is desired
	verbose = True

	start = t.time()

	#fn_in = "E:\\attribution\\alt\\graph2_2015\\output\\x1.event_file_sorted_20140101_20151231.txt"
	fn_in2 = "E:\\users\\xchai\\alt\\monthly_imp_subset.txt"
	fn_out = "E:\\users\\xchai\\alt\\monthly_imp_cnt.txt"

	fh_in2 = open(fn_in2,'r')
	fh_out = open(fn_out,'w')
	dat = pd.read_table(fh_in2,delimiter = "|", names = ["yearmonth","event_type","pub","tac"])
	new = dat.groupby(["yearmonth","event_type"]).size()

	new.to_csv(fh_out, sep="|", index=True)

	fh_in2.close()
	fh_out.close()


	#end of script actions
	end = t.time()
	elapsed = end - start


	print "done counting monthly impressions"
	print "Run time: ", elapsed, " seconds\n"

###########################################################################################################

#############
#METHOD 2--defaultdict (this method keeps all event_type even if it's blank)
#read these useful links
#https://codefisher.org/catch/blog/2015/04/22/python-how-group-and-count-dictionaries/
#https://docs.python.org/3/library/collections.html#collections.defaultdict
#############
elif METHOD == 2:
	import time as t
	from collections import defaultdict


	#set to True if printing progress to screen is desired
	verbose = True

	start = t.time()

	d = defaultdict(int)


	#fn_in = "E:\\attribution\\alt\\graph2_2015\\output\\x1.event_file_sorted_20140101_20151231.txt"
	fn_in2 = "E:\\users\\xchai\\alt\\monthly_imp_subset.txt"
	fn_out = "E:\\users\\xchai\\alt\\monthly_imp_cnt2.txt"

	with open(fn_in2,'r') as file_in:
		for line in file_in.readlines():
			v = line.strip().rsplit("|",2)
			
			d[v[0]] += 1

	fh_out = open(fn_out,"w")		
	for key in sorted(d):
		print >> fh_out,'%s|%s' %(key,d[key])

	fh_out.close()
	d.clear()


	#end of script actions
	end = t.time()
	elapsed = end - start


	print "done counting monthly impressions"
	print "Run time: ", elapsed, " seconds\n"




