# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:09:08 2019

@author: Mueen
"""

import pandas as pd
import numpy as np
import csv
import psycopg2
import os
from collections import Counter


# input data to database 

# get data from database

# write data from pandas dataframe to CSV file


'''
file_name = 'FUNCTION Argument'
columns_name = ["id","friends_count","followers_count","favourites_count","statuses_count"]
separator = '\t'
'''

# read data from CSV file
def read_csv (file_name, separator='\t', columns_name=None):
    
    megabyte_div = 1048576
    file_size = os.path.getsize(file_name)/megabyte_div
    
    # maximum file size in MB to read in one iteration
    file_size_limit = 100
    
    if file_size > file_size_limit:
        
        # no of row to read in one iteration
        chunk_size = 10000 
        temporary_data_list = []
        
        # if columns_name is provided, use them. Otherwise read all columns
        if columns_name:
            for chunk in pd.read_csv(file_name, chunksize=chunk_size,\
                                     sep=separator, usecols=columns_name):
                temporary_data_list.append(chunk)
        else:
            for chunk in pd.read_csv(file_name, chunksize=chunk_size,\
                                     sep=separator):
                temporary_data_list.append(chunk)
            
        data_frame = pd.concat(temporary_data_list, axis=0)
        del temporary_data_list, chunk
            
    else:
        if columns_name:
            data_frame = pd.read_csv(file_name, sep=separator, usecols=columns_name)
        else:
            data_frame = pd.read_csv(file_name, sep=separator)
            
    return data_frame

# function to create table
def create_table(sql_statement, database_name='tweet_text', \
                  hostname='localhost', username='postgres',\
                  password='tmobile91'):
    
    conn = psycopg2.connect\
    (host=hostname, dbname=database_name,\
     user=username, password=password)

    cur=conn.cursor()
    conn.autocommit=True
    
    cur.execute(sql_statement)
    conn.autocommit=False
    conn.close()

sql_query='''select * from all_prgd_users;'''

def get_data_from_database(sql_query, database_name='tweet_text', \
                  hostname='localhost', username='postgres',\
                  password='tmobile91'):
    
    conn = psycopg2.connect\
    (host=hostname, dbname=database_name,\
     user=username, password=password)
    
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    conn.commit()
    data = cursor.fetchall()
    conn.close()
    
    return data  


# perform hashtag count for a given database query statement
sql_query='''select hashtags from day_one_second_text;'''

def get_hashtag_count_from_database(sql_query, database_name = 'tweet_text', \
                  hostname='localhost', username='postgres',\
                  password='tmobile91', array_size=100000):
    
    conn = psycopg2.connect\
    (host=hostname, dbname=database_name,\
     user=username, password=password)
    
    cursor = conn.cursor()
    cursor.execute(sql_query)
    
    data = cursor.fetchmany(array_size)
    
    hashtag_count = Counter([])
    
    while data:
        
        temporary_hashtag_list = [x for w in data for\
                   x in w[0][1:-1].split(',') if x!='']
        
        temporary_hashtag_count = Counter(temporary_hashtag_list)
        hashtag_count = hashtag_count + temporary_hashtag_count
        
        data = cursor.fetchmany(array_size)    
    
    conn.close()
    
    return hashtag_count

 
'''
file_name = 'two_million_random_sample_full_data.csv'
random_data = read_csv(file_name)

def write_csv():
    
'''




