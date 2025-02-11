from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome() # відкриття browser

driver.get("http://0.0.0.0:8000/lessons/lesson_26/html_pages/elements.html")


# Знаходження текстових полів за ID і введення тексту
username_field = driver.find_element(By.ID, "username")
user_name = "example_username"
username_field.send_keys(user_name)  # username_field.get_attribute('value')

assert username_field.get_attribute('value') == user_name

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("example_password")

# Знаходження радіо кнопок за ID і вибір варіанта
male_radio = driver.find_element(By.ID, "male")
male_radio.click()

# Знаходження чекбоксу за ID і встановлення прапорця
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()

# Вибір значення з випадаючого списку за ID
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("США")

# Натискання на кнопку за ID
submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
print(submit_button.is_enabled())
# Зачекати 5 секунд перед завершенням
time.sleep(5)


driver.quit()  # закривати driver