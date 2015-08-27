##################################################################################
# lastTP_conv.py
# The purpose of this script is to calculate the time duration between the last Impression/Click/Video Impression and conversion
#Input: event_file_conv_only_ND_EP_:  sid|timestamp|conv_flag|event_type|publisher|tactic|campaign_type
#Output1: IKV_and_Conv_.txt file, has records when event type is I/K/V/E/P
#Output2: Time_LastDS_and_Conv_.txt file, this file has time duration between last I/V/K and conversion
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com> 
#Date: 2015/08/27
#
##################################################################################

import time as t
import pandas as pd
import numpy as np

##################################################################################
##PARAMETERS##
start_date = 20150401  #this should be the analysis period begin date
end_date = 20150731 #this should be the analysis period end date

#set to True if printing progress to screen is desired
verbose = True

#base output directory
output_directory = "E:\\users\\xchai\\output\\"
###################################################################################
start = t.time()

############################################################################################################################

#load tmp_final_model_dataset file
fh_in = output_directory + "event_file_conv_only_ND_EP_100_95_" + str(start_date) + "_" + str(end_date) + ".txt"
fh_out1 = output_directory + "IKV_and_Conv" + str(start_date) + "_" + str(end_date) + ".txt"
fh_out2 = output_directory + "Time_LastDS_and_Conv" + str(start_date) + "_" + str(end_date) + ".txt"

fh1 = open(fh_in,'r')
fh2 = open(fh_out,'w')

##need to check how many col the event_file_conv_only_ND_EP_ file has 
sid_disp = set()
for line in fh1.readlines():
		v = line.strip().split('|')
		sid = v[0]
		timestamp = v[1]
		conv_flag = v[2]
		event_type = v[3]
		publisher = v[4]
		tactic = v[5]
		campaign_type = v[6]
		
		if event_type == 'I' or event_type == 'K' or event_type == 'V':
			sid_disp.add(sid)
		
		if sid in sid_disp and (event_type == 'I' or event_type == 'K' or event_type == 'V' or event_type == 'P' or event_type == 'E'):
			event = sid +'|'+ timestamp +'|'+conv_flag +'|'+event_type +'|'+publisher +'|'+tactic +'|'+campaign_type
		
			print  >> fh2, '%s' % (event)
			
			
fh1.close()
fh2.close()
sid_disp.clear()

fh3 = open(fh_out1,'r')
fh4 = open(fh_out2,'w')
dat = pd.read_table(fh3, delimiter='|',names=['user_ID','timestamp','converter_flag','event_type','publisher','tactic','campaign_type'], engine='python')

##convert 'timestamp' from int to str. Used apply instead of astype because 'timestamp' is Series
dat['timestamp'] = dat['timestamp'].apply(str)
dat['timestamp'] = pd.to_datetime(dat['timestamp'], format='%Y%m%d%H%M%S')
new = dat.groupby('user_ID').tail(2).reset_index(drop=True)

new['delta_time'] = new.groupby('user_ID')['timestamp'].diff()
new['delta_time_sec']=new['delta_time'] / np.timedelta64(1, 's')

new.to_csv(fh4, sep='|',index=False, header=['user_ID','timestamp','converter_flag','event_type','publisher','tactic','campaign_type','delta_time','delta_time_sec'])

fh3.close()
fh4.close()


#end of script actions
end = t.time()
elapsed = end - start

#if verbose == True:
print "Run time: ", elapsed, " seconds\n"
print 'done'

#execfile('E:/users/xchai/IKV_conv.py');
