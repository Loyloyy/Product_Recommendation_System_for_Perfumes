from bs4 import BeautifulSoup
import requests
import csv

#to specify which page we want to extract HTML from
source = requests.get('XXXwebsiteXXX').text
soup = BeautifulSoup(source, 'lxml')

#to specify which csv file we want to write to
csv_file = open('XXXplace to store CSV fileXXX', 'w')
csv_writer = csv.writer(csv_file)
#to create the row headers for the csv file
csv_writer.writerow(['headline', 'sumary', 'video_link'])

#1#print the entire page's HTML
#print(soup.prettify())

#2#finds first article of the page and prints it in HTML
# article = soup.find('article')

#3#print the entire first post on the main page in HTML
#print(article.prettify())

#4#printing the first post's title in text
# headline = article.h2.a.text
# print(headline)

#5#printing out the first post's summary in text <work in conjunction with article = soup.find('article')>     p stands for parse
# summary = article.find('div', class_='entry-content').p.text
# print(summary)

#6#prints the youtube LINK because it is using ['src']
# vid_src = article.find('iframe', class_='youtube-player')['src']
# print(vid_src)
#7#splits the youtube link into multiple parts to allow us to pick the specific part we want for storing/usage
# vid_id = vid_src.split('/')[4]
# vid_id = vid_src.split('?')[0]
# print(vid_id)
#8#combine everything to get full youtube link
# yt_link = f'https://youtube.com/watch?v={vid_id}'

#9#to print all the titles, summaries and youtube links (everything mentioned before this) of every single post on the main page
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    #double noted here for video cause this section is for assuming that all posts have video links, below will have another section whereby a post without video is taken into account
    ## vid_src = article.find('iframe', class_='youtube-player')['src']
    ## vid_id = vid_src.split('/')[4]
    ## vid_id = vid_src.split('?')[0]
    ## yt_link = f'https://youtube.com/watch?v={vid_id}'
    #print(yt_link)

    ##printing the youtube link factoring that some posts do not have video links. Hence the output of the link string will be 'None'
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_src.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print()

    #to specify which strings to fit into the csv file
    csv_writer.writerow([headline, summary, yt_link])

#close the csv file
csv_file.close()
