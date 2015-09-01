##################################################################################
# Touch Point Distribution
# The purpose of this script is to create touchpoint distribution.
#Output: touchpoint_distribution.txt file
#Author: Xiaomeng Chai <chaixiaomeng@gmail.com>
#Date: 08/18/15, 08/24/15
# 
##################################################################################
import time as t

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
fh_in = "E:\\xhcai\\output\\tmp_final_model_dataset_100_95_" + str(start_date) + "_" + str(end_date) + ".txt"

# create an output file that is used later as input

fh_out = output_directory + "SID_plength_convflag_" + str(start_date) + "_" + str(end_date) + ".txt"
counter = 0
fh_out = open(fh_out,'w')
with open(fh_in,'r') as fh:
	for line in fh.readlines()[1:]:
		v = line.strip().split('|')
		SID = v[0]
		converter_flag = v[2]
		if converter_flag == '1':
			converter_flag =1
		else:
			converter_flag = 0
		path_length = int(float(v[12]))+int(float(v[13]))+int(float(v[14]))+int(float(v[15]))+int(float(v[16]))+int(float(v[17]))+int(float(v[18]))+int(float(v[19]))+int(float(v[20]))+int(float(v[21]))
		
		print  >> fh_out, '%s|%s|%s' % (SID,path_length, converter_flag)
		
		counter += 1
				
		if (counter % 10000000 == 0):
			print '%d events processed from tmp_final_dataset file' % (counter)

print  'finish pulling path length for each SID '
fh_out.close()

#08/18/2015  Publisher Distribution
cnt_0 = 0
cnt_1 = 0
cnt_2_10 = 0
cnt_11_50 = 0
cnt_51_100 = 0
cnt_101plus = 0

conv_0 = 0
conv_1 = 0
conv_2_10 = 0
conv_11_50 = 0
conv_51_100 = 0
conv_101plus = 0

fn_in = output_directory + "SID_plength_convflag_" + str(start_date) + "_" + str(end_date) + ".txt"
#fn_in = output_directory + "SID_test.txt"
fn_out = output_directory + "touchpoint_distribution_"+ str(start_date) + "_" + str(end_date) + ".txt"


fn = open (fn_in, 'r')
fh_out = open(fn_out,'w')

for line in fn.readlines():
	try:
		v = line.strip().split('|')
		SID = v[0]
		path_length = int(float(v[1]))
		conv_flag = int(float(v[2]))
	except:
	 print '%s' %(v)


	if path_length == 0:
		cnt_0 += 1
		conv_0 += conv_flag
	elif path_length == 1:
		cnt_1 += 1
		conv_1 += conv_flag
	elif (path_length >=2 and path_length <= 10):
		cnt_2_10 += 1
		conv_2_10 += conv_flag
	elif (path_length >= 11 and path_length <= 50):
		cnt_11_50 += 1
		conv_11_50 += conv_flag
	elif (path_length >= 51 and path_length <= 100):
		cnt_51_100 += 1
		conv_51_100 += conv_flag
	else:
		cnt_101plus += 1
		conv_101plus += conv_flag

print >> fh_out, 'cnt_0|cnt_1|cnt_2_10|cnt_11_50|cnt_51_100|cnt_101plus|conv_0|conv_1|conv_2_10|conv_11_50|conv_51_100|conv_101plus'
print  >> fh_out, '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s' % (str(cnt_0),str(cnt_1), str(cnt_2_10),str(cnt_11_50),str(cnt_51_100),str(cnt_101plus),str(conv_0),str(conv_1), str(conv_2_10),str(conv_11_50),str(conv_51_100),str(conv_101plus))

fh_out.close()
fn.close()

#end of script actions
end = t.time()
elapsed = end - start

#if verbose == True:
print "done creating touchpoint distribution"
print "Run time: ", elapsed, " seconds\n"

print 'done'


#execfile("E:/Users/xchai/touchpoint_distribution.py")




