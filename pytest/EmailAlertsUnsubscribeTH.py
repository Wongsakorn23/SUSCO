# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEmailAlertsUnsubscribeTH():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_emailAlertsUnsubscribeTH(self):
    # Test name: Email Alerts Unsubscribe TH
    # Step # | name | target | value | comment
    # 1 | open | https://demo.irplus.in.th/Listed/susco/email_alerts_unsubscribe.asp |  | 
    self.driver.get("https://demo.irplus.in.th/Listed/susco/email_alerts_unsubscribe.asp")
    # 2 | setWindowSize | 1936x1056 |  | 
    self.driver.set_window_size(1936, 1056)
    # 3 | click | linkText=TH |  | 
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    # 4 | click | id=email |  | 
    self.driver.find_element(By.ID, "email").click()
    # 5 | type | id=email | Test@tt.tt | 
    self.driver.find_element(By.ID, "email").send_keys("Test@tt.tt")
    # 6 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 7 | click | css=.rc-anchor-checkbox-holder |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".rc-anchor-checkbox-holder").click()
    # 8 | selectFrame | relative=parent |  | 
    self.driver.switch_to.default_content()
    # 9 | click | css=.btn__title |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn__title").click()
    # 10 | mouseOver | css=.btn__title |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn__title")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOut | css=.btn__title |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
