
##################################################################################
# 14.0.Fractional_Credit_by_Publisher.py
# The purpose of this script is to create fractional credit by publisher
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 08/07/2015
#
##################################################################################

import sys
import os
import time as t

start_date = 20150201  #this should be the analysis period begin date
end_date = 20150715 #this should be the analysis period end date


#set to True if printing progress to screen is desired
verbose = True

start = t.time()
#base directory
output_directory = "E:\\users\\xchai\\ab_su\\"

#dictionary class where the value defaults to zero if a key is added and no value is assigned	
class D_simple (dict):
	def __init__(self, default=None):
		self.default = default
	def __getitem__(self,key):
		if not self.has_key(key):
			self[key] = 0.00
		return dict.__getitem__(self,key)

###########################################################################################################
fn_in = output_directory + "output\\event_file_conv_only_ND_EP_FC_" + str(start_date)+"_"+str(end_date)+".txt"
#fn_in = output_directory + "FC_signup.txt" ---test
fn_out = output_directory + "Publisher_FC_"+ str(start_date)+"_"+str(end_date)+".txt"


fh = open(fn_in,'r')
counter = 0
sum_fc = 0
credit = D_simple(dict)

for line in fh:
	v = line.strip().split('|')
	pub = v[4]
	fc = float(v[7])

	key = pub
	credit[key] += fc

	sum_fc += fc

	counter += 1
	if verbose == True:
		if (counter % 100000000 == 0):
			print '%d lines processed' % (counter)

fh.close()

fh_out = open(fn_out,'w')
print >> fh_out,'publisher|fractional_credit'
for key in sorted(credit):
	if credit[key] == 0:
		FC = 0
	print >> fh_out,'%s|%s' %(key,credit[key])
fh_out.close()
credit.clear()


#end of script actions
end = t.time()
elapsed = end - start


print "done creating fractional credit by publisher"
print "Run time: ", elapsed, " seconds\n"


