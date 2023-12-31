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

class TestRequestInquiryEN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_requestInquiryEN(self):
    # Test name: Request Inquiry EN
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
    # 8 | click | css=li:nth-child(9) li:nth-child(2) > .dropdown-item |  | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(9) li:nth-child(2) > .dropdown-item").click()
    # 9 | click | id=full_name |  | 
    self.driver.find_element(By.ID, "full_name").click()
    # 10 | click | css=.banner-sub-ir-2 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".banner-sub-ir-2").click()
    # 11 | type | id=full_name | Test EN | 
    self.driver.find_element(By.ID, "full_name").send_keys("Test EN")
    # 12 | click | id=phone |  | 
    self.driver.find_element(By.ID, "phone").click()
    # 13 | type | id=phone | 0000000000 | 
    self.driver.find_element(By.ID, "phone").send_keys("0000000000")
    # 14 | click | id=email |  | 
    self.driver.find_element(By.ID, "email").click()
    # 15 | type | id=email | Test@tt.tt | 
    self.driver.find_element(By.ID, "email").send_keys("Test@tt.tt")
    # 16 | click | id=detail |  | 
    self.driver.find_element(By.ID, "detail").click()
    # 17 | type | id=detail | Test EN | 
    self.driver.find_element(By.ID, "detail").send_keys("Test EN")
    # 18 | click | id=chkboxconsent |  | 
    self.driver.find_element(By.ID, "chkboxconsent").click()
    # 19 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 20 | click | css=.recaptcha-checkbox-border |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
    # 21 | selectFrame | relative=parent |  | 
    self.driver.switch_to.default_content()
    # 22 | selectFrame | index=2 |  | 
    self.driver.switch_to.frame(2)
    # 23 | click | css=tr:nth-child(3) > .rc-imageselect-tile:nth-child(1) .rc-image-tile-33 |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .rc-imageselect-tile:nth-child(1) .rc-image-tile-33").click()
    # 24 | click | css=tr:nth-child(3) > .rc-imageselect-tile:nth-child(3) .rc-image-tile-33 |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > .rc-imageselect-tile:nth-child(3) .rc-image-tile-33").click()
    # 25 | click | css=tr:nth-child(2) > .rc-imageselect-tile:nth-child(2) .rc-image-tile-33 |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .rc-imageselect-tile:nth-child(2) .rc-image-tile-33").click()
    # 26 | click | css=tr:nth-child(2) > .rc-imageselect-tile:nth-child(3) .rc-image-tile-33 |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > .rc-imageselect-tile:nth-child(3) .rc-image-tile-33").click()
    # 27 | click | id=recaptcha-verify-button |  | 
    self.driver.find_element(By.ID, "recaptcha-verify-button").click()
    # 28 | selectFrame | relative=parent |  | 
    self.driver.switch_to.default_content()
    # 29 | click | id=subscribe |  | 
    self.driver.find_element(By.ID, "subscribe").click()
  
