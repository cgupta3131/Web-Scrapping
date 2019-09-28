from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

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

	url = "https://mail.google.com"
	driver.get(url)

	return 1


def SocialDelete():

	tab = driver.find_element_by_xpath("//div[ contains(@aria-label, \"Social\")]")
	tab.click()

	select_all = driver.find_element_by_xpath("//div[ contains(@aria-label, \"Select\")]")
	select_all.click()

	time.sleep(1)
	delete_btn = driver.find_element_by_xpath("//div[ contains(@aria-label, \"Delete\")]")

	try:
		delete_btn.click()
		print("Element Clickable")
	except WebDriverException:
	    print("Element is not clickable")

def PromoDelete():

	tab = driver.find_element_by_xpath("//div[ contains(@aria-label, \"Promotions\")]")
	tab.click()

	select_all = driver.find_element_by_xpath("//div[ contains(@aria-label, \"Select\")]")
	select_all.click()

	time.sleep(1)
	delete_btn = driver.find_element_by_xpath("//div[ contains(@aria-label, \"Delete\")]")

	try:
		delete_btn.click()
		print("Element Clickable")
	except WebDriverException:
	    print("Element is not clickable")

loginAuth()
while(True):
	SocialDelete()
	time.sleep(3)
	PromoDelete()
	time.sleep(3)
