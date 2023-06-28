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

class TestChairmanTH():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_chairmanTH(self):
    # Test name: Chairman TH
    # Step # | name | target | value | comment
    # 1 | open | https://demo.irplus.in.th/Listed/susco/homepage.asp |  | 
    self.driver.get("https://demo.irplus.in.th/Listed/susco/homepage.asp")
    # 2 | setWindowSize | 1936x1056 |  | 
    self.driver.set_window_size(1936, 1056)
    # 3 | click | css=.fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    # 4 | click | linkText=TH |  | 
    self.driver.find_element(By.LINK_TEXT, "TH").click()
    # 5 | click | css=.fa |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa").click()
    # 6 | click | id=navbarDropdown |  | 
    self.driver.find_element(By.ID, "navbarDropdown").click()
    # 7 | click | linkText=สารจากประธานกรรมการ |  | 
    self.driver.find_element(By.LINK_TEXT, "สารจากประธานกรรมการ").click()
    # 8 | click | id=slideout_tab |  | 
    self.driver.find_element(By.ID, "slideout_tab").click()
  
