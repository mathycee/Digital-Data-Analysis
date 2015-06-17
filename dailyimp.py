import os
import pandas as pd
import numpy as np
from pandas import DataFrame, Series


###########################################
verbose = True

with open("E:/users/xchai/"+ "daily_imp_test" + '.txt','a') as out: 
	for filename in os.listdir("E:/users/xchai/darden/temp"):
		if filename.startswith("i_2014072"):
			fh = open("E:/users/xchai/darden/temp/" + filename,'r')	
			readfile = pd.read_table(fh, delimiter='|',names=['ID','timestamp','publisher','tactic','activity'], engine='python')
			df = DataFrame({'imp_count':readfile.groupby([ "publisher", "tactic"]).size()}).reset_index()
			df.insert(0,'date',filename[2:10])
			if verbose == 'True':
				print df[:5]
			df.to_csv(out, sep='|',index=False, header=False)

fh.close()
out.close()	


#cstrong/darden_test/temp/i_20141124.txt
#execfile('E:/users/xchai/dailyimp-pandas.py')

