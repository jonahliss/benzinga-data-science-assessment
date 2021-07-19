import pandas as pd
import requests
import csv
from bs4 import BeautifulSoup

# Making list of all 199 article urls

article_data = pd.read_csv(r'C:\Users\jonah\Downloads\Article_Data.csv')
urls = article_data[["URL"]]
urls = urls.values.tolist()


# Making list of all
df = pd.read_csv(r'C:\Users\jonah\Downloads\tickers.csv')
all_tickers = df[["Tickers"]]
all_tickers = all_tickers.values.tolist()


# Function to get the word count of an article

def wordCounter(article):
    
    # Get correct html section of article
    page = requests.get(article)  
    html = BeautifulSoup(page.content, "html.parser") 
    article_content = html.find_all(class_="article-content-body")
    
    # Convert html into list
    content = []
    for words in article_content:
        words = words.text
        content.append(words)
    
    # Convert list into string
    content_string = ""
    for element in content:
        content_string += element
    
    word_count = len(content_string.split())
    
    return word_count


 # Function to get the word count of an article

def wordCounter(article):
    
    # Get correct html section of article
    page = requests.get(article)  
    html = BeautifulSoup(page.content, "html.parser") 
    article_content = html.find_all(class_="article-content-body")
    
    # Convert html into list
    content = []
    for words in article_content:
        words = words.text
        content.append(words)
    
    # Convert list into string
    content_string = ""
    for element in content:
        content_string += element
    
    word_count = len(content_string.split())
    
    return word_count
 

# Function to get the word count of an article with differnt format

def wordCounterAlternative(article):
    
    # Get correct html section of article
    page = requests.get(article)  
    html = BeautifulSoup(page.content, "html.parser") 
    article_content = html.find_all(class_="bz3-article-page__content")
    
    # Convert html into list
    content = []
    for words in article_content:
        words = words.text
        content.append(words)
    
    # Convert list into string
    content_string = ""
    for element in content:
        content_string += element
    
    word_count = len(content_string.split())
    
    return word_count
  
  
# Getting the word count for each article

word_count_list = []

for i in urls:
    for url in i:
        word_count = wordCounter(url)
        if word_count != 0:
            word_count_list.append(word_count)
        else:
            word_count_list.append(wordCounterAlternative(url))

          
# Adding word count data to the table

article_data["Word Count"] = word_count_list


# Function to retrieve the tickers of an article

def retrieveTickers(url):
    
    article_tickers_list = []
    
    page = requests.get(url)
    html = BeautifulSoup(page.content, "html.parser") 
    article_tickers = html.find_all(class_="ticker")
    
    for ticker in article_tickers:
        article_tickers_list.append(ticker.text.strip())
    
    return article_tickers_list
  
  
# Getting all of the tickers in one list

all_tickers_list = []

for i in urls:
    for url in i:
        all_tickers_list.append(retrieveTickers(url))
        
        
# Function to check for tickers

def checkForTicker(ticker):
    
    present_list = []

    for ticker_list in all_tickers_list:
        if ticker in ticker_list:
            present_list.append(1)
        else:
            present_list.append(0)
        
    return present_list
            
            
# Adding data for the tickers to the table

for i in all_tickers:
    for ticker in i:
         article_data[ticker] = checkForTicker(ticker)    
        
        
# Exporting article data to CSV

article_data.to_csv(r'C:\Users\jonah\Downloads\Article_Data_New.csv', index = False)


# Starting work on step 2

article_data = pd.read_csv(r'C:\Users\jonah\Downloads\Article_Data.csv')


# Determining the existing sections

section_list = []

for section in article_data["Section"]:
    if section not in section_list:
        section_list.append(section)
        
        
# Creating table

section_data = []
section_data = pd.DataFrame(section_data)
section_data["Section"] = section_list


# Function to get the average views and visitors for each section 

def getAverages(metric):
    
    master_average = []
    
    for section in section_list:

        i = 0
        x = 0
        total = 0
        
        for item in article_data["Section"]:
            if item == section:
                total += (article_data[metric])[i]
                i += 1
                x += 1
            else:
                i += 1
        
        average = total / x
        
        master_average.append(average)
        
    section_data["Average " + metric] = master_average
    
getAverages("Views")
getAverages("Visitors")


# Function to get the variances for both the views and visitors of each section 

def getVariances(metric):
    
    master_variance = []  
    
    y = 0
    
    for section in section_list:

        total = 0
        i = 0
        x = 0
        
        for item in article_data["Section"]:
            if item == section:
                total += ((article_data[metric][i] - section_data["Average " + metric][y]) ** 2)
                i += 1
                x += 1
            else:
                i += 1
        
        total = total / x
        
        master_variance.append(total)
        
        y += 1
        
    section_data[metric + " Variance"] = master_variance
    
getVariances("Views")
getVariances("Visitors")


# Exporting section data to CSV

section_data.to_csv(r'C:\Users\jonah\Downloads\Section_Data.csv', index = False)
