import pandas as pd
from bs4 import BeautifulSoup
import requests
from typing import List
from random import sample

### Variables
file = 'links.csv'
column = 'Link NL'

# returns list of links
def get_links(file: str, column: str, remove_duplicates=True) -> List[str]:
    df = pd.read_csv(file, usecols=[column])
    df = df[column].apply(lambda x: str(x).replace('article', 'article_body', 1))
    links = df.tolist()
    if remove_duplicates:
        links = list(set(links))
    return links


# returns list of scraped text from all links
def get_text(links: List[str], sample_fraction=1) ->List[str]:
    list_text = []
    links = sample(links, int(sample_fraction * len(links)))
    for url in links:
        soup = BeautifulSoup(requests.get(url).content, "lxml")
        Text = ''
        active = False
        for i in soup.find_all(text=True):
            if 'Voor de raadpleging van' in i or 'eerste woord' in i:
                active = False
            if active:
                if i.strip() != '':
                    Text += ' ' + i.strip().replace('\n','')
            if 'Numac' in i:
                active = True
        list_text.append(Text[1:-6])
    print(links)
    return list_text



links = get_links(file, column)
print(get_text(links, sample_fraction=1/len(links)))