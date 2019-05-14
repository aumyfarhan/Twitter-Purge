import time
import geocoder



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

gc=0

out_file_name='country_location_latlng_final_1.txt'
out_file=open(out_file_name,'w')

def download(temp_location):
    global cntry_loc_dict
    global gc

    if temp_location:
        
        try:
            geo_val = geocoder.arcgis(temp_location)
            
            geo_latlng=geo_val.latlng
            
            if len(geo_latlng)>1:
                
                geo_latlng_str=','.join(map(str, geo_latlng))
                gc=gc+1
                
                cntry_loc_dict[temp_location]=geo_latlng_str
                print(gc)
                
                line_write=''
                
                line_write=line_write+temp_location+'\t'+geo_latlng_str
                line_write=line_write.replace('\n','')
                out_file.write(line_write)
                out_file.write('\n')
   
        except Exception as e: print(e)


begin_time = time.time()

cntry_loc_dict={}

for ww in just_cntry:
    download(ww)
    
end_time = time.time()

diff_time=end_time-begin_time

out_file.close()

with open("cntry_loc_dict.pickle","wb") as pickle_out:
    pickle.dump(cntry_loc_dict, pickle_out)