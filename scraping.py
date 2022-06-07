import pandas as pd
from bs4 import BeautifulSoup
import requests
from typing import List
from random import sample

### Variables
file = 'links.csv'
language = 'NL'   #should be FR or NL

# returns list of links
def get_links(file: str, remove_duplicates=True) -> List[str]:
    df = pd.read_csv(file, usecols=['Link FR'])
    df = df['Link FR'].apply(lambda x: str(x).replace('article', 'article_body', 1))
    links = df.tolist()
    if remove_duplicates:
        links = list(set(links))
    return links


# returns list of scraped text from all links
def get_text(links: List[str], language, sample_size='all', drop_german=True) ->List[str]:
    list_text = []
    if sample_size != 'all':
        links = sample(links, sample_size)
        
    if language == 'FR':
        deactivation_str = ['premier mot', 'Pour la consultation']
        german_str = 'traduction allemande'
        
    if language == 'NL':
        deactivation_str = ['eerste woord', 'Voor de raadpleging van']
        german_str = 'Duitse vertaling'
        links = [link.replace('language=fr', 'language=nl') for link in links]
    
    for url in links:
        soup = BeautifulSoup(requests.get(url).content, "lxml")
        Text = ''
        active = False
        for i in soup.find_all(text=True):
            if deactivation_str[0] in i or deactivation_str[1] in i:
                active = False
            if active:
                if i.strip() != '':
                    Text += ' ' + i.strip().replace('\n','')
            if 'Numac' in i:
                active = True
        if drop_german and (german_str in Text):
            continue
        list_text.append(Text[1:-6])
    return list_text



links = get_links(file)
print(get_text(links, language, sample_size=1, drop_german=True))