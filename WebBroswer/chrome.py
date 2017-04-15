from selenium import webdriver

webdriver.
broswer = webdriver.Chrome()
broswer.get('http://www.baidu.com')
broswer.find_element_by_id('kw').send_keys('webdriver')
broswer.find_element_by_id('su').click()
broswer.close()
