import pandas as pd

chunk_size = 1000
chunks2 = []

for chunk2 in pd.read_csv('data.csv',chunksize=chunk_size,usecols=['id','lang']):    
    chunks2.append(chunk2)

data_frame = pd.concat(chunks2,axis=0)

del chunk2
del chunks2

data_series_lang = data_frame["lang"]
data_series_lang = data_series_lang.dropna(how='any')

total_user_count = data_series_lang.count()

language_count_hist = data_frame.groupby(data_frame["lang"])["lang"].count() / total_user_count

language_count_hist_sorted = language_count_hist.sort_values(ascending = False)
