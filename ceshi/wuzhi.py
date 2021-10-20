from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.whit.edu.cn/");
driver.find_element_by_xpath('//*[@id="heaer"]/div[1]/div/ul/li[2]/a').click()
all=driver.window_handles
print("所有页签handle %s" % all)
now_page = driver.current_window_handle

print("当前页签handle %s" %now_page)
driver.find_element_by_name("username").send_keys("1914040201")
driver.find_element_by_id("password").send_keys("281724")
driver.find_element_by_class_name("auth_login_btn primary full_width").click()


title_first_page = driver.title
print("切换前title %s" % title_first_page)

