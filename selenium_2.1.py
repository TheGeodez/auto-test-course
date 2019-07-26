from selenium import webdriver
import time
import math





link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure = browser.find_element_by_id('treasure')
x = treasure.get_attribute("valuex")


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

checkbox = browser.find_element_by_id('robotCheckbox')
checkbox.click()

radiobutton = browser.find_element_by_id('robotsRule')
radiobutton.click()

btn = browser.find_element_by_css_selector('.btn')
btn.click()



