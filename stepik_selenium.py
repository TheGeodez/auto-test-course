from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
name.send_keys('Name')
time.sleep(1)
name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
name.send_keys('No name')
time.sleep(1)
name = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
name.send_keys('No name')
time.sleep(1)

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text