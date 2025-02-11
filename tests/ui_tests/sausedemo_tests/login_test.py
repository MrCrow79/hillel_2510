from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By



def test_login():
    # iніціалізуємо веб-драйвер
    driver = Chrome()

    # відкриття сторінки
    driver.get("https://www.saucedemo.com/")

    user_name = 'standard_user'
    password = 'secret_sauce'

    login_input_locator = '#user-name'
    password_input_locator = '//input[@data-test="password"]'
    login_button_locator = '#login-button'

    user_name_filed = driver.find_element(By.CSS_SELECTOR, login_input_locator)
    user_password_filed = driver.find_element(By.XPATH, password_input_locator)
    login_button = driver.find_element(By.CSS_SELECTOR, login_button_locator)

    user_name_filed.send_keys(user_name)
    user_password_filed.send_keys(password)
    login_button.click()

    driver.find_element(By.XPATH, '//div[@class="header_secondary_container"]')

    driver.quit()



