# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:01:10 2018

@author: Mueen
"""
import pandas as pd
import numpy as np
import csv

chunk_size=1000
chunks=[]
for chunk in pd.read_csv('two_million_random_sample_full_data.csv', chunksize=chunk_size,sep='\t',usecols=["id","friends_count","followers_count","favourites_count","statuses_count"]):
    chunks.append(chunk)



df=pd.concat(chunks,axis=0)
del chunks


def plot_cdf(list_counts, xlabel, path, leg=False, islogx=True, xlimit=False):
    
######
MIN=1
MAX=max(df["statuses_count"])

zero_bin=[0,0.9]
zero_hist = np.histogram(df["statuses_count"], bins=zero_bin)

bins_log=np.logspace(np.log10(MIN),np.log10(MAX),10*np.log10(MAX))
bins_log=np.unique(np.array([int(i) for j,i in enumerate(bins_log)]))

hist = np.histogram(df["statuses_count"], bins=bins_log)
 
total_sum=sum(hist[0])+zero_hist[0]
x_count=bins_log[:-1]
y_cdf=(np.cumsum(hist[0])+zero_hist[0])/total_sum


output_file='random_status_vs_user.csv'

table=[] 
for i,j in enumerate(x_count):
    y=y_cdf[i]
    table.append([j,y])


# creating a csv file of data sample id and their corresponding  class label 
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in table:
        writer.writerow(val)

######
MIN=1
MAX=max(df["friends_count"])

zero_bin=[0,0.9]
zero_hist = np.histogram(df["friends_count"], bins=zero_bin)

bins_log=np.logspace(np.log10(MIN),np.log10(MAX),10*np.log10(MAX))
bins_log=np.unique(np.array([int(i) for j,i in enumerate(bins_log)]))

hist = np.histogram(df["friends_count"], bins=bins_log)
 

total_sum=sum(hist[0])+zero_hist[0]
x_count=bins_log[:-1]
y_cdf=(np.cumsum(hist[0])+zero_hist[0])/total_sum


output_file='random_friends_vs_user.csv'

table=[] 
for i,j in enumerate(x_count):
    y=y_cdf[i]
    table.append([j,y])


# creating a csv file of data sample id and their corresponding  class label 
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in table:
        writer.writerow(val)

######
MIN=1
MAX=max(df["followers_count"])

zero_bin=[0,0.9]
zero_hist = np.histogram(df["followers_count"], bins=zero_bin)

bins_log=np.logspace(np.log10(MIN),np.log10(MAX),10*np.log10(MAX))
bins_log=np.unique(np.array([int(i) for j,i in enumerate(bins_log)]))

hist = np.histogram(df["followers_count"], bins=bins_log)
 
total_sum=sum(hist[0])+zero_hist[0]
x_count=bins_log[:-1]
y_cdf=(np.cumsum(hist[0])+zero_hist[0])/total_sum


output_file='random_followers_vs_user.csv'

table=[] 
for i,j in enumerate(x_count):
    y=y_cdf[i]
    table.append([j,y])


# creating a csv file of data sample id and their corresponding  class label 
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in table:
        writer.writerow(val)


######
MIN=1
MAX=max(df["favourites_count"])

zero_bin=[0,0.9]
zero_hist = np.histogram(df["favourites_count"], bins=zero_bin)

bins_log=np.logspace(np.log10(MIN),np.log10(MAX),10*np.log10(MAX))
bins_log=np.unique(np.array([int(i) for j,i in enumerate(bins_log)]))

hist = np.histogram(df["favourites_count"], bins=bins_log)
 

total_sum=sum(hist[0])+zero_hist[0]
x_count=bins_log[:-1]
y_cdf=(np.cumsum(hist[0])+zero_hist[0])/total_sum


output_file='random_favourites_vs_user.csv'

table=[] 
for i,j in enumerate(x_count):
    y=y_cdf[i]
    table.append([j,y])


# creating a csv file of data sample id and their corresponding  class label 
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in table:
        writer.writerow(val)

