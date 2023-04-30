import json
from contextlib import suppress
import allure
import pytest
import random
import string
import constants
import psycopg2
from page_objects.site_pages import LoginPage
from utilities.driver_factory import driver_factory
from utilities.configuration import Configuration


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')
    parser.addoption('--env', action='store', help='Env name')


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{constants.ROOT_DIR}/configurations/config.json', 'r') as file:
        res = file.read()
    config = json.loads(res)
    return Configuration(**config)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_browser(env, request):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url)
    yield driver
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(driver.get_screenshot_as_png(), name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    driver.quit()


@pytest.fixture()
def generate_random_email():
    random_email = [''.join(random.choice(string.ascii_letters) for _ in range(10))]
    random_email += "@fake.com"
    return random_email


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


@pytest.fixture()
def expand_dropdown_menu(open_login_page):
    return open_login_page.expand_dropdown_menu()


@pytest.fixture()
def open_main_page(open_login_page, expand_dropdown_menu, env):
    return expand_dropdown_menu.login(env.email, env.password)


@pytest.fixture()
def open_wishlist_page(open_main_page, create_browser):
    return open_main_page.click_wishlist_button()


@pytest.fixture()
def open_hair_category_page(open_main_page, create_browser):
    return open_main_page.click_hair_category_button()


@pytest.fixture()
def open_promotions_page(open_main_page, create_browser):
    return open_main_page.click_promotions_button()


@pytest.fixture()
def logout(open_main_page, create_browser):
    return open_main_page.click_account_button().logout()


@pytest.fixture()
def open_account_page(open_main_page, create_browser):
    return open_main_page.click_account_button()


@pytest.fixture
def open_address_book_tab(open_account_page, create_browser):
    return open_account_page.open_address_book_tab()


@pytest.fixture
def open_wishlist_tab(open_account_page, create_browser):
    return open_account_page.open_wishlist_tab()


@pytest.fixture
def open_orders_history_tab(open_account_page, create_browser):
    return open_account_page.open_orders_history_tab()


@pytest.fixture
def change_site_language(open_main_page, create_browser):
    return open_main_page.change_site_language()


@pytest.fixture
def check_monitor_price(open_wishlist_page, create_browser):
    return open_wishlist_page.monitor_price()


@pytest.fixture
def notify_about_availability(open_wishlist_page, create_browser):
    return open_wishlist_page.notify_about_availability()


@pytest.fixture
def search_item(open_hair_category_page, create_browser):
    return open_hair_category_page.search_item()


@pytest.fixture
def add_to_basket_from_wishlist(open_wishlist_page, create_browser):
    return open_wishlist_page.click_buy_button().continue_shopping()

@pytest.fixture()
def create_db_connection(env):
    __connection = psycopg2.connect(
        user=env.db_user,
        password=env.db_password,
        host=env.host,
        port=env.port,
        database=env.db_name)
    __cursor = __connection.cursor()
    yield __connection, __cursor
    if __connection:
        __cursor.close()
        __connection.close()