import pandas as pd
from bs4 import BeautifulSoup
import requests
from typing import List
from random import sample

##################### Variables
file = 'links.csv'

#should be FR or NL
language = 'NL'

#rel dir where textfiles are written to, should exist before running
text_folder = 'text_nl' 


# returns list of links
def get_links(file: str, remove_duplicates=True) -> List[str]:
    df = pd.read_csv(file, usecols=['Link FR'])
    df = df['Link FR'].apply(lambda x: str(x).replace('article', 'article_body', 1))
    links = df.tolist()
    if remove_duplicates:
        links = list(set(links))
    return links


# returns list of scraped text from all links
def get_text(links: List[str], language, sample_size='all',
             write_to_textfile=False) ->List[str]:
    list_text = []
    if sample_size != 'all':
        links = sample(links, sample_size)
        
    if language == 'NL':
        links = [link.replace('language=fr', 'language=nl') for link in links]
    
    for url in links:
        soup = BeautifulSoup(requests.get(url).content, "lxml")
        Text = ''
        for i in soup.find_all(text=True):
            if i.strip() != '':
                Text += ' ' + i.strip().replace('\n','')
        list_text.append(Text)
    
    if write_to_textfile:
        n = 0
        for i in list_text:
            filename = str(text_folder) + '/article_' + str(n) + '.txt'
            n += 1
            with open(filename, 'w', errors='ignore') as f:
                f.write(i)
    
    else:
        return list_text