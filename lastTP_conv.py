##################################################################################
# lastTP_conv.py
# The purpose of this script is to calculate the time difference between last touchpoint and conversion
#Input: event_file_conv_only_ND_EP_:  sid|timestamp|conv_flag|event_type|publisher|tactic|campaign_type
#Output: time_lastTP_conv_.txt file, this file is sored by id, timestamp
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com> 
#Date: 2015/08/26
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
fh_out = output_directory + "time_lastTP_conv_" + str(start_date) + "_" + str(end_date) + ".txt"

fh1 = open(fh_in,'r')
fh2 = open(fh_out,'w')


dat = pd.read_table(fh1, delimiter='|',names=['user_ID','timestamp','converter_flag','event_type','publisher','tactic','campaign_type'], engine='python')

##convert 'timestamp' from int to str. Use apply() instead of astype() because 'timestamp' is Series
dat['timestamp'] = dat['timestamp'].apply(str)
dat['timestamp'] = pd.to_datetime(dat['timestamp'], format='%Y%m%d%H%M%S')
newdat = dat.groupby('user_ID').tail(2).reset_index(drop=True)

newdat['delta_time'] = newdat.groupby('user_ID')['timestamp'].diff()
newdat['delta_time_sec']=newdat['delta_time'] / np.timedelta64(1, 's')

newdat.to_csv(fh2, sep='|',index=False, header=['user_ID','timestamp','converter_flag','event_type','publisher','tactic','campaign_type','delta_time','delta_time_sec'])

fh1.close()
fh2.close()


#end of script actions
end = t.time()
elapsed = end - start

#if verbose == True:
print "Run time: ", elapsed, " seconds\n"
print 'done'

#execfile('E:/users/xchai/lastTP_conv.py');
