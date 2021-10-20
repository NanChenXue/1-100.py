from selenium import webdriver
import time
driver=webdriver.Chrome();
driver.get("https://www.ctrip.com/")
driver.find_element_by_xpath('//*[@id="nav-bar-set-login"]/a/span').click()
driver.find_element_by_id("nloginname").send_keys("13965408036")#用户名
driver.find_element_by_id("npwd").send_keys("cdlbj0328")#密码
#验证码
driver.find_element_by_id("nsubmit").click();
