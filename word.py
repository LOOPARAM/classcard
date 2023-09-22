#데이터 분석을 하기위한 라이브러리
import pandas as pd

#웹 크롤링을 할 수 있는 라이브러리
from bs4 import BeautifulSoup

#마찬가지로 웹 크롤링을 도와주는 라이브러리
from urllib.request import Request,urlopen

#Sleep함수를 위함
import time

#웹 크롤링하는거
import requests

#직접 버튼을 누르고 페이지에서 동작을 가능하게 해주는 라이브러리
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('D:\#1 Coding\[10] Python\word\prismatic-fact-399718-d5ea42ecf7a4.json',scope)

gc = gspread.authorize(credentials)

doc = gc.open_by_url('https://docs.google.com/spreadsheets/d/1_NBbaVZm3gtiPDMHZJe9LrmsqJ_g9ViZ1U1qW2i-2os/edit?usp=sharing')

worksheet = doc.worksheet('시트1')

cell_data = worksheet.acell('C1').value

print(cell_data)

url = 'https://www.classcard.net/set/11714765/938157'


browser = webdriver.Chrome()

browser.maximize_window()

action = ActionChains(browser)

browser.get(url)

login = browser.find_element(By.CLASS_NAME,'m-r-25.anchor-underline')

login.send_keys(Keys.ENTER)

id = browser.find_element(By.CLASS_NAME,'form-control.input-lg.font-15')

id.send_keys('sslgh1024')

password = browser.find_element(By.CLASS_NAME,'form-control.input-lg.m-t-12.font-15')

password.send_keys('gg1024!!')

login_btn = browser.find_element(By.CLASS_NAME, 'btn.btn-block.btn-lg.btn-success.shadow.m-t-lg.font-15')

login_btn.send_keys(Keys.ENTER)

browser.implicitly_wait(100)

star = False


for t in range(0,25):
    word_a = browser.find_element(By.XPATH,f'/html/body/div[1]/div[2]/div/div/div[2]/div[3]/div/div[{28-t}]/div[2]/div/a')
    word_a.click()

    if star == False:
        all = browser.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[3]/div[2]/div/a')
        print('hi')
        all.click()
        
        
        all_ = browser.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[3]/div[2]/div/ul/li[1]/a')
        all_.click()
        

    browser.implicitly_wait(100)

    mean = browser.find_element(By.CLASS_NAME,'is_show_back')

    mean.click()

    browser.implicitly_wait(1000)
    browser.execute_script("window.scrollTo(0,50000);")

    
    webpage = browser.page_source

    wp = '//*[@id="tab_set_section"]/div[1]/div[2]/div/div'
    wp_ = '//*[@id="tab_set_favor"]/div/div[2]/div/div'

    w = browser.find_elements(By.XPATH, wp_ if star == True else wp)

    english = []
    ko = []

    print(len(w))
    for i in range(0,40):
        
        xp = f'//*[@id="tab_set_all"]/div[2]/div[{1+i}]/div[4]/div[1]/div[1]/div/div'
        xp_ = f'//*[@id="tab_set_favor"]/div/div[2]/div/div[{1+i}]/div[4]/div[1]/div[1]/div/div'


        webpage_str = browser.find_element(By.XPATH, xp_ if star == True else xp)
        print(webpage_str.text)  
        english.append(webpage_str.text)

    for i in range(0,40):
        
        xp2 = f'//*[@id="tab_set_all"]/div[2]/div[{1+i}]/div[4]/div[2]/div[1]/div/div'
        xp2_ = f'//*[@id="tab_set_favor"]/div/div[2]/div/div[{1+i}]/div[4]/div[2]/div[1]/div/div'

        webpage_str = browser.find_element(By.XPATH, xp2_ if star == True else xp2)
        print(webpage_str.text)  
        ko.append(webpage_str.text)

    data = {f'{t+1}과 영어':english, f'{t+1}과 뜻':ko}

    if (t!=0):
        df1 = df

    df = pd.DataFrame(data)

    if(t!=0):
        df = pd.concat([df1, df], axis=1)
        


    browser.back()

    if(t==24):
        print(df)
        df.to_csv('Word_5.csv')

