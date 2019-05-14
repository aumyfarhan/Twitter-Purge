import csv

import psycopg2


conn5 = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor5=conn5.cursor()

sql_command5='''  select aa.user_id,aa.retweet_user_id from elec_prgd_matched_retweet_tmp as aa
 where aa.retweet_user_id in 
 (select distinct bb.id
  from all_prgd_users as bb)
 and aa.user_id!=aa.retweet_user_id;'''

cursor5.execute(sql_command5)

conn5.commit()

data5=cursor5.fetchall()

conn5.close()
cursor5.close()


output_file='ELEC_tweet_retweet_userid_COMMON_purged.csv'

TTtable=[]

pd=str('source')
cc=str('target')

TTtable.append([pd,cc])
for j in data5:
    
    Tcur_user_id=j[0]
    Tcur_retweet_user_id=j[1]
    TTtable.append([Tcur_user_id,Tcur_retweet_user_id])
        
        
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in TTtable:
        writer.writerow(val) 