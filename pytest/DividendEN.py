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

class TestDividendEN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dividendEN(self):
    # Test name: Dividend EN
    # Step # | name | target | value | comment
    # 1 | open | https://demo.irplus.in.th/Listed/susco/homepage.asp |  | 
    self.driver.get("https://demo.irplus.in.th/Listed/susco/homepage.asp")
    # 2 | setWindowSize | 1936x1056 |  | 
    self.driver.set_window_size(1936, 1056)
    # 3 | click | css=.fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    # 4 | click | linkText=EN |  | 
    self.driver.find_element(By.LINK_TEXT, "EN").click()
    # 5 | click | css=.fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    # 6 | click | linkText=INVESTOR RELATIONS |  | 
    self.driver.find_element(By.LINK_TEXT, "INVESTOR RELATIONS").click()
    # 7 | mouseOver | css=li:nth-child(4) > .dropdown-toggle |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .dropdown-toggle")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=li:nth-child(4) li:nth-child(4) > .dropdown-item |  | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(4) > .dropdown-item").click()
  
