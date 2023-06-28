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

class TestSuscoSquareStationsTH():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_suscoSquareStationsTH(self):
    # Test name: Susco Square Stations TH
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
    # 6 | click | linkText=ผลิตภัณฑ์และบริการ |  | 
    self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ").click()
    # 7 | mouseOver | linkText=ผลิตภัณฑ์และบริการ |  | 
    element = self.driver.find_element(By.LINK_TEXT, "ผลิตภัณฑ์และบริการ")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | linkText=SUSCO SQUARE |  | 
    self.driver.find_element(By.LINK_TEXT, "SUSCO SQUARE").click()
    # 9 | click | id=slideout_tab |  | 
    self.driver.find_element(By.ID, "slideout_tab").click()
    # 10 | click | linkText=ยอมรับ |  | 
    self.driver.find_element(By.LINK_TEXT, "ยอมรับ").click()
    # 11 | click | linkText=กรุงเทพฯ และปริมณฑล |  | 
    self.driver.find_element(By.LINK_TEXT, "กรุงเทพฯ และปริมณฑล").click()
    # 12 | click | linkText=ภาคเหนือ |  | 
    self.driver.find_element(By.LINK_TEXT, "ภาคเหนือ").click()
    # 13 | click | linkText=ภาคใต้ |  | 
    self.driver.find_element(By.LINK_TEXT, "ภาคใต้").click()
    # 14 | click | linkText=ภาคกลาง |  | 
    self.driver.find_element(By.LINK_TEXT, "ภาคกลาง").click()
    # 15 | click | linkText=ภาคอีสาน |  | 
    self.driver.find_element(By.LINK_TEXT, "ภาคอีสาน").click()
    # 16 | click | linkText=ภาคตะวันออก |  | 
    self.driver.find_element(By.LINK_TEXT, "ภาคตะวันออก").click()
    # 17 | click | linkText=ภาคตะวันตก |  | 
    self.driver.find_element(By.LINK_TEXT, "ภาคตะวันตก").click()
    # 18 | click | linkText=ทั้งหมด |  | 
    self.driver.find_element(By.LINK_TEXT, "ทั้งหมด").click()
  