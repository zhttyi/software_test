
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(executable_path='D:\chrome dowload\chromedriver.exe')#声明浏览器
url = 'http://118.192.69.103:8069/web'
browser.get(url)#打开浏览器预设网址
print(browser.page_source)#打印网页源代码

