import psycopg2


conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()
conn.autocommit=True

create_sentiment_table="create table elec_prgd_tweet_sentiment\
                                         (tweet_id BIGINT PRIMARY KEY,\
                                          sentiment_label TEXT);"

cur.execute(create_sentiment_table)

#cur.execute(create_table3)

conn.autocommit=False
conn.close()
