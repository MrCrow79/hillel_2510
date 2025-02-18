from setting import d_settings


# прибрати імпорти = ctrl+alt+o


def test_login(driver, login_page):


    login_page.login(d_settings.sausedemo_user_name, d_settings.sausedemo_pwd).product_page_check_page_is_opened()

