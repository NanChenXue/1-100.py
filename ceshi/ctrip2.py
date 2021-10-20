from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome();
driver.get("https://www.ctrip.com/")
driver.find_element_by_id("HD_CityName").send_keys("上海")#目的地
driver.find_element_by_id("HD_CheckIn").clear()
driver.find_element_by_id("HD_CheckIn").send_keys("2021-07-04")#入住日期
driver.find_element_by_id("HD_CheckOut").clear()
driver.find_element_by_id("HD_CheckOut").send_keys("2021-07-06")#退房日期

# a=driver.find_element_by_id("J_roomCountList")
# Select(a).select_by_value("2间")#房间数
driver.find_element_by_xpath('//*[@id="J_roomCountList"]/option[2]').click()
# b=driver.find_element_by_id("searchHotelLevelSelect")
# Select(b).select_by_value("三星级/舒适")#酒店级别
driver.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]/option[4]').click()
driver.find_element_by_xpath('//*[@id="HD_Btn"]').click()#搜索
