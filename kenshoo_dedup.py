##################################################################################
# NOTE: need to sort input file by ID and timestamp before running this code!!!
# The purpose of this script is to de-dup kenshoo activity file.
#Output: text file
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 11/09/15
# 
##################################################################################
import time as t

##################################################################################
##PARAMETERS##
start_date = 20150401  #this should be the analysis period begin date
end_date = 20150630 #this should be the analysis period end date

#set to True if printing progress to screen is desired
verbose = True

#base output directory
output_directory = "E:\\users\\xchai\\"
###################################################################################
start = t.time()

############################################################################################################################
#'''
#load tmp_final_model_dataset file
fn_in = "E:\\users\\xchai\\june_kenshoo_withdups.txt"
fn_out = output_directory + "June_kenshoo_ND_" + str(start_date) + "_" + str(end_date) + ".txt"
fn_out2 = output_directory + "June_kenshoo_dups_" + str(start_date) + "_" + str(end_date) + ".txt"

counter = 0
past_SID_timestamp = None
fh_out = open(fn_out,'w')
fh_out2 = open(fn_out2, 'w')

with open(fn_in,'r') as fh_in:
	for line in fh_in.readlines():
		v = line.strip().split('|')
		SID = v[0]
		timestamp = v[1]
		conv_type = v[2]
		lines = v[3]
		YYYYMMDD = int(timestamp[:8])
		
		SID_timestamp = SID + "|" + timestamp
		
		if SID_timestamp != past_SID_timestamp and YYYYMMDD >= start_date and YYYYMMDD <= end_date:
			print >> fh_out, '%s' %("|".join(v))
		else:
			print >>fh_out2, '%s' %("|".join(v))
			
		past_SID_timestamp = SID_timestamp
		counter += 1
		
		if (counter % 1000000 == 0):
			print '%d events processed from kenshoo activity file' % (counter)
		
		
fh_out.close()
fh_out2.close()


#end of script actions
end = t.time()
elapsed = end - start

#if verbose == True:
print "done dedupping kenshoo activity file"
print "Run time: ", elapsed, " seconds\n"

print 'done'



#execfile("E:/Users/xchai/kenshoo_dedup.py")




