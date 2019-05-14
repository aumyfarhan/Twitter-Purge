import psycopg2


conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()
conn.autocommit=True

create_retweet_table="create table before_prg_tweet_retweet\
                                         (id BIGSERIAL PRIMARY KEY,\
                                          tweet_id BIGINT,\
                                          user_id BIGINT,\
                                          tweet_lang TEXT,\
                                          tweet_text TEXT,\
                                          tweet_time TIMESTAMP,\
                                          hashtags TEXT,\
                                          user_mentions TEXT,\
                                          short_url TEXT,\
                                          big_url TEXT,\
                                          retweet_id BIGINT,\
                                          retweet_user_id BIGINT);"

cur.execute(create_retweet_table)

#cur.execute(create_table3)

conn.autocommit=False
conn.close()