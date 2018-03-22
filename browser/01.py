'''
#@Author: Grizlly 
# @Date: 2018-03-17 19:58:37 
# -*- coding: utf-8 -*- 
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# browser = webdriver.PhantomJS()
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# browser = webdriver.Chrome(chrome_options=option)

chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

# chrome_options.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
# browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://www.baidu.com'

browser.get(url)

browser.implicitly_wait(3)

text = browser.find_element_by_id('kw')

text.clear()

button = browser.find_element_by_id('su')

button.submit()

print(browser.title)

browser.save_screenshot('text.png')

results = browser.find_element_by_class_name('t')

for result in results:
    print('title:{} url:{}'.format(result.text,
    result.find_element_by_class_name('a').get_attribute('href')))