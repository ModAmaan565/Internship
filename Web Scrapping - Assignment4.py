#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Ans1


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


table = soup.find("table", {"class": "wikitable"})


rows = table.find_all("tr")


ranks = []
names = []
artists = []
upload_dates = []
views = []

for row in rows[1:]: 
    cols = row.find_all("td")
    if len(cols) >= 5:
        ranks.append(cols[0].text.strip())
        names.append(cols[1].text.strip())
        artists.append(cols[2].text.strip())
        upload_dates.append(cols[3].text.strip())
        views.append(cols[4].text.strip())


df = pd.DataFrame({
    "Rank": ranks,
    "Name": names,
    "Artist": artists,
    "Upload Date": upload_dates,
    "Views": views
})

print(df)

df.to_csv("youtube_most_viewed.csv", index=False)


# In[3]:


# Ans2


import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = "https://www.bcci.tv/"
response = session.get(url)

soup = BeautifulSoup(response.content, "html.parser")

fixtures_link = soup.find('a', text='Fixtures')['href']
full_fixtures_url = f"https://www.bcci.tv{fixtures_link}"

fixtures_response = session.get(full_fixtures_url)
fixtures_soup = BeautifulSoup(fixtures_response.content, "html.parser")

fixtures = fixtures_soup.find_all("div", class_="fixture")  
for fixture in fixtures:
    series = fixture.find("h2").text.strip()  
    place = fixture.find("span", class_="place").text.strip()  
    date = fixture.find("span", class_="date").text.strip()  
    time = fixture.find("span", class_="time").text.strip() 
    print(f"Series: {series}, Place: {place}, Date: {date}, Time: {time}")


# In[4]:


# Ans3


import requests
from bs4 import BeautifulSoup

session = requests.Session()

url = "http://statisticstimes.com/"
response = session.get(url)

soup = BeautifulSoup(response.content, "html.parser")

economy_link = soup.find('a', text='Economy')['href']
full_economy_url = f"http://statisticstimes.com{economy_link}"

economy_response = session.get(full_economy_url)
economy_soup = BeautifulSoup(economy_response.content, "html.parser")


state_gdp_link = economy_soup.find('a', text='State-wise GDP of India')['href']
full_state_gdp_url = f"http://statisticstimes.com{state_gdp_link}"

state_gdp_response = session.get(full_state_gdp_url)
state_gdp_soup = BeautifulSoup(state_gdp_response.content, "html.parser")

table = state_gdp_soup.find("table")  
rows = table.find_all("tr")

gdp_data = []

for row in rows[1:]:  
    cols = row.find_all("td")
    if len(cols) >= 6:
        rank = cols[0].text.strip()
        state = cols[1].text.strip()
        gdp_18_19 = cols[2].text.strip()
        gdp_19_20 = cols[3].text.strip()
        share_18_19 = cols[4].text.strip()
        gdp_billion = cols[5].text.strip()
        gdp_data.append({
            "Rank": rank,
            "State": state,
            "GSDP(18-19)": gdp_18_19,
            "GSDP(19-20)": gdp_19_20,
            "Share(18-19)": share_18_19,
            "GDP($ billion)": gdp_billion
        })

for data in gdp_data:
    print(data)


# In[5]:


# Ans4 


import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

charts_link = soup.find('a', text='Charts')['href']

charts_response = requests.get(charts_link)
charts_soup = BeautifulSoup(charts_response.content, "html.parser")

hot_100_link = charts_soup.find('a', href=lambda x: x and 'hot-100' in x)['href']

hot_100_response = requests.get(hot_100_link)
hot_100_soup = BeautifulSoup(hot_100_response.content, "html.parser")

songs = hot_100_soup.find_all('li', class_='o-chart-results-list-row-container')

for song in songs[:100]:  
    song_name = song.find('h3', class_='c-title').text.strip()
    artist_name = song.find('span', class_='c-label').text.strip()
    last_week_rank = song.find('span', class_='c-label').find_next('span').text.strip()
    peak_rank = song.find('span', class_='c-label').find_next('span').find_next('span').text.strip()
    weeks_on_board = song.find('span', class_='c-label').find_next('span').find_next('span').find_next('span').text.strip()

    print(f"Song: {song_name}, Artist: {artist_name}, Last Week Rank: {last_week_rank}, Peak Rank: {peak_rank}, Weeks on Board: {weeks_on_board}")


# In[6]:


# Ans 6


import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find('table')

books = []
for row in table.find_all('tr')[1:]:  
    cols = row.find_all('td')
    if len(cols) >= 5:  
        book_info = {
            "Book Name": cols[0].text.strip(),
            "Author Name": cols[1].text.strip(),
            "Volumes Sold": cols[2].text.strip(),
            "Publisher": cols[3].text.strip(),
            "Genre": cols[4].text.strip()
        }
        books.append(book_info)

for book in books:
    print(book)


# In[13]:


# Ans7
   
   
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls095964455/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

series_list = soup.find_all('div', class_='lister-item mode-detail')

series_data = []
for series in series_list:
   name = series.h3.a.text.strip()
   year_span = series.h3.find('span', class_='lister-item-year').text.strip()
   genre = series.find('span', class_='genre').text.strip()
   runtime = series.find('span', class_='runtime').text.strip()
   rating = series.find('span', class_='ipl-rating-star__rating').text.strip()
   votes = series.find('span', attrs={'name': 'nv'}).text.strip() if series.find('span', attrs={'name': 'nv'}) else 'N/A'

   series_data.append({
       "Name": name,
       "Year Span": year_span,
       "Genre": genre,
       "Run Time": runtime,
       "Ratings": rating,
       "Votes": votes
   })

for series in series_data:
   print(series)


# In[14]:


# Ans8


import requests
from bs4 import BeautifulSoup

base_url = "https://archive.ics.uci.edu/"
datasets_url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(datasets_url)
soup = BeautifulSoup(response.content, "html.parser")

all_datasets_link = soup.find('a', text='Show All Datasets')['href']
full_datasets_url = base_url + all_datasets_link

datasets_response = requests.get(full_datasets_url)
datasets_soup = BeautifulSoup(datasets_response.content, "html.parser")

datasets = datasets_soup.find_all('tr')[1:]  

dataset_details = []
for dataset in datasets:
    cols = dataset.find_all('td')
    if len(cols) >= 7: 
        dataset_info = {
            "Dataset Name": cols[0].text.strip(),
            "Data Type": cols[1].text.strip(),
            "Task": cols[2].text.strip(),
            "Attribute Type": cols[3].text.strip(),
            "No of Instances": cols[4].text.strip(),
            "No of Attributes": cols[5].text.strip(),
            "Year": cols[6].text.strip()
        }
        dataset_details.append(dataset_info)

for detail in dataset_details:
    
    print(detail)


# In[ ]:




