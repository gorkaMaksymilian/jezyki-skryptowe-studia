import selenium as se
from selenium import webdriver
import datetime
import time
import editHTML
import default
import logging
logger=logging.getLogger(__name__)
logger.setLevel(default.DEFAULT_LOG["level"])
formatter=logging.Formatter(""+default.DEFAULT_LOG["formatter"]+"")
file_handler = logging.FileHandler(""+default.DEFAULT_LOG["file"]+"")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

now = datetime.datetime.now()



def connect(my_url,liczbaPrzystankow,nazwa):

    options = se.webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options,executable_path=default.DEFAULT_CONNECT_TTSS["root"])
    driver.get(my_url)
    time.sleep(1)
    b=1

    editHTML.createIndex()

    while (b<liczbaPrzystankow):
        
        numer_element = driver.find_element_by_xpath(default.DEFAULT_CONNECT_TTSS["xPathFirst"]+str(b)+default.DEFAULT_CONNECT_TTSS["xPathSecond"])
        przystanek_element = driver.find_element_by_xpath(default.DEFAULT_CONNECT_TTSS["xPathFirst"]+str(b)+default.DEFAULT_CONNECT_TTSS["xPathThird"])
        czas_element = driver.find_element_by_xpath(default.DEFAULT_CONNECT_TTSS["xPathFirst"]+str(b)+default.DEFAULT_CONNECT_TTSS["xPathFourth"])
        b+=1
        editHTML.insertData(numer_element.text,przystanek_element.text,czas_element.text,str(b),nazwa)
    
    driver.quit()
