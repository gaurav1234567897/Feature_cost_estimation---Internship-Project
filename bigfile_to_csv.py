#!/usr/bin/env python
# coding: utf-8

## Instructions:
## Note: The input file have to be compressed file as file_name.gz and output file name as file_name.csv

import subprocess
import os
import pandas as pd


# In[209]:


lines = 5000000 ## to split on basis of lines can be changed as required


# In[210]:


path = os.getcwd()


# In[211]:


file_in_path=input("Input the file path and file name (As format: /dir../input_file_name.gz)\n  : ")


# In[213]:


for _ in range(len(file_in_path)-1,0,-1):
    if file_in_path[_] == '/':
        file_in_location = file_in_path[:_+1]
        file_in_name = file_in_path[_+1:]
        break

# In[212]:


file_in_location,file_in_name

        
# In[214]:


file_out_path=input("Enter the output file path and name (As format: /dir../output_file_name.csv)\n  : ")


# In[215]:


for _ in range(len(file_out_path)-1,0,-1):
    if file_out_path[_] == '/':
        file_out_location = file_out_path[:_+1]
        file_out_name = file_out_path[_+1:]
        break


# In[216]:


file_out_location,file_out_name


# In[217]:


subprocess.run('mkdir '+file_out_name,shell=True,cwd=file_out_location)
file_out_location=file_out_location+file_out_name+'/'
subprocess.run('gunzip '+file_in_name,shell=True,capture_output=True,cwd=file_in_location)
print(subprocess.run('split -l '+str(lines)+' '+file_in_location+file_in_name[:-3]+' '+file_out_location,shell=True,capture_output=True,text=True).stdout)
splitted_list=subprocess.run('ls',capture_output=True,text=True,cwd=file_out_location).stdout.split()
print("The given file is splitted in the given subfiles and processing..: ",splitted_list)
for i in splitted_list:
    print(subprocess.run('./accesslog_to_csv.py -gal '+file_out_location+i+' -csv '+file_out_location+i+'.csv',shell=True,capture_output=True,text=True,cwd=path).stdout) ## for prod file just add -prod after .csv as shell input in this line
    print("Processed.. the splitted file: ",i)
    subprocess.run('rm -R '+i,shell=True,cwd=file_out_location)


# In[218]:


for i in splitted_list:
    subprocess.run('gunzip '+i+'.csv.gz',shell=True,capture_output=True,cwd=file_out_location)
print("Processing.. to make final output file : ",file_out_name)
dfs = []
for filename in splitted_list:
    dfs.append(pd.read_csv(file_out_location+filename+'.csv'))
    subprocess.run('rm -R '+filename+'.csv',shell=True,cwd=file_out_location)    ## If commented will not delete the splitted files in the output location

pd.concat(dfs, ignore_index=True).to_csv(file_out_location+file_out_name,index=False)
    
subprocess.run('gzip '+file_in_path[:-3],shell=True,capture_output=True)

print("\nFinished..")

