from selenium import webdriver

broswer = webdriver.Firefox()
broswer.get("http://www.baidu.com")
broswer.find_element_by_id("kw").send_keys("selenium")
broswer.find_element_by_id("su").click()
broswer.close()
