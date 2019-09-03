# -*- coding: utf-8 -*-
"""

Plots the language histogram
Created on Mon Sep  2 22:24:09 2019

@author: Mueen
"""

from collections import Counter
import pandas as pd
import seaborn as sbn
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# given a numeric account property data series,
# return a logarithmic CDF

def get_CDF(df):
    
    MIN = 1
    MAX = df.max(axis=0)
    
    zero_bin = [0,0.9]
    zero_hist = np.histogram(df, bins=zero_bin)
    
    bins_log = np.logspace(np.log10(MIN), np.log10(MAX), 10*np.log10(MAX))
    bins_log = np.unique(np.array([int(i) for j,i in enumerate(bins_log)]))
    
    hist = np.histogram(df, bins=bins_log)
     
    total_sum = sum(hist[0]) + zero_hist[0]
    x_count = bins_log[:-1]
    y_cdf = (np.cumsum(hist[0]) + zero_hist[0])/total_sum
    
    
    '''CDF = [] 
    for i, j in enumerate(x_count):
        y = y_cdf[i]
        CDF.append([j,y])'''
        
    return x_count, y_cdf


# takes input of a pandas data series of language name
# returns "top_no" no of language count percentage
def get_top_language(df, top_no):
    
    # using data series to list conversion
    # then using counter
    '''language_list = df.tolist()
    total_user = len(language_list)
    counter = Counter(language_list).most_common(top_no)
    top_language = [(x[0],x[1]*100/total_user) for x in counter]'''
    
    
    # using pandas built-in groupby method
    language_count = df.groupby(df).count()*100/df.size
    language_count.sort_values(ascending=False)
        
    return language_count[:top_no].to_dict()




# account creation year plotting

def get_account_creation_year_count(df):    
    
    df = df.astype("datetime64")

    no_of_users_per_year = df.groupby(df.dt.year).count()*100/df.size
    
    return no_of_users_per_year.to_dict()


def get_top_hashtag(df, top_no):
    

    hashtag_list_temp = df.tolist()
    
    hashtag_list = [hashtag for inner_list in hashtag_list_temp for\
               hashtag in inner_list[0][1:-1].split(',') if hashtag!='']
    
    hashtag_count = Counter(hashtag_list).most_common(top_no)
    
    return hashtag_count



x, y = get_CDF(df)

'''
def top_hashtags(df, topn, troll_origin):
    all_tweets = df.shape[0]
    hashtags_list = df['hashtags'].tolist()
    hashtags_flat = [item for sublist in hashtags_list for item in sublist]
    counter = Counter(hashtags_flat).most_common(topn)
    res = []
    column_name = 'Hashtag (' + troll_origin + ')' 
    for c in counter:
        
        res.append({column_name: c[0], 'Percentage (%)': c[1]/len(hashtags_flat)*100})
    return res

top_hashtags_russians = pd.DataFrame(find_top_hashtags(russians_df_all[russians_df_all.hashtags!=False], 
                                                       20, 'Russians'))
top_hashtags_iranians = pd.DataFrame(find_top_hashtags(iranians_df_all[iranians_df_all.hashtags!=False], 
                                                       20, 'Iranians'))
table_3 = pd.concat([top_hashtags_russians, top_hashtags_iranians], axis=1)
table_3

#plt.savefig('control_lang_count.pdf', bbox_inches="tight")'''