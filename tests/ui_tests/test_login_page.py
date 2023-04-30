import pytest

from utilities.config_reader import get_user_creds


@pytest.mark.login
@pytest.mark.smoke
def test_login(expand_dropdown_menu):
    main_page = expand_dropdown_menu.set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button()
    assert main_page.is_account_button_displayed(), 'Account button is not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_subscribe_with_existing_email(open_login_page):
    login_page = open_login_page.subscribe_with_existing_email(email=get_user_creds()[0])
    assert login_page.is_subscription_failed(), 'User is able to subscribe with already subscribed email'


@pytest.mark.login
@pytest.mark.regression
def test_subscribe_with_new_email(open_login_page, generate_random_email):
    login_page = open_login_page.subscribe_with_new_email(email=generate_random_email)
    assert login_page.is_subscription_successful(), 'User is not able to subscribe with new email'


@pytest.mark.login
@pytest.mark.regression
def test_password_reset_with_valid_email(expand_dropdown_menu):
    dropdown_menu = expand_dropdown_menu.remind_password(email=get_user_creds()[0])
    assert dropdown_menu.is_password_reset_message_successfully_sent(), 'Password reset message is not sent'


@pytest.mark.login
@pytest.mark.regression
def test_password_reset_with_invalid_email(expand_dropdown_menu, generate_random_email):
    dropdown_menu = expand_dropdown_menu.remind_password(email=generate_random_email)
    assert dropdown_menu.is_password_reset_message_sending_failed(), 'Password reset message is sent to not ' \
                                                                     'registered email'
