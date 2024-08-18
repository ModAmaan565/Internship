#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[11]:


# Answer 1.


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.imdb.com/list/ls056092300/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = []
years = []
ratings = []

for movie in soup.find_all('div', class_='lister-item mode-detail'):
    title = movie.h3.a.text
    titles.append(title)
    year = 
    movie.h3.find('span', class_='lister-item-year').text.strip("()")
    years.append(year)
 
    rating = movie.find('span', class_='ipl-rating-star__rating').text
    ratings.append(rating)

df = pd.DataFrame({
    'Title': titles,
    'Year': years,
    'Rating': ratings
})

print(df)


# In[12]:





# In[14]:


# Answer 5


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cnbc.com/world/?region=world")
soup = BeautifulSoup(response.content, 'html.parser')

headings = []
dates = []
news_links = []

articles = soup.find_all('div', class_='Card-titleAndSubtitle')

for article in articles:
    heading = article.find('a').text.strip()
    headings.append(heading)

    link = article.find('a')['href']
    news_links.append(link)

    date = article.find('time')
    dates.append(date.text if date else 'No Date')

for i in range(len(headings)):
    print(f"Heading: {headings[i]}")
    print(f"Date: {dates[i]}")
    print(f"Link: {news_links[i]}\n")


# In[ ]:


# Answer 6.

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cnbc.com/world/?region=world")
soup = BeautifulSoup(response.content, 'html.parser')

headings = []
dates = []
news_links = []

articles = soup.find_all('div', class_='Card-titleAndSubtitle')

for article in articles:

    heading = article.find('a').text.strip()
    headings.append(heading)

    link = article.find('a')['href']
    news_links.append(link)

    date = article.find('time')
    dates.append(date.text if date else 'No Date')

for i in range(len(headings)):
    print(f"Heading: {headings[i]}")
    print(f"Date: {dates[i]}")
    print(f"Link: {news_links[i]}\n")

