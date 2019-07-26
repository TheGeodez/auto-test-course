from selenium import webdriver
import os


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

name = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(2)')
name.send_keys('First name')

last_name = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(4)")
last_name.send_keys('Last name')

email = browser.find_element_by_css_selector("body > div > form > div > input:nth-child(6)")
email.send_keys('123@gmail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '123.txt')

send_file = browser.find_element_by_id('file')
send_file.send_keys(file_path)

button = browser.find_element_by_css_selector('.btn')
button.click()

