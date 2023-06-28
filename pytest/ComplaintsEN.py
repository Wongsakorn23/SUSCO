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

class TestComplaintsEN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_complaintsEN(self):
    # Test name: Complaints EN
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
    # 7 | mouseOver | css=li:nth-child(9) > .dropdown-item |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=li:nth-child(9) li:nth-child(4) > .dropdown-item |  | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) li:nth-child(4) > .dropdown-item").click()
    # 9 | click | id=complaints_type |  | 
    self.driver.find_element(By.ID, "complaints_type").click()
    # 10 | select | id=complaints_type | label=Other complaints. | 
    dropdown = self.driver.find_element(By.ID, "complaints_type")
    dropdown.find_element(By.XPATH, "//option[. = 'Other complaints.']").click()
    # 11 | click | id=detail |  | 
    self.driver.find_element(By.ID, "detail").click()
    # 12 | type | id=detail | Test EN | 
    self.driver.find_element(By.ID, "detail").send_keys("Test EN")
    # 13 | click | id=full_name |  | 
    self.driver.find_element(By.ID, "full_name").click()
    # 14 | click | css=.row:nth-child(5) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5)").click()
    # 15 | type | id=full_name | Test EN | 
    self.driver.find_element(By.ID, "full_name").send_keys("Test EN")
    # 16 | click | id=email |  | 
    self.driver.find_element(By.ID, "email").click()
    # 17 | click | css=.row:nth-child(6) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(6)").click()
    # 18 | click | css=.row:nth-child(6) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(6)").click()
    # 19 | type | id=email | Test@tt.tt | 
    self.driver.find_element(By.ID, "email").send_keys("Test@tt.tt")
    # 20 | click | id=phone |  | 
    self.driver.find_element(By.ID, "phone").click()
    # 21 | type | id=phone | 0000000000 | 
    self.driver.find_element(By.ID, "phone").send_keys("0000000000")
    # 22 | click | id=contact_other |  | 
    self.driver.find_element(By.ID, "contact_other").click()
    # 23 | type | id=contact_other | Test EN | 
    self.driver.find_element(By.ID, "contact_other").send_keys("Test EN")
    # 24 | click | id=chkboxconsent |  | 
    self.driver.find_element(By.ID, "chkboxconsent").click()
    # 25 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 26 | click | css=.recaptcha-checkbox-border |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    # 27 | selectFrame | relative=parent |  | 
    self.driver.switch_to.default_content()
    # 28 | click | id=subscribe |  | 
    self.driver.find_element(By.ID, "subscribe").click()
  