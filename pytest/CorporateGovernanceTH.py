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

class TestCorporateGovernanceTH27666():
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
  
  def test_corporateGovernanceTH27666(self):
    # Test name: Corporate Governance TH 27/6/66
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
    # 7 | click | linkText=การกำกับดูแลกิจการ |  | 
    self.driver.find_element(By.LINK_TEXT, "การกำกับดูแลกิจการ").click()
    # 8 | click | id=slideout-bt |  | 
    self.driver.find_element(By.ID, "slideout-bt").click()
    # 9 | click | linkText=ยอมรับ |  | 
    self.driver.find_element(By.LINK_TEXT, "ยอมรับ").click()
    # 10 | click | css=tr:nth-child(1) img |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 11 | storeWindowHandle | root |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) img").click()
    # 12 | selectWindow | handle=${win2192} |  | 
    self.vars["win2192"] = self.wait_for_window(2000)
    # 13 | close |  |  | 
    self.vars["root"] = self.driver.current_window_handle
    # 14 | selectWindow | handle=${root} |  | 
    self.driver.switch_to.window(self.vars["win2192"])
    # 15 | click | css=tr:nth-child(2) img |  | 
    self.driver.close()
    # 16 | selectWindow | handle=${win8037} |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 17 | close |  |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 18 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) img").click()
    # 19 | click | css=tr:nth-child(3) img |  | 
    self.vars["win8037"] = self.wait_for_window(2000)
    # 20 | selectWindow | handle=${win4147} |  | 
    self.driver.switch_to.window(self.vars["win8037"])
    # 21 | close |  |  | 
    self.driver.close()
    # 22 | selectWindow | handle=${root} |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 23 | click | css=tr:nth-child(4) img |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 24 | selectWindow | handle=${win45} |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) img").click()
    # 25 | close |  |  | 
    self.vars["win4147"] = self.wait_for_window(2000)
    # 26 | selectWindow | handle=${root} |  | 
    self.driver.switch_to.window(self.vars["win4147"])
    # 27 | click | css=tr:nth-child(5) img |  | 
    self.driver.close()
    # 28 | selectWindow | handle=${win173} |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 29 | close |  |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 30 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) img").click()
    # 31 | click | linkText=นโยบายต่อต้านการคอร์รัปชั่น |  | 
    self.vars["win45"] = self.wait_for_window(2000)
    # 32 | click | linkText=คู่มือจริยธรรมธุรกิจ |  | 
    self.driver.switch_to.window(self.vars["win45"])
    # 33 | click | linkText=นโยบายการบริหารจัดการด้านความยั่งยืน |  | 
    self.driver.close()
    # 34 | click | linkText=นโยบายภาษี |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 35 | click | linkText=นโยบายการกำกับดูแลกิจการของบริษัทฯ |  | 
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) img").click()
    self.vars["win173"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win173"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.find_element(By.LINK_TEXT, "นโยบายต่อต้านการคอร์รัปชั่น").click()
    self.driver.find_element(By.LINK_TEXT, "คู่มือจริยธรรมธุรกิจ").click()
    self.driver.find_element(By.LINK_TEXT, "นโยบายการบริหารจัดการด้านความยั่งยืน").click()
    self.driver.find_element(By.LINK_TEXT, "นโยบายภาษี").click()
    self.driver.find_element(By.LINK_TEXT, "นโยบายการกำกับดูแลกิจการของบริษัทฯ").click()
  
