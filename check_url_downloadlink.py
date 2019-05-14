

import psycopg2

conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor=conn.cursor()

sql_command2='''select tweet_id,url from elec_prgd_tweet_bigurl;'''

cursor.execute(sql_command2)

conn.commit()

data2=cursor.fetchall()
conn.close()

extnsn=('.pdf','.mp3','.jepg',\
        'exe','doc','.js','.jar','.sfx','.bat','.jpg','.tmp','.py','docx')
url_append=[]
count=0
for uu1 in data2:
    uu=uu1[1]
    if uu.endswith(extnsn):
       count=count+1
       url_append.append(uu1)
 

import psycopg2

conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor=conn.cursor()

sql_command2='''select tweet_id,user_id from prgd_elec_tweet_text;'''

cursor.execute(sql_command2)

conn.commit()

data3=cursor.fetchall()
conn.close()     

tid_uid=dict(data3)