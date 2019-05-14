import time
import geocoder
from concurrent.futures import ThreadPoolExecutor


"""
import psycopg2
conn2 = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor2=conn2.cursor()

sql_command2='''select id, location from all_prgd_users where location is not null;'''

cursor2.execute(sql_command2)

conn2.commit()

data2=cursor2.fetchall()

cursor2.close()
conn2.close()"""

ec=0
gc=0

out_file_name='all_location_latlngtemp_spcl.txt'
out_file=open(out_file_name,'w')

def download(cur_data, base):
    global gc
    global ec
    global op_main

    cur_user_id=cur_data[0]
    temp_location=cur_data[1]
    
    if temp_location:
        
        

        try:
            geo_val = geocoder.arcgis(temp_location)
            
            geo_latlng=geo_val.latlng
            
            if len(geo_latlng)>1:
                
                geo_latlng_str=','.join(map(str, geo_latlng))
                gc=gc+1
                
                if (gc % 1000)==0:
                    print(gc)
                    print('\n',geo_latlng)    
                
                line_write=''
                
                line_write=line_write+str(cur_user_id)+'\t'+geo_latlng_str
                line_write=line_write.replace('\n','')
                out_file.write(line_write)
                out_file.write('\n')
   
        except Exception as e: print(e)


begin_time = time.time()


new_data2=data2[:100]

    
with ThreadPoolExecutor(max_workers=8) as executor:
    begin_time = time.time()
    result=executor.map(download, new_data2, [begin_time for i in range(len(new_data2))])


end_time = time.time()

diff_time=end_time-begin_time

out_file.close()