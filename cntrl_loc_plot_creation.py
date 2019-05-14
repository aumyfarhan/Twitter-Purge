conn3 = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor3=conn3.cursor()

sql_command3="""SELECT distinct location,count(location) 
   FROM all_control_users
   WHERE location ~'.*[a-zA-Z].*'
   GROUP BY location
   HAVING COUNT(location) > 5;"""

cursor3.execute(sql_command3)

conn3.commit()

CNTRL_all_data_count=cursor3.fetchall()

cursor3.close()
conn3.close()


CNTRL_colors = ["rgb(255,0,117)"]

scale = 25
CNTRL_all_lat=[]
CNTRL_all_lon=[]
CNTRL_all_loc_count=[]
CNTRL_all_loc_name=[]

for CNTRL_cur_data in CNTRL_all_data_count:

    CNTRL_cur_location_name=CNTRL_cur_data[0]
    CNTRL_cur_location_count=CNTRL_cur_data[1]
    
    if CNTRL_cur_location_name in all_loc_dict.keys():
        CNTRL_cur_location_value=list(map(float, all_loc_dict[CNTRL_cur_location_name].split(',')))
        CNTRL_all_loc_count.append(CNTRL_cur_location_count)
        CNTRL_all_loc_name.append(CNTRL_cur_location_name)
        
        
        CNTRL_all_lon.append(round(CNTRL_cur_location_value[1],4))
        CNTRL_all_lat.append(round(CNTRL_cur_location_value[0],4))
        
        
CNTRL_city = [go.Scattergeo(
    #locationmode = 'country names',
    lon = CNTRL_all_lon,
    lat = CNTRL_all_lat,
  
    #text = df_sub['text'],
    
    marker = go.scattergeo.Marker(
        
        size = [x/scale for x in CNTRL_all_loc_count],
        color = CNTRL_colors[0],
        
        line = go.scattergeo.marker.Line(
            width=0.5, color='rgb(40,40,40)'
        ),
        sizemode = 'area',
        opacity=0.5
    ) )]