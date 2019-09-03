
def create_table(statement, database_name = 'tweet_text', \
                  hostname = 'localhost', username = 'postgres',\
                  password = 'tmobile91'):
    
    conn = psycopg2.connect\
    (host = hostname, dbname = database_name,\
     user = username, password = password)

    cur=conn.cursor()
    conn.autocommit=True
    
    cur.execute(statement)
    conn.autocommit=False
    conn.close()


'''
create_table1="create table tweet_text(tweet_id BIGINT PRIMARY KEY,\
                                        tweet_text TEXT,\
                                        user_id BIGINT NOT NULL,\
                                        lang TEXT,\
                                        post_time TIMESTAMP NOT NULL)"

#cur.execute("set autocommit on;")

#cur.execute("set transaction read write")
#create_table_space="CREATE TABLESPACE tweet_text LOCATION 'G:/tweet_data_collection';"
#create_database="CREATE DATABASE tweet_text TABLESPACE tweet_text"
#cur.execute(create_table_space)'''




