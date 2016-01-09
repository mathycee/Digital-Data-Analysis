##################################################################################
# The purpose of this script is match timestamp to get ID
#Output: order_id.txt file
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 01/07/16
# 
##################################################################################
import time as t
import pandas as pd


##################################################################################
##PARAMETERS##
start_date = 20151101  #this should be the analysis period begin date
end_date = 20151130 #this should be the analysis period end date

#set to True if printing progress to screen is desired
verbose = True

#base output directory
output_directory = "E:\\users\\xchai\\LS\\"
###################################################################################
start = t.time()

############################################################################################################################

counter = 0 

fn_in1 = "E:\\users\\xchai\\LS\\activity_event_lookup_" + str(start_date) + "_" + str(end_date) + ".txt"
fn_in2 = output_directory + "SMB_lines_"+ str(start_date) + "_" + str(end_date) + ".txt"
fn_out1 = output_directory + "conv_lines_order_id_"+ str(start_date) + "_" + str(end_date) + ".txt"
fn_out2 = output_directory + "order_id_" + str(start_date) + "_" + str(end_date) + ".txt"

fh_out1 = open(fn_out1,'w')
with open(fn_in1,'r') as fh_in1:
	for line in fh_in1.readlines():
		v = line.strip().split('|')
		DFA_ID = v[0]
		timestamp = v[1]
		other_data=v[4]

		order_id = 0
		if 'u5=' in other_data:
			order_id = other_data.split('u5=')[1].split(';')[0]
		
		lines = 0
		if 'u4=' in other_data:
			lines = other_data.split('u4=')[1].split(';')[0]
		
		event = DFA_ID + '|' + timestamp + '|' + str(order_id) + '|' + str(lines)  
		
		print >> fh_out1, '%s' %(event)
		
		counter += 1
			
		if (counter % 1000000 == 0):
			print '%d events processed from kenshoo activity file' % (counter)
		
		
fh_out1.close()

fh_in2 = open(fn_in2,'r')
fh_in3 = open(fn_out1,'r')

fh_out2 = open(fn_out2,'w')

dat1 = pd.read_table(fh_in2, delimiter = '|', names=['SID', 'timestamp','lines'], engine ='python')
dat2 = pd.read_table(fh_in3, delimiter = '|', names =['DFA_ID','timestamp','id','lines'], engine ='python')

match_result = pd.merge(dat1,dat2, how='inner', on = ['timestamp'])

match_result.to_csv(fh_out2, sep='|', index=False)


fh_in2.close()
fh_in3.close()
fh_out2.close()

#end of script actions
end = t.time()
elapsed = end - start

#if verbose == True:
print "done matching id "
print "Run time: ", elapsed, " seconds\n"

print 'done'




