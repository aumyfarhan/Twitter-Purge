
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2
import collections
conn2 = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor2=conn2.cursor()

sql_command2='''select shorturl from elec_prgd_tweet_shorturl;'''

cursor2.execute(sql_command2)

conn2.commit()

data3=cursor2.fetchall()

cursor2.close()
conn2.close()


elec_urls=[x[0] for x in data3]

elec_url_count=collections.Counter(elec_urls)

elec_url_count_top=elec_url_count.most_common(15)

url=[x[0] for x in elec_url_count_top]
val=[x[1] for x in elec_url_count_top]


# Initialize the matplotlib figure
#sns.set(style="white")

fig = plt.figure(figsize=(8,6))
ax = plt.gca()

sns.set(font_scale=1.5)
sns.set_color_codes("pastel")

ax=sns.barplot(val,url, label="pastel",color="indianred")
ax.set_xscale('log')
ax.set_ylabel('URLs')
ax.set_xlabel('Count (in log scale)')
ax.set_xlim(right=val[0]+200000)

for xxx,i in enumerate(ax.patches):
    # get_x pulls left or right; get_height pushes up or down
    ax.text( i.get_width()+15+i.get_width()*0.03, i.get_y()+0.4,\
            int(round(i.get_width())),verticalalignment="center", fontsize=12 ,color='black')
plt.savefig('elec_url_count2.pdf', bbox_inches="tight")   
plt.show()