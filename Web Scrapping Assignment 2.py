#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ans1:-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Setup Chrome WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path to your chromedriver

# Step 1: Open the Naukri.com page
driver.get('https://www.naukri.com/')
time.sleep(2)  # Wait for the page to load

# Step 2: Enter “Data Scientist” in the search box
search_box = driver.find_element(By.ID, 'qsb-keyword-sugg')
search_box.send_keys('Data Scientist')

# Step 3: Click the search button
search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
search_button.click()

# Step 4: Apply Location and Salary Filter
time.sleep(3)  # Wait for the search results to load
location_filter = driver.find_element(By.XPATH, "//span[contains(text(),'Delhi / NCR')]")
location_filter.click()

time.sleep(2)
salary_filter = driver.find_element(By.XPATH, "//span[contains(text(),'3-6 Lakhs')]")
salary_filter.click()

# Step 5: Scrape the first 10 job results
time.sleep(2)  # Wait for the page to load after applying filters
job_titles = driver.find_elements(By.XPATH, "//a[@class='title fw500 ellipsis']")
job_locations = driver.find_elements(By.XPATH, "//li[@class='fleft grey-text br2 placeHolderLi location']/span")
company_names = driver.find_elements(By.XPATH, "//a[@class='subTitle ellipsis fleft']")
experience_required = driver.find_elements(By.XPATH, "//li[@class='fleft grey-text br2 placeHolderLi experience']/span")

# Creating lists to store the data
titles, locations, companies, experiences = [], [], [], []

# Scraping data for the first 10 jobs
for i in range(10):
    titles.append(job_titles[i].text)
    locations.append(job_locations[i].text)
    companies.append(company_names[i].text)
    experiences.append(experience_required[i].text)

# Step 6: Create a DataFrame from the scraped data
jobs_df = pd.DataFrame({
    'Job Title': titles,
    'Location': locations,
    'Company Name': companies,
    'Experience Required': experiences
})

# Save the DataFrame to a CSV file
jobs_df.to_csv('naukri_data_scientist_jobs.csv', index=False)

# Close the browser
driver.quit()

print("Scraping complete. Data saved to 'naukri_data_scientist_jobs.csv'")


# In[2]:


# Ans2:-


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Setup Chrome WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path to your chromedriver

# Step 1: Open the Shine website
driver.get('https://www.shine.com/')
time.sleep(2)  # Allow the page to load

# Step 2: Enter “Data Analyst” in the job title field and “Bangalore” in the location field
job_title_field = driver.find_element(By.ID, 'id_q')
job_title_field.send_keys('Data Analyst')

location_field = driver.find_element(By.ID, 'id_loc')
location_field.send_keys('Bangalore')

# Step 3: Click the search button
search_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary search']")
search_button.click()

# Step 4: Scrape the first 10 job results
time.sleep(3)  # Wait for the results to load

# Finding the job elements
job_titles = driver.find_elements(By.XPATH, "//h2[@class='job_title']")
job_locations = driver.find_elements(By.XPATH, "//div[@class='job_loc']")
company_names = driver.find_elements(By.XPATH, "//div[@class='job_company_name']")
experience_required = driver.find_elements(By.XPATH, "//li[contains(@class,'exp')]")

titles, locations, companies, experiences = [], [], [], []

for i in range(10):
    titles.append(job_titles[i].text if i < len(job_titles) else 'N/A')
    locations.append(job_locations[i].text if i < len(job_locations) else 'N/A')
    companies.append(company_names[i].text if i < len(company_names) else 'N/A')
    experiences.append(experience_required[i].text if i < len(experience_required) else 'N/A')

# Step 5: Create a DataFrame from the scraped data
jobs_df = pd.DataFrame({
    'Job Title': titles,
    'Location': locations,
    'Company Name': companies,
    'Experience Required': experiences
})

jobs_df.to_csv('shine_data_analyst_jobs_bangalore.csv', index=False)


driver.quit()

print("Scraping complete. Data saved to 'shine_data_analyst_jobs_bangalore.csv'")


# In[3]:


# Ans4:-



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Setup Chrome WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Update the path to your chromedriver

# Open the Flipkart reviews page for iPhone 11
url = "https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY"
driver.get(url)
time.sleep(3)  # Wait for the page to load

# Lists to store scraped data
ratings = []
review_summaries = []
full_reviews = []

# Loop through multiple pages to scrape 100 reviews
while len(ratings) < 100:
    # Step 1: Find review elements (rating, review summary, and full review)
    review_blocks = driver.find_elements(By.XPATH, "//div[@class='_1AtVbE']//div[@class='col _2wzgFH K0kLPL']")

    for block in review_blocks:
        # Extract rating
        try:
            rating = block.find_element(By.XPATH, ".//div[@class='_3LWZlK _1BLPMq']").text
        except:
            rating = 'N/A'
        
        # Extract review summary (title of the review)
        try:
            review_summary = block.find_element(By.XPATH, ".//p[@class='_2-N8zT']").text
        except:
            review_summary = 'N/A'
        
        # Extract full review (body of the review)
        try:
            full_review = block.find_element(By.XPATH, ".//div[@class='t-ZTKy']").text
        except:
            full_review = 'N/A'
        
        # Append the data to the respective lists
        ratings.append(rating)
        review_summaries.append(review_summary)
        full_reviews.append(full_review)
        
        # Break if we reach 100 reviews
        if len(ratings) >= 100:
            break

    # Step 2: Click the "Next" button to go to the next page of reviews
    try:
        next_button = driver.find_element(By.XPATH, "//a[@class='_1LKTO3'][last()]")
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
    except:
        print("No more pages to scrape.")
        break

# Step 3: Create a DataFrame with the scraped data
reviews_df = pd.DataFrame({
    'Rating': ratings[:100],  # Limit to 100 reviews
    'Review Summary': review_summaries[:100],
    'Full Review': full_reviews[:100]
})

# Step 4: Save the DataFrame to a CSV file
reviews_df.to_csv('flipkart_iphone11_reviews.csv', index=False)

# Close the browser
driver.quit()

print("Scraping complete. Data saved to 'flipkart_iphone11_reviews.csv'.")


# In[ ]:




