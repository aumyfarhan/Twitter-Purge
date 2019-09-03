# -*- coding: utf-8 -*-
"""

Plots the language histogram
Created on Mon Sep  2 22:24:09 2019

@author: Mueen
"""

import pandas as pd
import seaborn as sbn
import math
import matplotlib.pyplot as plt

chunk_size=1000
chunks2=[]

for chunk2 in pd.read_csv('data.csv',chunksize=chunk_size,usecols=['id','lang']):    
    chunks2.append(chunk2)


df2=pd.concat(chunks2,axis=0)

del chunk2
del chunks2

df2=df2.dropna(how='any')

total_count2=df2["lang"].count()
lang_hist2=df2.groupby(df2["lang"])["lang"].count()/total_count2

#lang_hist2=lang_hist.apply(lambda x: math.log2(x))
lang_hist22=lang_hist2.sort_values(ascending=False)

fig2 = plt.figure()
ax2 = plt.gca()
ax2=lang_hist22[:10].plot(kind='bar')

ax2.set_ylabel('user count')
ax2.set_xlabel('language')

lang_code_dict={"en":"English",\
                "es":"Spanish",\
                "pt":"Portuguese",\
                "ru":"Russian",\
                "tr":"Turkish",\
                "ar":"Arabic",\
                "fr":"French",\
                "ja":"Japanese",\
                "id":"Indonesian",\
                "en-gb":"English (UK)"}


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

#plt.savefig('control_lang_count.pdf', bbox_inches="tight")