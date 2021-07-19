# benzinga-data-science-assessment
Web scraping and processing

Problem Definition: You are given as input a CSV, named Article_Data.csv, which consists of 200 links to articles on Benzinga.com written by Benzinga Insights, of differing types (specified by Section), along with other metrics on the articles. You are also given another CSV (tickers.csv) with all the tickers in the Benzinga universe.

Goal: 

1. Extract from each article, the ticker symbols that are present in each from the list of tickers in tickers.csv. Store them in the same CSV file given to you (Article_Data.csv) as additional column(s) where each cell of the new ticker columns is 1 if the ticker is presentin an article and 0 otherwise.

2. Group each article by Section and report each sections mean and variance across viewers and visitors. Store these metrics for each grouping in a different CSV.

3. For each article compute the total word count, you do not have to include title, store this info for each article as an additional column in the same Article_Data.csv.Deliverable 

Instructions:

1. Provide all code in the form of Python script(s) (e.g. scraper.py).

2. Submit a link to the GitHub repository where the code lives. Please include a README.md in the repo.

3. This code should run in the same directory as the article CSV you are given as input.

4. Code quality is important, please try to follow an Object-Oriented programming paradigm and PEP-8 guidelines.NOTE: If at any point you get stuck on the assignment and cannot figure out how to do something, do not hesitate to reach out with questions. If you are confused about the instructions or the definitions of certain words, please reach out at any time.
