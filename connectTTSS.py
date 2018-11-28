import selenium as se
from selenium import webdriver
import datetime
import time
import editHTML


now = datetime.datetime.now()

def connect(my_url,liczbaPrzystankow,nazwa):

    options = se.webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options,executable_path=r"C:\webdrivers\chromedriver.exe")
    driver.get(my_url)
    time.sleep(1)
    b=1

    editHTML.createIndex()

    while (b<liczbaPrzystankow):
        
        numer_element = driver.find_element_by_xpath('//*[@id="isg2_prediction_table"]/tbody/tr['+str(b)+']/td[2]')
        przystanek_element = driver.find_element_by_xpath('//*[@id="isg2_prediction_table"]/tbody/tr['+str(b)+']/td[3]/div')
        czas_element = driver.find_element_by_xpath('//*[@id="isg2_prediction_table"]/tbody/tr['+str(b)+']/td[6]')
        b+=1
        editHTML.insertData(numer_element.text,przystanek_element.text,czas_element.text,str(b),nazwa)
    
    driver.quit()
