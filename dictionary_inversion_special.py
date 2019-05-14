import psycopg2
import plotly
import plotly.graph_objs as go
import plotly.io as pio
import pickle
# create_inverted_dictionary
invert_loc_dict={}

with open('all_loc_dict_final.pickle','rb') as handle:
    all_loc_dict2=pickle.load(handle)
    
for key,val in all_loc_dict2.items():
    invert_loc_dict.setdefault(val, []).append(key)

### get cntrl data
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

cntrl_all_data_count=cursor3.fetchall()

cursor3.close()
conn3.close()


# get prgd data

conn2 = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor2=conn2.cursor()

sql_command2="""SELECT distinct location,count(location) 
   FROM all_prgd_users
   WHERE location ~'.*[a-zA-Z].*'
   GROUP BY location
   HAVING COUNT(location) > 5;"""

cursor2.execute(sql_command2)

conn2.commit()

prgd_all_data_count=cursor2.fetchall()

cursor2.close()
conn2.close() 


# create dictionary for cntrl_users_location_count
    
cntrl_dict_loc_count=dict(cntrl_all_data_count)   

cntrl_lat_long_loc_count={}    

for key,val in invert_loc_dict.items():
    
    temp_count=0
    for x in val:
        temp_count=temp_count+cntrl_dict_loc_count.get(x,0)
        
    cntrl_lat_long_loc_count[key]=temp_count    

# create data for cntrl    
CNTRL_colors = ["rgb(255,0,117)"]

scale = 100
CNTRL_all_lat=[]
CNTRL_all_lon=[]
CNTRL_all_loc_count=[]

for key,val in cntrl_lat_long_loc_count.items():


    CNTRL_cur_location_value=list(map(float, key.split(',')))
    
    CNTRL_all_loc_count.append(val)
    
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
            width=0, color='rgb(255,255,255)'
        ),
        sizemode = 'area',
        opacity=0.5
    ) )]
# create dictionary for prgd_users_location_count
    
prgd_dict_loc_count=dict(prgd_all_data_count)   

prgd_lat_long_loc_count={}    

for key,val in invert_loc_dict.items():
    
    temp_count=0
    for x in val:
        temp_count=temp_count+prgd_dict_loc_count.get(x,0)
        
    prgd_lat_long_loc_count[key]=temp_count        
    
#create data fro prgd

PRGD_colors =["rgb(0,116,217)"]

scale = 100
PRGD_all_lat=[]
PRGD_all_lon=[]
PRGD_all_loc_count=[]

for key,val in prgd_lat_long_loc_count.items():


    PRGD_cur_location_value=list(map(float, key.split(',')))
    
    PRGD_all_loc_count.append(val)
    
    PRGD_all_lon.append(round(PRGD_cur_location_value[1],4))
    PRGD_all_lat.append(round(PRGD_cur_location_value[0],4))
        
        
PRGD_city = [go.Scattergeo(
    #locationmode = 'country names',
    lon = PRGD_all_lon,
    lat = PRGD_all_lat,
  
    #text = df_sub['text'],
    
    marker = go.scattergeo.Marker(
        
        size = [x/scale for x in PRGD_all_loc_count],
        color = PRGD_colors[0],
        
        line = go.scattergeo.marker.Line(
            width=0, color='rgb(255,255,255)'
        ),
        sizemode = 'area',
        opacity=0.5
    ) )]    

layout = go.Layout(
        showlegend = True,
        geo = go.layout.Geo(
            #scope = 'world',
            showframe = False,
            showcoastlines = False,
            showcountries = True,
            projection = go.layout.geo.Projection(
                type='equirectangular'
            ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        )
    )
            
            
fig = go.Figure(data=PRGD_city+CNTRL_city, layout=layout)
plotly.offline.plot(fig, filename='d3-bubble-map-populations')
pio.write_image(fig, 'fig4.pdf')        