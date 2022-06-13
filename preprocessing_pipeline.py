from utils.cleaning import clean
from utils.preprocessing import preprocess
from utils.scraping import get_links
import os
import pandas as pd



# folder with original raw text
folder_raw_text = '/text_nl/'

# make list with path of all these raw text files
path = os.getcwd().replace('\\', '/') + folder_raw_text
raw_text_files = [path + i for i in os.listdir(path)]

# perform clean function on all raw text files. Some files will get dropped
cleaned_text = [clean(file, 'nl' ) for file in raw_text_files]


# preprocess english_text
final_text = [preprocess(file) for file in cleaned_text]



# set destination folder
# dest_folder = 'final_text/'

# write all articles to textfiles
# i = 0

# for text in final_text:
#     if text != None:
#         file_name = dest_folder + 'article_' + str(i) + '.txt'
#         with open(file_name, 'w', errors='ignore') as f:
#             f.write(text)
#     i += 1



links = get_links('links.csv')


df = pd.DataFrame()

df['url'] = links
df['content'] = final_text

df.dropna(inplace=True)
df.drop_duplicates(inplace=True, subset=['content'])

df.to_csv('dataframe.csv', index=False)
