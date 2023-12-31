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

class TestFinanceStatementTH():
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
  
  def test_financeStatementTH(self):
    # Test name: Finance Statement TH
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
    # 6 | click | linkText=นักลงทุนสัมพันธ์ |  | 
    self.driver.find_element(By.LINK_TEXT, "นักลงทุนสัมพันธ์").click()
    # 7 | mouseOver | linkText=ข้อมูลทางการเงิน |  | 
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลทางการเงิน")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | linkText=งบการเงิน |  | 
    self.driver.find_element(By.LINK_TEXT, "งบการเงิน").click()
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
    # 15 | click | linkText=2566 |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 16 | storeWindowHandle | root |  | 
    self.driver.find_element(By.LINK_TEXT, "2566").click()
    # 17 | selectWindow | handle=${win1392} |  | 
    self.vars["win1392"] = self.wait_for_window(2000)
    # 18 | click | linkText=งบกำไรขาดทุนเบ็ดเสร็จ |  | 
    self.vars["root"] = self.driver.current_window_handle
    # 19 | click | linkText=งบกระแสเงินสด |  | 
    self.driver.switch_to.window(self.vars["win1392"])
    # 20 | click | linkText=งบแสดงฐานะการเงิน |  | 
    self.driver.find_element(By.LINK_TEXT, "งบกำไรขาดทุนเบ็ดเสร็จ").click()
    # 21 | close |  |  | 
    self.driver.find_element(By.LINK_TEXT, "งบกระแสเงินสด").click()
    # 22 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.LINK_TEXT, "งบแสดงฐานะการเงิน").click()
    # 23 | selectFrame | index=0 |  | 
    self.driver.close()
    # 24 | click | linkText=2565 |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 25 | selectWindow | handle=${win618} |  | 
    self.driver.switch_to.frame(0)
    # 26 | click | linkText=งบกำไรขาดทุนเบ็ดเสร็จ |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 27 | click | linkText=งบกระแสเงินสด |  | 
    self.driver.find_element(By.LINK_TEXT, "2565").click()
    # 28 | click | linkText=งบแสดงฐานะการเงิน |  | 
    self.vars["win618"] = self.wait_for_window(2000)
    # 29 | close |  |  | 
    self.driver.switch_to.window(self.vars["win618"])
    # 30 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.LINK_TEXT, "งบกำไรขาดทุนเบ็ดเสร็จ").click()
    # 31 | selectFrame | index=0 |  | 
    self.driver.find_element(By.LINK_TEXT, "งบกระแสเงินสด").click()
    # 32 | click | linkText=2564 |  | 
    self.driver.find_element(By.LINK_TEXT, "งบแสดงฐานะการเงิน").click()
    # 33 | selectWindow | handle=${win2862} |  | 
    self.driver.close()
    # 34 | click | linkText=งบกำไรขาดทุนเบ็ดเสร็จ |  | 
    self.driver.switch_to.window(self.vars["root"])
    # 35 | click | linkText=งบกระแสเงินสด |  | 
    self.driver.switch_to.frame(0)
    # 36 | click | linkText=งบแสดงฐานะการเงิน |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 37 | close |  |  | 
    self.driver.find_element(By.LINK_TEXT, "2564").click()
    # 38 | selectWindow | handle=${root} |  | 
    self.vars["win2862"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win2862"])
    self.driver.find_element(By.LINK_TEXT, "งบกำไรขาดทุนเบ็ดเสร็จ").click()
    self.driver.find_element(By.LINK_TEXT, "งบกระแสเงินสด").click()
    self.driver.find_element(By.LINK_TEXT, "งบแสดงฐานะการเงิน").click()
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
  
