from langdetect import detect_langs



# language should be nl or fr

def clean(article, language, dest_file, treshold=.9):
    
    with open(article, 'r') as f:
        text = f.read().split(' ')
        
        if 'Numac' in text:
            ind_numac = text.index('Numac')
        else:
            return
            
        if '-' in text[ind_numac:]:
            ind_start = text[ind_numac:].index('-') + ind_numac + 1
        else:
            return
        
        text = text[ind_start:]
        
        if 'Numac' in text:
            ind_end = text.index('Numac') - 8
        else:
            return
        
        text = text[:ind_end]
        text = ' '.join(text)
        
        x = detect_langs(text)[0]
        
        if x.lang == language.lower() and x.prob > treshold:
            with open(dest_file, 'w', errors='ignore') as f:
                f.write(text)
 
                
 
                
for i in range(786):
    article = 'text_nl/article_' + str(i) + '.txt'
    dest_file = 'clean_text_nl/article_' + str(i) + '.txt'
    clean(article, 'nl', dest_file)


for i in range(786):
    article = 'text_fr/article_' + str(i) + '.txt'
    dest_file = 'clean_text_fr/article_' + str(i) + '.txt'
    clean(article, 'fr', dest_file)
