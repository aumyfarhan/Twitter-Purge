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



user_1=[x[0] for x in data5]
user_2=[x[1] for x in data5]

all_user=user_1+user_2
all_user_mod=list(set(all_user))


conn5 = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor5=conn5.cursor()


cursor5.execute("select user_id,pol_count from user_political_bias_final")

conn5.commit()

data6=cursor5.fetchall()

conn5.close()
cursor5.close()

id_label_dict=dict(data6)

TTtable=[]

pd=str('id')
cc=str('label')

con_user_count=0

lib_user_count=0

TTtable.append([pd,cc])

for cur_user in all_user_mod:
    
    cur_label_tmp=id_label_dict.get(cur_user,0)
    if (cur_label_tmp>0):
        cur_label=1
        con_user_count=con_user_count+1
    elif cur_label_tmp<0:
        lib_user_count=lib_user_count+1
        cur_label=-1
    else:
        cur_label=0

    TTtable.append([cur_user,cur_label])
    
output_file="elec_user_id_poli_label.csv"
with open(output_file, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in TTtable:
        writer.writerow(val) 