from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import pandas as pd

i = 1

# Creating the dataframe to store the relevant data while scraping
df = pd.DataFrame(columns=['Name', 'Year', 'Sex', 'Number_comments', 'Designer', 'MainAccords1', 'MainAccords2'
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

#--| Setup
options = Options()
#options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)
#--| Parse or automation
browser.get(XXXXXXXX) # where XXXXXXXX is the link you will of the designer (not the parent company!)


# define the function to help scrape the wanted information for each perfume page
def getthemall(i, designer1, accord1, accord2, accord3, accord4, accord5, daynight6, have7, had8, want9
                , signature10, rating11, no_vote12, longpoor13, longweak14, longmod15, longlong16
                , longverylong17, sillagesoft18, sillagemod19, sillageheavy20, sillageenormous21, user22
                , user23, user24, user25, user26, user27, user28, user29, user30, user31, user32, user33
                , user34, user35, user36, user37, user38, user39, user40, user41):

    # Scraping the name of the designer
    designer = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/p/span[1]/span/a/span')
    df.loc[i, designer1] = designer[0].text

    # Scraping the first main note of the perfume, if the website does not list it, return NA
    try:
        main1 = browser.find_elements_by_xpath('//*[@id="prettyPhotoGallery"]/div[1]/div[2]/span')
        df.loc[i, accord1] = main1[0].text
    except Exception as e:
        df.loc[i, accord1] = 'NA'

    # Scraping the second main note of the perfume, if the website does not list it, return NA
    try:
        main2 = browser.find_elements_by_xpath('//*[@id="prettyPhotoGallery"]/div[1]/div[4]/span')
        df.loc[i, accord2] = main2[0].text
    except Exception as e:
        df.loc[i, accord2] = 'NA'

    # Scraping the third main note of the perfume, if the website does not list it, return NA
    try:
        main3 = browser.find_elements_by_xpath('//*[@id="prettyPhotoGallery"]/div[1]/div[6]/span')
        df.loc[i, accord3] = main3[0].text
    except Exception as e:
        df.loc[i, accord3] = 'NA'

    # Scraping the forth main note of the perfume, if the website does not list it, return NA
    try:
        main4 = browser.find_elements_by_xpath('//*[@id="prettyPhotoGallery"]/div[1]/div[8]/span')
        df.loc[i, accord4] = main4[0].text
    except Exception as e:
        df.loc[i, accord4] = 'NA'

    # Scraping the fifth main note of the perfume, if the website does not list it, return NA
    try:
        main5 = browser.find_elements_by_xpath('//*[@id="prettyPhotoGallery"]/div[1]/div[10]/span')
        df.loc[i, accord5] = main5[0].text
    except Exception as e:
        df.loc[i, accord5] = 'NA'

    # Checking how many people voted the perfume as a day or a night perfume
    day = browser.find_elements_by_xpath('//*[@id="clsdayD"][@style]')
    day = day[0].get_attribute("style").split(';')[1].split(';')[0].split(':')[1].split('p')[0]
    night = browser.find_elements_by_xpath('//*[@id="clsnightD"][@style]')
    night = night[0].get_attribute("style").split(';')[1].split(';')[0].split(':')[1].split('p')[0]

    # if more people voted day, it will be labelled as such and vice versa, or else NA will be returned
    if int(day) > int(night):
        df.loc[i, daynight6] = 'Daytime scent'
    elif int(day) < int(night):
        df.loc[i, daynight6] = 'Nighttime scent'
    else:
        df.loc[i, daynight6] = 'NA'

    # Scraping the line where users vote if they have it/had it/want it/have is as their signature perfume
    have = browser.find_elements_by_xpath('//*[@id="mainpicbox"]/p/span')

    # Separating the line and extracting the number of people who have it, if nothing, NA is returned
    try:
        df.loc[i, have7] = have[0].text.split('I have it')[1].split('I')[0].split(':')[1].strip(' ')
    except Exception as e:
        df.loc[i, have7] = 'NA'

    # Separating the line and extracting the number of people who had it, if nothing, NA is returned
    try:
        had = have#browser.find_elements_by_xpath('//*[@id="mainpicbox"]/p/span"')
        df.loc[i, had8] = had[0].text.split('I had it:')[1].split('I')[0].strip(' ')
    except Exception as e:
        df.loc[i, had8] = 'NA'

    # Separating the line and extracting the number of people who want it, if nothing, NA is returned
    try:
        want = have#browser.find_elements_by_xpath('//*[@id="mainpicbox"]/p/span"')
        df.loc[i, want9] = want[0].text.split('I want it:')[1].split('M')[0].strip(' ')
    except Exception as e:
        df.loc[i, want9] = 'NA'

    # Separating the line and extracting the number of people who have it as their signature, if nothing, NA is returned
    try:
        signature = have#browser.find_elements_by_xpath('//*[@id="mainpicbox"]/p/span"')
        df.loc[i, signature10] = signature[0].text.split('My signature:')[1].strip(' ')
    except Exception as e:
        df.loc[i, signature10] = 'NA'


    # Scraping the rating of the perfume, based on the users, if nothing, NA is returned
    try:
        rating = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[6]/p/span[1]')
        df.loc[i, rating11] = rating[0].text
    except Exception as e:
        df.loc[i, rating11] = 'NA'

    # Scraping the number of people who vated, if nobody, NA is returned
    try:
        numberofvotes = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[6]/p/span[3]')
        df.loc[i, no_vote12] = numberofvotes[0].text
    except Exception as e:
        df.loc[i, no_vote12] = 'NA'

    # Scraping the users' opinion of the perfume's longetivity
    # Scraping the number of users who think the longetivity is poor, if nobody, NA is returned
    try:
        longpoor = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[1]/div/table/tbody/tr[1]/td[2]')
        df.loc[i, longpoor13] = longpoor[0].text
    except Exception as e:
        df.loc[i, longpoor13] = 'NA'

    # Scraping the number of users who think the longetivity is weak (stronger than poor), if nobody, NA is returned
    try:
        longweak = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[1]/div/table/tbody/tr[2]/td[2]')
        df.loc[i, longweak14] = longweak[0].text
    except Exception as e:
        df.loc[i, longweak14] = 'NA'

    # Scraping the number of users who think the longetivity is moderate, if nobody, NA is returned
    try:
        longmoderate = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[1]/div/table/tbody/tr[3]/td[2]')
        df.loc[i, longmod15] = longmoderate[0].text
    except Exception as e:
        df.loc[i, longmod15] = 'NA'

    # Scraping the number of users who think the longetivity is long, if nobody, NA is returned
    try:
        longlong = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[1]/div/table/tbody/tr[4]/td[2]')
        df.loc[i, longlong16] = longlong[0].text
    except Exception as e:
        df.loc[i, longlong16] = 'NA'

    # Scraping the number of users who think the longetivity is very long, if nobody, NA is returned
    try:
        longverylong = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[1]/div/table/tbody/tr[5]/td[2]')
        df.loc[i, longverylong17] = longverylong[0].text
    except Exception as e:
        df.loc[i, longverylong17] = 'NA'

    # Scraping the users' opinion of the perfume's sillage
    # Scraping the number of users who think the sillage is soft (lowest), if nobody, NA is returned
    try:
        sillagesoft = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[2]/table/tbody/tr/td/table/tbody/tr[1]/td[2]')
        df.loc[i, sillagesoft18] = sillagesoft[0].text
    except Exception as e:
        df.loc[i, sillagesoft18] = 'NA'

    # Scraping the number of users who think the sillage is moderate, if nobody, NA is returned
    try:
        sillagemod = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[2]/table/tbody/tr/td/table/tbody/tr[2]/td[2]')
        df.loc[i, sillagemod19] = sillagemod[0].text
    except Exception as e:
        df.loc[i, sillagemod19] = 'NA'

    # Scraping the number of users who think the sillage is heavy, if nobody, NA is returned
    try:
        sillageheavy = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[2]/table/tbody/tr/td/table/tbody/tr[3]/td[2]')
        df.loc[i, sillageheavy20] = sillageheavy[0].text
    except Exception as e:
        df.loc[i, sillageheavy20] = 'NA'

    # Scraping the number of users who think the sillage is enormous, if nobody, NA is returned
    try:
        sillageenormous = browser.find_elements_by_xpath('//*[@id="col1"]/div/div/div[8]/div[2]/table/tbody/tr/td/table/tbody/tr[4]/td[2]')
        df.loc[i, sillageenormous21] = sillageenormous[0].text
    except Exception as e:
        df.loc[i, sillageenormous21] = 'NA'


    # Scraping the users' opinions on the perfumes' notes
    # Scaping the first users' opnions on notes, if nothing, NA is returned
    try:
        usernotes1 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[1]/img')
        df.loc[i, user22] = usernotes1[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user22] = 'NA'

    # Scaping the second users' opnions on notes, if nothing, NA is returned
    try:
        usernotes2 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[2]/img')
        df.loc[i, user23] = usernotes2[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user23] = 'NA'

    # Scaping the third users' opnions on notes, if nothing, NA is returned
    try:
        usernotes3 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[3]/img')
        df.loc[i, user24] = usernotes3[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user24] = 'NA'

    # Scaping the forth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes4 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[4]/img')
        df.loc[i, user25] = usernotes4[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user25] = 'NA'

    # Scaping the fifth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes5 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[5]/img')
        df.loc[i, user26] = usernotes5[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user26] = 'NA'

    # Scaping the sixth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes6 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[6]/img')
        df.loc[i, user27] = usernotes6[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user27] = 'NA'

    # Scaping the seventh users' opnions on notes, if nothing, NA is returned
    try:
        usernotes7 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[7]/img')
        df.loc[i, user28] = usernotes7[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user28] = 'NA'

    # Scaping the eigth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes8 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[8]/img')
        df.loc[i, user29] = usernotes8[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user29] = 'NA'

    # Scaping the ninth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes9 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[9]/img')
        df.loc[i, user30] = usernotes9[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user30] = 'NA'

    # Scaping the tenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes10 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[10]/img')
        df.loc[i, user31] = usernotes10[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user31] = 'NA'

    # Scaping the eleventh users' opnions on notes, if nothing, NA is returned
    try:
        usernotes11 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[11]/img')
        df.loc[i, user32] = usernotes11[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user32] = 'NA'

    # Scaping the twelfth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes12 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[12]/img')
        df.loc[i, user33] = usernotes12[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user33] = 'NA'

    # Scaping the thirteenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes13 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[13]/img')
        df.loc[i, user34] = usernotes13[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user34] = 'NA'

    # Scaping the fourteenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes14 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[14]/img')
        df.loc[i, user35] = usernotes14[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user35] = 'NA'

    # Scaping the fifteenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes15 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[15]/img')
        df.loc[i, user36] = usernotes15[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user36] = 'NA'

    # Scaping the sixteenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes16 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[16]/img')
        df.loc[i, user37] = usernotes16[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user37] = 'NA'

    # Scaping the seventeenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes17 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[17]/img')
        df.loc[i, user38] = usernotes17[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user38] = 'NA'

    # Scaping the eighteenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes18 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[18]/img')
        df.loc[i, user39] = usernotes18[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user39] = 'NA'

    # Scaping the nineteenth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes19 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[19]/img')
        df.loc[i, user40] = usernotes19[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user40] = 'NA'

    # Scaping the twentieth users' opnions on notes, if nothing, NA is returned
    try:
        usernotes20 = browser.find_elements_by_xpath('//*[@id="userMainNotes"]/div[20]/img')
        df.loc[i, user41] = usernotes20[0].get_attribute("title")
    except Exception as e:
        df.loc[i, user41] = 'NA'
