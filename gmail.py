from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome();


user = "cgupta3131@gmail.com"
passw = "Fidato@27"

def loginAuth():
	url = "https://accounts.google.com"
	driver.get(url)

	time.sleep(1)

	username = driver.find_element_by_id("identifierId")
	username.clear()
	username.send_keys(user)

	driver.find_element_by_id("identifierNext").click()
	time.sleep(1)

	password = driver.find_element_by_name("password")
	password.clear()
	password.send_keys(passw)

	driver.find_element_by_id("passwordNext").click()
	time.sleep(2)

	urlx = "https://mail.google.com"
	driver.get(urlx)

	return 1

loginAuth()