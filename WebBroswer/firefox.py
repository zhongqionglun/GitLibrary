# -*- coding: utf-8 -*-
from selenium import webdriver
import time

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities['marionette'] = False
broswer = webdriver.Firefox()
broswer.get("http://www.baidu.com")
broswer.find_element_by_link_text(u'新闻').click()
time.sleep(5)
broswer.back()
time.sleep(2)
broswer.find_element_by_id("kw").send_keys("selenium")
broswer.find_element_by_id("su").click()
time.sleep(2)
broswer.close()
