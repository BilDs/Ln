# Linkedin automation
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver.exe")
driver.get("https://www.linkedin.com")
# driver.get("https://www.linkedin.com/sales/login") connect to sales navigator
time.sleep(2)

#               connect to Linkedin account                    #

username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")
LN_username = "b.merad@dtwin.city"
LN_password = "password"
username.send_keys(LN_username)
password.send_keys(LN_password)
time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

# ******************** Connect with leads ********************* #
driver.get("result link ")
time.sleep(2)
