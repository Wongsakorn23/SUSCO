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

class TestCalculatorTH27666():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_calculatorTH27666(self):
    # Test name: Calculator TH 27/6/66
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
    # 7 | mouseOver | linkText=ข้อมูลราคาหลักทรัพย์ |  | 
    element = self.driver.find_element(By.LINK_TEXT, "ข้อมูลราคาหลักทรัพย์")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | linkText=เครื่องคำนวณการลงทุน |  | 
    self.driver.find_element(By.LINK_TEXT, "เครื่องคำนวณการลงทุน").click()
    # 9 | click | id=slideout-bt |  | 
    self.driver.find_element(By.ID, "slideout-bt").click()
    # 10 | click | linkText=ยอมรับ |  | 
    self.driver.find_element(By.LINK_TEXT, "ยอมรับ").click()
    # 11 | click | id=price_purchase_enter |  | 
    self.driver.find_element(By.ID, "price_purchase_enter").click()
    # 12 | type | id=price_purchase_enter | 1000 | 
    self.driver.find_element(By.ID, "price_purchase_enter").send_keys("1000")
    # 13 | click | id=shares_held_enter |  | 
    self.driver.find_element(By.ID, "shares_held_enter").click()
    # 14 | type | id=shares_held_enter | 1000 | 
    self.driver.find_element(By.ID, "shares_held_enter").send_keys("1000")
    # 15 | click | id=price_sold_enter |  | 
    self.driver.find_element(By.ID, "price_sold_enter").click()
    # 16 | type | id=price_sold_enter | 1000 | 
    self.driver.find_element(By.ID, "price_sold_enter").send_keys("1000")
    # 17 | click | id=dividend_taxed_enter |  | 
    self.driver.find_element(By.ID, "dividend_taxed_enter").click()
    # 18 | type | id=dividend_taxed_enter | 1000 | 
    self.driver.find_element(By.ID, "dividend_taxed_enter").send_keys("1000")
    # 19 | click | id=dividend_tax_exempt_enter |  | 
    self.driver.find_element(By.ID, "dividend_tax_exempt_enter").click()
    # 20 | type | id=dividend_tax_exempt_enter | 1000 | 
    self.driver.find_element(By.ID, "dividend_tax_exempt_enter").send_keys("1000")
    # 21 | click | css=.button |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".button").click()
  
