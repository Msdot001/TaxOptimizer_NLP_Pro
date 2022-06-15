from langdetect import detect_langs


def clean(article: str, language="nl", write_text=False, dest_file=None, treshold=0.99) -> str:

    """ 
    Function to remove unnecessary text from the scraped articles. Discards articles that are not in the desired language.
    arguments and keywords:
    article: path to textfile
    language: desired language of article
    write_text: True if you want to write the cleaned article to a textfile
    dest_file: name of file where the cleaned article gets written to (if write_text=True)
    treshold: if the certainty that the language of the article is the same as the desired language is lower than this treshold, the article gts discarded
    """
    
    with open(article, "r") as f:
        text = f.read().split(" ")

        if "Numac" in text:
            ind_numac = text.index("Numac")
        else:
            return

        if "-" in text[ind_numac:]:
            ind_start = text[ind_numac:].index("-") + ind_numac + 1
        else:
            return None

        text = text[ind_start:]

        if "Numac" in text:
            ind_end = text.index("Numac") - 8
        else:
            return None

        text = text[:ind_end]
        text = " ".join(text)

        x = detect_langs(text)[0]

        if x.lang == language.lower() and x.prob > treshold:
            if write_text:
                with open(dest_file, "w", errors="ignore") as f:
                    f.write(text)
            else:
                return text
