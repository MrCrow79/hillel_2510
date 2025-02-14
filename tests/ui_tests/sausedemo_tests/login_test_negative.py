import time

from setting import d_settings


# прибрати імпорти = ctrl+alt+o


def test_login_wrong_credentials_negative(driver, login_page):


    # login error
    login_page.set_user_name('wrong_user_name', timeout=5)
    login_page.set_user_pwd(d_settings.sausedemo_pwd)
    login_page.click_login()


    # login_page.set_user_name('wrong_user_name').set_user_pwd(d_settings.sausedemo_pwd).click_login()
    login_page.check_creds_are_wrong()
    time.sleep(1)


