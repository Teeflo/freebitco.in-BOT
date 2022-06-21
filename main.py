import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# open config.json
with open("config.json", "r") as confg:
    config = json.load(confg)

# take your login info
config_user = config["user"]
config_password = config["password"]
chrome_driver = './Drivers/chromedriver.exe'


class freeBTC_Claim:
  driver = webdriver.Chrome(chrome_driver)
  wait_a_min_or = WebDriverWait(driver, 60)

  def start(self):

    self.driver.get("https://freebitco.in/?op=home#")
    self.driver.maximize_window()
    self.login(config_user, config_password)

  def login(self,config_user, config_password):
    # Click on login tab
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a')))
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/nav/section/ul/li[10]/a').click()
    # Type login and password and submit
    self.wait_a_min_or.until(EC.presence_of_element_located((By.ID, "login_form_btc_address")))
    self.driver.find_element(By.ID, "login_form_btc_address").send_keys(config_user)
    self.driver.find_element(By.ID, "login_form_password").send_keys(config_password)
    self.driver.find_element(By.ID, "login_button").click()
    # Close push notification pop-up
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]')))
    self.driver.find_element(By.XPATH, '//*[@id="push_notification_modal"]/div[1]/div[2]/div/div[1]').click()
    # Close cookies warn
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/a[1]')))
    self.driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()
    # click on claimed BTC without captcha
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[7]/div[2]/div/div[1]/div[1]')))
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[7]/div[2]/div/div[1]/div[1]').click()
    #click on roll
    self.wait_a_min_or.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[7]/p[3]/input')))
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[7]/p[3]/input').click()
    time.sleep(2)
    #close browser
    self.driver.quit()
