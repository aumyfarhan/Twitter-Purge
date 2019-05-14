import seaborn as sns
import matplotlib.pyplot as plt
#sns.set(style="white")

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(8, 1.5))

x_total=[286349,696157]
x_total_label=['286K','696K']
y_universal=['Liberal','Conservative']


x_part_1=[90490,230461]
x_part_1_label=['90K','230K']

x_part_2=[90490+81128,230461+190795]
x_part_2_label=['81K','190K']

x_part_3_label=['115K','275K']

sns.set(font_scale=1.3)
sns.set_color_codes("bright")
ax=sns.barplot(x_total,y_universal, label="Neutral",color="palegreen",saturation=0.33)

#sns.set_color_codes("muted")
ax=sns.barplot(x_part_2,y_universal, label="Positive",color="lightskyblue",saturation=0.66)
    
#sns.set_color_codes("deep")
ax=sns.barplot(x_part_1,y_universal, label="Negative", color="salmon")

ind_val=[0,100000,200000,300000,400000,500000,600000,700000]
ind_name=['0','100K','200K','300K','400K','500K','600K','700K']
plt.xticks([r  for r in ind_val], ind_name)
ax.legend(ncol=2, loc="upper right")

"""
for i, v in enumerate(x_total):
    ax.text(v + 1000, i, x_total_label[i],verticalalignment="center", color='black')
    
for i, v in enumerate(x_part_1):
    ax.text(v-(v/1.6), i, x_part_1_label[i],verticalalignment="center", color='black')
    
for i, v in enumerate(x_part_2):
    ax.text(v - (v-x_part_1[i])/1.6, i, x_part_2_label[i], verticalalignment="center",color='black')
    ax.text(v + (x_total[i]-v)/2.5, i, x_part_3_label[i],verticalalignment="center", color='black')
"""  
ax.set_ylabel('Political Bias',size=16)
ax.set_xlabel('# of tweet',size=16)
ax.set_xlim(right=ind_val[-1]+100000)
sns.despine(left=True, bottom=True)

plt.savefig('plotical_sentiment_elec4.pdf', bbox_inches="tight")