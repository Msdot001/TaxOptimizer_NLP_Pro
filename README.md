<h2> <align="center">KPMG Tax Documents - Natural Language Processing</h1>
<p align="center"><img src="https://www.todaysoftmag.com/images/articles/tsm64/a41.jpg" width="500" height="300"></p>




## Host organization:
<a href="https://github.com/becodeorg"><strong>BeCode</strong></a>(Ghent campus)
<img src="https://becode.org/app/uploads/2021/06/logo-becode.png" alt="Logo" width="200" height="200">
  
## Client organization:
<a href="https://www.linkedin.com/company/kpmg-belgium/?originalSubdomain=be"><strong>KPMG</strong></a>(Belgium)
<img src="image\KMPG.png" alt="Logo" width="200" height="200">


## The timeline of the project:
2 weeks - **01/06/2022 - 16/06/2022**

## Project Goal: 
Creating a tool which scrapes the [National Gazette](http://www.ejustice.just.fgov.be/cgi/welcome.pl) and extracts the content relevant to client.

* Scrape legal content
* Use Natural Language Processing to analyze text
* Classify tax-related documents based on their content

## Dataset details:
Link.csv with attributes:"Date of release of laws", "Titles" and "url links to both French and Dutch versions of the laws".


## Description:
We are tasked by KPMG Belgium to work on a NLP-based prototype for automating the process of detecting tax-related law changes. 

The steps we have taken:
* Scrapping of documents using the Dutch urls from [National Gazette](http://www.ejustice.just.fgov.be/cgi/welcome.pl)
* Cleaning the documents to make it more readable and understandable.
* Preprocessing the documents to remove the stopwords, strip the tags, numerics, multiple whitespaces,punctuations, tokenization and lemmatization. 
* Unsupervised Topic modelling using Latent Dirichlet Allocation Model (LDA) setting number of topics to 10
* Generating the labels from the topics 
* NLP Streamlit App capable to visualise "Lemma", "Name Entity Recongnition", "Words importances", "Summaries text"

  
## Usage 
We are using jupyter notebooks:
  * Functions for scraping the documents from the Dutch urls
  * Functions for cleaning the scraped documents
  * Functions for preprocessing the cleaned documents
  * Latent Dirichlet Allocation Model (LDA)
  * NLP Streamlit App

### App Usage:
To open the heroku application, follow the link [Heroku](https://textoptimizerapp.herokuapp.com/)

## Result

### Visualisation of the LDA model with pyLDAvis
<p align="center"><img src="image\LDA_modelVisualisation.png" alt="Logo" width="400" height="250"></p>

### Cloud of Words
<p align="center"><img src="image\Topic.png" alt="Logo" width="400" height="250"></p>

### Streamlit App Interface
<p align="center"><img src="image\App.png" alt="Logo" width="400" height="250"></p>

### Bar showing words importance 
<p align="center"><img src="image\bar1.png" alt="Logo" width="400" height="250"></p>


## Used Language and Libraries:
Python / libraries:
* Numpy
* Pandas 
* spacy
* Matplotlib
* sklearn
* langdetect
* BeautifulSoup
* Gensim
* Streamlit

## Repo Architecture 

```

│   README.md                     : This file
│   data                          : contains raw data and preprocesses data
│   utils                         : contains all the Scripts for scraping, cleaning, preprocessing. 
│   notebooks                     : contains scripts for running model and translating
│   app                           : contain scripts for running the streamlit NLP app.
│   image                         : contains images

│   requirements.txt              : conatins libraries require for runing the stramlit NLP app.
│___   
|    data          
│   │ links.csv                   : All url adresses from National Gazette, not cleaned.
│   │ dataframe.csv               : All scraped urls, content of the document, cleaned and preprocessed.        
│___  
|    utils
|   | scraping.py                 : Scipt used for scraping the documents.
│   | cleaning.py                 : Script used for cleaning the scraped documents.
│   │ preprocessing.py            : Script used preprocessing  the cleaned data.#
│___ 
│   app
│   │ app.py                      : Script for running the streamlit NLP app.
│   │ preprocessapp.py            : Script for preprocessing for the app. 
│   │ setup.sh
│   │ Profile
│___ 
│   notebooks
│   │ Topic Nodeling Dutcg.ipynb  
│   │ translating_notebook.ipynb

```
## Team name: TaxOptimizer_NLP_Pro: 
<a href="https://github.com/Moshood Owolabi">Moshood Owolabi, 
<a href="https://www.linkedin.com/in/pieter-van-hoefs">Pieter Van Hoefs,
<a href="https://www.linkedin.com/in/sebastiangarciamartinez">Sebastián García Martínez, 
<a href="https://www.linkedin.com/in/havva-ebrahimi-pour"> Havva Ebrahimi Pour</a>
