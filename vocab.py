from selenium import webdriver as wbd
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

from vocab_input import word_func

def extractsynonyms(text):
    text = text.replace('synonyms:','')
    texts = text.split(',')
    texts = texts[0:5]
    finalString =''
    for i in  texts:
        finalString+= i+","
    finalString = finalString[:-1]
    return finalString


word = word_func()
word=word.title()
url= 'https://www.google.com/search?q='+word+'&rlz=1C1CHBF_enIN797IN797&oq=alterc&aqs=chrome.1.69i57j0l7.2230j0j15&sourceid=chrome&ie=UTF-8'
url2 = 'https://www.merriam-webster.com/dictionary/'+word.lower()


book_location = 'D:\\OneDrive\\GRE\\Vocab.xlsx'
cols = ['Word','Meaning','Synonyms','Sentence']

word_check = pd.read_excel(book_location,usecols=cols)

word_list = word_check['Word'].values.tolist()



if word not in word_list:
    res = requests.get(url)
    source = res.content
    soup = BeautifulSoup(source,'lxml')


    des =  soup.findAll("div", {"class": "v9i61e"})

    oneRecord = []
    meaning =''
    sentence =''

    synonyms=''


    c=0
    for i in des:
        if c%2==0:
            meaning+=(i.findChild().text +";\n\n")
        else:
            sentence+=(i.findChild().text+";\n\n")

        c=c+1



    syns = soup.body.findAll(text=re.compile('synonyms:'))

    for i in syns:
        synonyms+=(extractsynonyms(i)+";\n\n")

    meaning=meaning[:-3]
    synonyms=synonyms[:-3]
    sentence=sentence[:-3]


    oneRecord.extend([[word,meaning,synonyms,sentence]])

    df_original = pd.read_excel(book_location,usecols=cols)

    df = pd.DataFrame(oneRecord,columns=cols)

    df_original = df_original.append(df,ignore_index=True)

    print(df_original)
    df_original.to_excel(book_location,index=False)
else:
    print("Already there")
