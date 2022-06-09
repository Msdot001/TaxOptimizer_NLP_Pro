from utils.cleaning import clean
# from utils.preprocessing import preprocess
import os
from googletrans import Translator


# folder with original raw text
folder_raw_text = '/text_nl_sample/'

# make list with path of all these raw text files
path = os.getcwd().replace('\\', '/') + folder_raw_text
raw_text_files = [path + i for i in os.listdir(path)]

# perform clean function on all raw text files. Some files will get dropped
cleaned_text = [clean(file, 'nl' ) for file in raw_text_files]

# initiate google translator
translator = Translator()

# translate every text to english
english_text = [translator.translate(file).text for file in cleaned_text]


# preprocess english_text
# final_text = [preprocess(file) for file in english_text]

