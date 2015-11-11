##################################################################################
# 
# The purpose of this script is to de-dup DFA activity file.
#Output: text files
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 11/08/15
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
output_directory = "E:\\users\\xchai\\Lines_sold\\"
###################################################################################
start = t.time()

############################################################################################################################
#'''
#load tmp_final_model_dataset file
fn_in = "E:\\users\\xchai\\Lines_sold\\activity_event_lookup_" + str(start_date) + "_" + str(end_date) + ".txt"
fn_out = output_directory + "June_DFA_Linesold_ND_" + str(start_date) + "_" + str(end_date) + ".txt"
fn_out2 = output_directory + "June_DFA_Linesold_dups_" + str(start_date) + "_" + str(end_date) + ".txt"

counter = 0
past_SID = None
past_timestamp = None
fh_out = open(fn_out,'w')
fh_out2 = open(fn_out2, 'w')

with open(fn_in,'r') as fh_in:
	for line in fh_in.readlines():
		v = line.strip().split('|')
		SID = v[0]
		timestamp = v[1]
		conv_type = v[2]
		other_data = v[3]
		
		if 'u4=' in other_data:
			linesold_index = other_data.index('u4')
			if other_data[linesold_index+4].isdigit():
				lines = other_data[linesold_index+3:linesold_index+5]
			else:
				lines = other_data[linesold_index+3]
		else:
			lines = 0
			
		event = SID + "|" + timestamp + "|" + conv_type + "|" + str(lines)
		
		if (SID != past_SID and timestamp != past_timestamp):			
			print >> fh_out, '%s' %(event)
		else:
			print >>fh_out2, '%s' %(event)
			
		past_SID = SID
		past_timestamp = timestamp
		counter += 1
		
		if (counter % 1000000 == 0):
			print '%d events processed from DFA activity file' % (counter)
		
		
fh_out.close()
fh_out2.close()


#end of script actions
end = t.time()
elapsed = end - start

#if verbose == True:
print "done dedupping DFA activity file"
print "Run time: ", elapsed, " seconds\n"

print 'done'



#execfile("E:/Users/xchai/Lines_sold/dfa_linesold_ND.py")




