# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time


class TestCase1Seleniumide1(unittest.TestCase):
    def setUp(self):
        capabilities = webdriver.DesiredCapabilities().FIREFOX
        capabilities['marionette'] = False
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case1_seleniumide1(self):
        driver = self.driver
        driver.get(
            self.base_url + "/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=selenium&rsv_pq=bd63f9aa0006d2cd&rsv_t=2f68eYFbwBE7wRRl%2BB1VUVfwv2KKtuJFx4fi9qUwp%2F6X%2BEaLrbP1rJeH9Mk&rqlang=cn&rsv_enter=1&rsv_sug3=4&rsv_sug1=2&rsv_sug7=100")
        time.sleep(2)
        storedText = driver.find_element_by_link_text(u"selenium - 随笔分类 - 虫师 - 博客园").text
        print(storedText)
        self.assertEqual("Selenium", driver.find_element_by_css_selector("em").text)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
