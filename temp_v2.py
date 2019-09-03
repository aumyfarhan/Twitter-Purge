import psycopg2
from collections import Counter


def get_hashtag_count(sql_query, database_name = 'tweet_text', \
                  hostname = 'localhost', username = 'postgres',\
                  password = 'tmobile91', array_size = 100000):
    
    conn = psycopg2.connect\
    (host = hostname, dbname = database_name,\
     user = username, password = password)
    
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
    
    return hashtag_count.most_common(50)

sql_query='''select hashtags from prgd_elec_tweet_text;'''
hashtag_count = get_hashtag_count(sql_query)

"""op=[int(x) for w in data for x in w[0][1:-1].split(',') if x.isdigit()]

with open('most_mentioned.pickle', 'wb') as handle:
    pickle.dump(top_counter_val, handle)"""
    
    
