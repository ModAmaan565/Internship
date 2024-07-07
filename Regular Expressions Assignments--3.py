#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Ans1:-

import re

def replace_with_colon(text):
    characters_to_replace = [' ', ',', '.']
    
    for char in characters_to_replace:
        text = text.replace(char, ':')
    
    return text

sample_text = 'Python Exercises, PHP exercises.'

output_text = replace_with_colon(sample_text)
print("Original Text:", sample_text)
print("Expected Output:", output_text)




# In[6]:


# Ans2:-

import pandas as pd
import re

data = {
    'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']
}
df = pd.DataFrame(data)

df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

print(df)


# In[7]:


import pandas as pd
import re

data = {
    'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']
}
df = pd.DataFrame(data)

df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'[^\w\s]', '', x))

df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

print(df)


# In[9]:


import pandas as pd
import re

data = {
    'SUMMARY': ['hello, world!', 'XXXXX test', '123four, five:; six...']
}
df = pd.DataFrame(data)

def clean_summary(summary):
    # Remove everything except words (letters)
    clean_text = re.sub(r'[^\w\s]', '', summary)
    # Remove any extra whitespace
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

df['SUMMARY'] = df['SUMMARY'].apply(clean_summary)
print(df)


# In[10]:


def find_long_words(text):
    pattern = re.compile(r'\b\w{4,}\b')
    
    long_words = pattern.findall(text)
    
    return long_words

text = "This is an example sentence with several long words."
print(find_long_words(text))


# In[11]:


# Ans 4

import re

def find_specific_length_words(text):
    pattern = re.compile(r'\b\w{3,5}\b')
    
    specific_length_words = pattern.findall(text)
    
    return specific_length_words

text = "This is an example with some three, four, and five character words."
print(find_specific_length_words(text))


# In[12]:


#Ans7:-

def split_on_uppercase(text):
    pattern = re.compile(r'(?=[A-Z])')
    
    words = pattern.split(text)
    
    words = [word for word in words if word]
    
    return words

sample_text = "ImportanceOfRegularExpressionsInPython"
print(split_on_uppercase(sample_text))


# In[13]:


# Ans8:-

def insert_spaces_before_numbers(text):
    pattern = re.compile(r'(?=\d)')
    
    result = pattern.sub(' ', text)
    
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
print(insert_spaces_before_numbers(sample_text))


# In[14]:


#Ans9:-

import re

def insert_spaces_before_capitals_and_numbers(text):
    pattern = re.compile(r'(?=[A-Z0-9])')
    
    result = pattern.sub(' ', text).strip()
    
    return result

sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
print(insert_spaces_before_capitals_and_numbers(sample_text))


# In[15]:


#Ans10:-

import pandas as pd

url = 'https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv'

df = pd.read_csv(url)

df['first_six_letters'] = df['Country'].str[:6]

print(df.head())


# In[16]:


# Ans 11:-

import re

def match_string(input_string):
    pattern = r'^[a-zA-Z0-9_]+$'
    if re.match(pattern, input_string):
        return True
    else:
        return False

strings_to_test = [
    "Hello_World123",
    "Python_3",
    "User_Name",
    "example123",
    "invalid string!",
    "12_34_ABC"
]

for string in strings_to_test:
    if match_string(string):
        print(f"{string}: Matches")
    else:
        print(f"{string}: Does not match")


# In[17]:


# Ans14:-

sample_text = 'On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'

pattern = r'\b([A-Z][a-z]+) (\d{1,2}(st|nd|rd|th)) (\d{4})\b'

match = re.search(pattern, sample_text)

if match:
    date_string = match.group(0)
    print(f"Extracted Date: {date_string}")
else:
    print("Date string not found in the text.")


# In[18]:


# Ans15:-

def search_strings(text, searched_words):
    found_words = []
    for word in searched_words:
        if word in text:
            found_words.append(word)
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_words = ['fox', 'dog', 'horse']

found_words = search_strings(sample_text, searched_words)

if found_words:
    print(f"Found words: {', '.join(found_words)}")
else:
    print("No searched words found in the text.")


# In[19]:


# Ans16:-

def search_string_and_location(text, pattern):
    found_positions = []
    index = text.find(pattern)
    while index != -1:
        found_positions.append(index)
        index = text.find(pattern, index + 1)
    return found_positions

sample_text = 'The quick brown fox jumps over the lazy dog.'

searched_word = 'fox'

positions = search_string_and_location(sample_text, searched_word)

if positions:
    print(f"Found '{searched_word}' at positions: {positions}")
else:
    print(f"'{searched_word}' not found in the text.")


# In[21]:


# Ans17:-

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))


# In[22]:


#Ans19:-


def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


# In[23]:


# Ans20:-

def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    return pattern.findall(text)

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

decimal_numbers = find_decimal_numbers(sample_text)

print("Expected Output:", decimal_numbers)


# In[24]:


# Ans21:-

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


# In[25]:


# Ans23:-

def insert_spaces(text):
    words = re.findall(r'[a-z]+|[A-Z][a-z]*', text)
    
    spaced_text = ' '.join(words)
    
    return spaced_text

sample_text = "RegularExpressionIsAnImportantTopicInPython"

output_text = insert_spaces(sample_text)

print("Expected Output:", output_text)


# In[26]:


# Ans24:-

sample_text = "RegularExpressionIsAnImportantTopicInPython"

pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, sample_text)

print("Matches found:", matches)


# In[33]:


# Ans25:-

import re

def remove_continuous_duplicates(sentence): 
    pattern = r'\b(\w+)( \1\b)+'
    
    cleaned_sentence = re.sub(pattern, r'\1', sentence)
    
    return cleaned_sentence

sample_text = "Hello hello world world"

output_text = remove_continuous_duplicates(sample_text)
print("Expected Output:", output_text)


# In[28]:


# Ans26:-

def ends_with_alphanumeric(text):
    pattern = r'\w$'  
    return bool(re.search(pattern, text))

strings = [
    "Hello123",    
    "World456!",  
    "Python3.9",   
    "2024",        
    "Regex!"       
]

for s in strings:
    if ends_with_alphanumeric(s):
        print(f"{s}: Ends with alphanumeric")
    else:
        print(f"{s}: Does not end with alphanumeric")


# In[29]:


# Ans27:-

def extract_hashtags(text):
    pattern = r'\#\w+'
    
    hashtags = re.findall(pattern, text)
    
    return hashtags

sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

hashtags = extract_hashtags(sample_text)

print("Expected Output:", hashtags)


# In[30]:


# Ans28:-

def remove_u_plus_symbols(text):
    pattern = r'<U\+[0-9A-Fa-f]{2,4}>'
    
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text

sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

output_text = remove_u_plus_symbols(sample_text)

print("Expected Output:", output_text)


# In[35]:


# Ans30:-
def remove_words_by_length(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    
    cleaned_text = pattern.sub('', text)
    
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

output_text = remove_words_by_length(sample_text)

print("Expected Output:", output_text)


# In[ ]:




