'''
This code resturns data from database

'''
import psycopg2
import pandas as pd

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
    column_names = []
    for column in cursor.description:
        column_names.append(column[0])
    conn.close()
    
    return data, column_names

def get_top_language(df, top_no):
    language_list = df.tolist()
    total_user = len(language_list)
    counter = Counter(language_list).most_common(top_no)
    top_language = [(x[0],x[1]*100/total_user) for x in counter]
    
    return top_language


sql_query='''select * from all_prgd_users;'''

data, column_names = get_data_from_database(sql_query)

data_frame = pd.DataFrame(data, columns=column_names)

