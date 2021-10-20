from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://nj.zu.anjuke.com/") #打开网页

a=driver.find_element_by_class_name("select_icon");
ActionChains(driver).move_to_element(a).perform();
time.sleep(3)
driver.find_element_by_xpath('//*[@id="city-panel"]/dl[2]/dd/a[4]').click() #南京
driver.find_element_by_xpath('//*[@id="city_list"]/dl[2]/dd/a[4]').click()#地铁找房
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/span[2]/div/a[3]').click()#2号线
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/span[2]/div/div/a[20]').click()#马群

driver.find_element_by_id("from-price").send_keys('5000')
driver.find_element_by_id("to-price").send_keys('8000')
driver.find_element_by_class_name("smit").click()

driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[4]/span[2]/a[2]').click()#整租
driver.find_element_by_xpath('//*[@id="condmenu"]/ul/li[2]/ul/li[2]/a').click()#普通住宅

driver.find_element_by_id("search-rent").send_keys('经天路')
driver.find_element_by_id("search-button").click()

driver.find_element_by_xpath('//*[@id="list-content"]/div[1]/a[2]').click()#视频看房
driver.find_element_by_xpath('//*[@id="list-content"]/div[2]/div/a[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="list-content"]/div[2]/div/a[3]').click()
driver.find_element_by_xpath('//*[@id="list-content"]/div[3]').click()
driver.quit()
