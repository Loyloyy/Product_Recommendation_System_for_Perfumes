from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import pandas as pd
from Sel_Scraper_function import get_them_all

i = 0
j = 1
k = 1
x = 1

# Creating the dataframe to store the scaped data
df = pd.DataFrame(columns=['Name', 'Year', 'Sex', 'Designer', 'MainAccords1', 'MainAccords2'
                            , 'MainAccords3', 'MainAccords4', 'MainAccords5', 'dayornight','HaveRating'
                            , 'HadRating', 'WantRating', 'SignatureRating', 'PerfumeRating', 'Number_Votes'
                            , 'LongevityPoor', 'LongevityWeak', 'LongevityModerate', 'LongevityLong'
                            , 'LongevityVeryLong', 'SillageSoft', 'SillageModerate', 'SillageHeavy'
                            , 'SillageEnormous', 'consumerMainNoteType1', 'consumerMainNoteType2'
                            , 'consumerMainNoteType3', 'consumerMainNoteType4', 'consumerMainNoteType5'
                            , 'consumerMainNoteType6', 'consumerMainNoteType7', 'consumerMainNoteType8'
                            , 'consumerMainNoteType9','consumerMainNoteType10', 'consumerMainNoteType11'
                            , 'consumerMainNoteType12', 'consumerMainNoteType13', 'consumerMainNoteType14'
                            , 'consumerMainNoteType15', 'consumerMainNoteType16', 'consumerMainNoteType17'
                            , 'consumerMainNoteType18', 'consumerMainNoteType19', 'consumerMainNoteType20'])

#--| Setup1793
options = Options()
#options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
#--| Parse or automation

# Setting up the link to scrape the data from
browser.get('XXXwebsite_to_scrapeXXX')

# The loop function will scrape and store all the perfume names into the csv
def loop(i, list, name):
    for this in list:
        i = i + 1
        df.loc[i, name] = this.text

# The doubleloop function will store the intended sex of the perfume along with the year the perfume was released
def doubleloop(i, list, name1, name2, j, k):
    for this in list:
        i += 1
        if i % 2 == 0:
            df.loc[j, name1] = this.text
            j += 1
        else:
            df.loc[k, name2] = this.text
            k += 1

# Creating a list to store all the links scapred to push into the get_them_all function later
links = []

# Extracting the perfume links from HTML and adding them into the link list
posts = browser.find_elements_by_xpath('//div[@class="flex-child-auto"]/h3/a[@href]')
for post in posts:
    links.append(post.get_attribute("href"))

# Scraping the perfume names, year and intended sex
namelist = browser.find_elements_by_xpath('//div[@class="flex-child-auto"]/h3/a[@href]')
yearsexlist =  browser.find_elements_by_xpath('//div[@class="flex-container align-justify "]/span')

# Executing the functions to get perfume names, year and intended sex
loop(i, namelist, 'Name')
doubleloop(i, yearsexlist ,'Year', 'Sex', j, k)

# Counting the length of the links
# This will be used for uddating the scraping user on the script's progress
y = len(links)

# Creating a for loop to scrape all the wanted information from the links stored in links list
for i in links:
    browser.get(i)
    # Sleep function is implemented if the website limits the number of opens
    time.sleep(10)
    get_them_all(x, 'Designer', 'MainAccords1', 'MainAccords2', 'MainAccords3', 'MainAccords4', 'MainAccords5'
                , 'dayornight', 'HaveRating', 'HadRating', 'WantRating', 'SignatureRating', 'PerfumeRating'
                , 'Number_Votes', 'LongevityPoor', 'LongevityWeak', 'LongevityModerate', 'LongevityLong'
                , 'LongevityVeryLong', 'SillageSoft', 'SillageModerate', 'SillageHeavy', 'SillageEnormous'
                , 'consumerMainNoteType1', 'consumerMainNoteType2'
                , 'consumerMainNoteType3', 'consumerMainNoteType4', 'consumerMainNoteType5'
                , 'consumerMainNoteType6', 'consumerMainNoteType7', 'consumerMainNoteType8'
                , 'consumerMainNoteType9','consumerMainNoteType10', 'consumerMainNoteType11'
                , 'consumerMainNoteType12', 'consumerMainNoteType13', 'consumerMainNoteType14'
                , 'consumerMainNoteType15', 'consumerMainNoteType16', 'consumerMainNoteType17'
                , 'consumerMainNoteType18', 'consumerMainNoteType19', 'consumerMainNoteType20')
    # To update the user on the script's progress
    x += 1
    print(x-1,'/', y)
    # Sleep function is implemented if the website limits the number of opens
    time.sleep(10)

# Printing the entire dataframe
print(df)

# Storing the dataframe into a csv file
# User may also select the intended format to be stored as
with open('XXXXXcsv_filenameX', 'a', encoding='utf-8') as f:
        df.to_csv(f)

# Close the browser used for scraping
browser.close()
