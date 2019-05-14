
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from nltk import FreqDist
from nltk.util import ngrams
import matplotlib.pyplot as plt
from wordcloud import WordCloud
#####
import re
import string

import warnings
import psycopg2

conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cursor=conn.cursor()

sql_command2='''select tweet_text from conservative_sentiment where sentiment_label='NGT';'''

cursor.execute(sql_command2)

conn.commit()

data2=cursor.fetchall()
conn.close()


all_tweet_list=[x[0] for x in data2]


warnings.filterwarnings("ignore")

punctuation = [x for x in string.punctuation]
stop_words = stopwords.words('english') + punctuation + ['rt', 'via',"i'm","don't"]

pat1 = r'@[A-Za-z0-9_]+'
pat2 = r'https?://[^ ]+'
combined_pat = r'|'.join((pat1, pat2))
www_pat = r'www.[^ ]+'

tokenizer = TweetTokenizer()

def tweet_tokenizer(verbatim):
    try:
        stripped = re.sub(combined_pat, '', verbatim)
        stripped = re.sub(www_pat, '', stripped)
        lower_case = stripped.lower()
        letters_only = re.sub("[^a-zA-Z]", " ", lower_case)
    
        all_tokens = tokenizer.tokenize(letters_only)
        
        # this line filters out all tokens that are entirely non-alphabetic characters
        filtered_tokens = [t for t in all_tokens if t.islower()]
        # filter out all tokens that are <2 chars
        filtered_tokens = [x for x in filtered_tokens if len(x)>1]
        
        filtered_tokens = [term for term in filtered_tokens if term not in stop_words]
        
        out_text=' '.join(filtered_tokens)
    except IndexError:
        out_text=''
        filtered_tokens = []
    return(out_text)
    

test_bed=[tweet_tokenizer(x) for x in all_tweet_list]

all_concat_str=' '.join(test_bed)
freq_dist_count=FreqDist(ngrams(all_concat_str.split(), 2))                  
#freq_dist_count=FreqDist(all_concat_str.split())   

to_WC=freq_dist_count.most_common(100)

to_WC2=[]
for bgm in to_WC:
    to_WC2.append(((bgm[0][0]+'_'+bgm[0][1]),bgm[1]))

wordcloud_purged = WordCloud(max_font_size=120, max_words=50, background_color="white",\
                      width=800, height=600)\
                      .generate_from_frequencies(dict(to_WC2))

plt.figure()
plt.imshow(wordcloud_purged, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud_purged.to_file("WC_BIGRAM_CON_NEG_T100.png")         