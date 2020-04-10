from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(executable_path='D:\chrome dowload\chromedriver.exe')#声明浏览器
url = 'http://118.192.69.103:8069/web/login'
browser.get(url)#打开浏览器预设网址
print(browser.page_source)#打印网页源代码
# browser.close()#关闭浏览器
browser.find_element_by_link_text('iECSUrban_kuajing').click()
time.sleep(2)
browser.find_element_by_name('login').send_keys('admin')
browser.find_element_by_name('password').send_keys('yatinova0827')
# browser.find_element_by_link_text('登录').click()
# browser.element.send_keys(Keys.ENTER)
browser.find_element_by_xpath("//button[@class='btn btn-primary']").click()
time.sleep(3)
browser.find_element_by_xpath("//nav[@id='oe_main_menu_navbar']//li[8]//a[1]//span[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//a[contains(text(),'(assets)')]").click()
time.sleep(6)
browser.find_element_by_xpath("//li[@class='o_debug_manager']//a[@class='dropdown-toggle']").click()
time.sleep(1)
browser.find_element_by_xpath("//a[contains(text(),'JS')]").click()
time.sleep(60)

browser.find_element_by_xpath("//html").text
# browser.find_element_by_xpath("").click()