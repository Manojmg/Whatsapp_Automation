# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:53:04 2019

@author: Manoj
"""

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')


driver.get('https://web.whatsapp.com/')
name = input("Enter the name of the user")
message = input("Enter the message")
count = int(input("Enter the count"))
input("Enter anything after scanning the QR code")

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()
message_box = driver.find_element_by_class_name("_3u328")
for i in range(count):
    message_box.send_keys(message)
    driver.find_element_by_class_name('_3M-N-').click()