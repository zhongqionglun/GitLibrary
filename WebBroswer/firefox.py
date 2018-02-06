# -*- coding: utf-8 -*-

from selenium import webdriver

capabilities = webdriver.DesiredCapabilities().FIREFOX
capabilities["marionette"] = False
fbroswer = webdriver.Firefox(capabilities=capabilities)
fbroswer.get("https://www.baidu.com")
fbroswer.find_element_by_id("kw").send_keys("selenium")
fbroswer.find_element_by_id("su").click()
fbroswer.close()
