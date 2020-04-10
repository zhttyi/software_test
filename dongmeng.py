from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='D:\chrome dowload\chromedriver.exe')#声明浏览器
url = 'http://118.192.66.92:8080/clbs/login'
browser.get(url)#打开浏览器预设网址
print(browser.page_source)#打印网页源代码
# browser.close()#关闭浏览器
time.sleep(2)

browser.find_element_by_id('email').send_keys('fengjingshan')
browser.find_element_by_id('tg_password').send_keys('fengjingshan123')
browser.find_element_by_id('login_ok').click()