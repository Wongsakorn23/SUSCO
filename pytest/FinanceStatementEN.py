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

class TestFinanceStatementEN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_financeStatementEN(self):
    # Test name: Finance Statement EN
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
    # 7 | mouseOver | css=.dropdown-menu-right > li:nth-child(2) > .dropdown-item |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu-right > li:nth-child(2) > .dropdown-item")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=li:nth-child(2) li:nth-child(1) > .dropdown-item |  | 
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) li:nth-child(1) > .dropdown-item").click()
    # 9 | click | id=slideout-bt |  | 
    self.driver.find_element(By.ID, "slideout-bt").click()
    # 10 | click | linkText=ยอมรับ |  | 
    self.driver.find_element(By.LINK_TEXT, "ยอมรับ").click()
    # 11 | click | css=#type_fin_income > .text-menu-finance |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#type_fin_income > .text-menu-finance").click()
    # 12 | click | css=#type_fin_cash > .text-menu-finance |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#type_fin_cash > .text-menu-finance").click()
    # 13 | click | css=#type_fin_balance > .text-menu-finance |  | 
    self.driver.find_element(By.CSS_SELECTOR, "#type_fin_balance > .text-menu-finance").click()
    # 14 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 15 | click | linkText=2023 |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 16 | storeWindowHandle | root |  | 
    self.driver.find_element(By.LINK_TEXT, "2023").click()
    # 17 | selectWindow | handle=${win8121} |  | 
    self.vars["win8121"] = self.wait_for_window(2000)
    # 18 | click | linkText=Statement of Comprehensive Income |  | 
    self.vars["root"] = self.driver.current_window_handle
    # 19 | click | linkText=Statement of Cash Flows |  | 
    self.driver.switch_to.window(self.vars["win8121"])
    # 20 | click | linkText=Statement of Financial Position |  | 
    self.driver.find_element(By.LINK_TEXT, "Statement of Comprehensive Income").click()
    # 21 | close |  |  | 
    self.driver.find_element(By.LINK_TEXT, "Statement of Cash Flows").click()
    # 22 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.LINK_TEXT, "Statement of Financial Position").click()
    # 23 | selectFrame | index=0 |  | 
    self.driver.close()
    # 24 | click | linkText=2022 |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 25 | selectWindow | handle=${win1066} |  | 
    self.driver.switch_to.frame(0)
    # 26 | click | linkText=Statement of Comprehensive Income |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 27 | click | linkText=Statement of Cash Flows |  | 
    self.driver.find_element(By.LINK_TEXT, "2022").click()
    # 28 | click | linkText=Statement of Financial Position |  | 
    self.vars["win1066"] = self.wait_for_window(2000)
    # 29 | close |  |  | 
    self.driver.switch_to.window(self.vars["win1066"])
    # 30 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.LINK_TEXT, "Statement of Comprehensive Income").click()
    # 31 | selectFrame | index=0 |  | 
    self.driver.find_element(By.LINK_TEXT, "Statement of Cash Flows").click()
    # 32 | click | linkText=2021 |  | 
    self.driver.find_element(By.LINK_TEXT, "Statement of Financial Position").click()
    # 33 | selectWindow | handle=${win334} |  | 
    self.driver.close()
    # 34 | click | linkText=Statement of Comprehensive Income |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 35 | click | linkText=Statement of Cash Flows |  | 
    self.driver.switch_to.frame(0)
    # 36 | click | linkText=Statement of Financial Position |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 37 | close |  |  | 
    self.driver.find_element(By.LINK_TEXT, "2021").click()
    # 38 | selectWindow | handle=${root} |  | 
    self.vars["win334"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win334"])
    self.driver.find_element(By.LINK_TEXT, "Statement of Comprehensive Income").click()
    self.driver.find_element(By.LINK_TEXT, "Statement of Cash Flows").click()
    self.driver.find_element(By.LINK_TEXT, "Statement of Financial Position").click()
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
  
