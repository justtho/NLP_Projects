import pandas as pd
import numpy as np
import os
import bs4 as BeautifulSoup
import urllib.request
import requests
import sys

def get_url():
    df = pd.read_csv(r'C:\Sharpest_Minds\gdelt_project\nlp_project\notebooks\data_files\sourceurl.csv')
    urls = df['sourceurl'].unique()
    return urls

def extract_data():
    urls = get_url()
    for i,url in enumerate(urls):
        fetch_data= requests.get(url)

    #     article_read = fetch_data.read()

        article_parsed = BeautifulSoup.BeautifulSoup(fetch_data.text,'html.parser')

        #Return Header tags

        headers_text = article_parsed.find('h1')
        headers = headers_text.text if headers_text else 'N/A'
        paragraphs = article_parsed.find_all('p')

        article_content = ''

        for p in paragraphs:
            article_content +=p.text

        print(headers)
        print(article_content)


        file = open("C:/Sharpest_Minds/webfile/site{}.txt".format(i), 'wb')
        file.write(headers.encode('utf8'))
        file.write('\n'.encode('utf8'))
        file.write(article_content.encode())
        file.close()

        get_url()
        extract_data()
