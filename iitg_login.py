#! /usr/local/bin/python3

from selenium import webdriver
import sys
import os
import time
from datetime import datetime

# print("Enter Username: ")
user = os.environ.get("user")
# print("Enter Password: ")
passw = os.environ.get("pass")

driver = webdriver.Chrome()


def loginAuth():
    url = "https://agnigarh.iitg.ac.in:1442/logout?"
    # Press logout twice #
    logoutAuth()
    logoutAuth()

    username = driver.find_element_by_id("ft_un")
    username.clear()
    username.send_keys(user)

    password = driver.find_element_by_id("ft_pd")
    password.clear()
    password.send_keys(passw)

    driver.find_element_by_tag_name("button").click() # Press Login #
    return 1

def logoutAuth():
    url = "https://agnigarh.iitg.ac.in:1442/logout?"
    driver.get(url)

def keepAlive():
    url = "https://agnigarh.iitg.ac.in:1442/keepalive?"
    driver.get(url)
    # Try finding my name
    if("class=\"offline\"" in driver.page_source):
        print(str(datetime.now()) + "You are not connected to Internet! Please do! Retrying after 10s")
        time.sleep(8)
        return

    if(user not in driver.page_source):
        loginAuth()


while(True):
    try:
        keepAlive()
    except Exception as e:
        print(e)
        print(str(datetime.now()) + "Some Problem Occured")
        pass

    time.sleep(2)
