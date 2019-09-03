'''
This code 

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


sql_query='''select * from all_prgd_users;'''

data, column_names = get_data_from_database(sql_query)

data_frame = pd.DataFrame(data, columns=column_names)

output_filename = 'random_5000_purged_users.csv'

data_frame.sample(n=5000).to_csv(output_filename, index=False,\
                  sep=',', encoding='utf-8')


SELECT * FROM my_table TABLESAMPLE SYSTEM(0.001) LIMIT 1;