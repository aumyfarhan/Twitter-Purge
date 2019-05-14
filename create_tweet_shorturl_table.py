import psycopg2


conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()
conn.autocommit=True

create_shorturl_table="create table elec_prgd_tweet_shorturl\
                                         (id SERIAL PRIMARY KEY, tweet_id BIGINT,\
                                          shorturl TEXT,political_label int);"

cur.execute(create_shorturl_table)

#cur.execute(create_table3)

conn.autocommit=False
cur.close()
conn.close()
