from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage
import allure


class WishlistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __wishlist_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item wish-list active']")
    __monitor_price_checkbox1 = (By.XPATH, "//li/div[2]/div[2]")
    __buy_button = (By.XPATH, "//li[1]/div[2]/div[@class='button buy']")
    __continue_shopping = (By.XPATH, "//div[@class='popup__window']/div[@class='popup-close close-icon']")
    __notify_about_availability = (By.XPATH, "//li[5]/div[2]/div[1]")
    __selected_price_checkbox = (By.XPATH, "//input[@id='set_price_inform-819358-1903479'][@checked]")
    __selected_availability_checkbox = (By.XPATH, "//input[@id='set_inform-811501-1816960'][@checked]")

    def is_wishlist_page_opened(self):
        return self._is_page_opened(locator=self.__wishlist_tab_active)

    @allure.step
    def monitor_price(self):
        self._click(locator=self.__monitor_price_checkbox1)
        return self

    def is_price_checkbox_checked(self):
        if self._is_selected(locator=self.__selected_price_checkbox):
            return True
        else:
            return False

    @allure.step
    def notify_about_availability(self):
        self._click(locator=self.__notify_about_availability)
        return self

    def is_notify_about_availability_checkbox_checked(self):
        if self._is_selected(locator=self.__selected_availability_checkbox):
            return True
        else:
            return False

    @allure.step
    def click_buy_button(self):
        self._click(locator=self.__buy_button)
        return self

    @allure.step
    def continue_shopping(self):
        self._click(locator=self.__continue_shopping)
        return WishlistPage(self.driver)


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __hair_page = (By.XPATH, "//li/span[text() = 'Косметика для волосся']")
    __monitor_the_price = (By.XPATH, "//div[3]/div/div/div[2][@class='button apply']")
    __search_button = (By.XPATH, "//div[@class='search-button']")
    __search_field = (By.XPATH, "//input[@id='search-input']")
    __submit_button = (By.XPATH, "//div[@id='search-modal-container']/button[@type='submit']")
    __searched_item = (By.XPATH, "//li/div/a[@href = '/ua/product/182877/']")
    __item_name = "Batiste Dry Shampoo Clean and Classic Original"

    def is_category_page_opened(self):
        return self._is_page_opened(locator=self.__hair_page)

    @allure.step
    def search_item(self):
        self._click(self.__search_button)
        self._send_keys(locator=self.__search_field, value=self.__item_name)
        self._click(self.__submit_button)
        return self

    def is_searched_item_displayed(self):
        return self._is_displayed(locator=self.__searched_item)


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __logout_button = (By.XPATH, "//a[@href='/ua/user/logout/']")
    __login_button = (By.XPATH, "//a[@href='/ua/user/logout/']")
    __address_book_button = (By.XPATH, "//li[2][@class='private-office__tabs__item']")
    __wishlist_button = (By.XPATH, "//li[@class='private-office__tabs__item wish-list']")
    __orders_history_button = (By.XPATH, "//li[@class='private-office__tabs__item history-order']")
    __address_book_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item active']")
    __wishlist_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item wish-list active']")
    __orders_history_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item history-order active']")
    __contact_info_tab_active = (By.XPATH, "//li[1][@class='private-office__tabs__item active']")

    @allure.step
    def logout(self):
        self._click(self.__logout_button)
        return LoginPage(self.driver)

    @allure.step
    def open_address_book_tab(self):
        self._click(self.__address_book_button)
        return self

    def is_address_book_tab_active(self):
        return self._is_page_opened(locator=self.__address_book_tab_active)

    @allure.step
    def open_wishlist_tab(self):
        self._click(self.__wishlist_button)
        return self

    def is_wishlist_tab_active(self):
        return self._is_page_opened(locator=self.__wishlist_tab_active)

    @allure.step
    def open_orders_history_tab(self):
        self._click(self.__orders_history_button)
        return self

    def is_orders_history_tab_active(self):
        return self._is_page_opened(locator=self.__orders_history_tab_active)

    @allure.step
    def is_contact_info_page_opened(self):
        return self._is_page_opened(locator=self.__contact_info_tab_active)


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __account_button = (By.XPATH, "//header/div/div/div/a[@href='/ua/user/']")
    __wishlist_button = (By.XPATH, "//a[@class='header-favourite']")
    __hair_category_button = (By.XPATH, "//ul[@class='menu-list']/li/a[@href = '/ua/categorys/20272/']")
    __promotions_button = (By.XPATH, "//ul/li[1]/a[@class='header-top-list__link']")
    __promotions_page = (By.XPATH, "//h1[text() = 'Акції']")
    __dropdown_menu = (By.XPATH, "//div[text()[contains(.,'Вхід')]]")
    __change_language_button = (By.XPATH, "//a[@lang='ru']")
    __ru_site_lang = (By.XPATH, "//html[@lang='ru']")

    def is_account_button_displayed(self):
        return self._is_page_opened(locator=self.__account_button)

    @allure.step
    def click_wishlist_button(self):
        self._click(self.__wishlist_button)
        return WishlistPage(self.driver)

    @allure.step
    def click_hair_category_button(self):
        self._click(self.__hair_category_button)
        return CategoryPage(self.driver)

    @allure.step
    def click_promotions_button(self):
        self._click(self.__promotions_button)
        return self

    def is_promotions_page_opened(self):
        return self._is_displayed(locator=self.__promotions_page)

    @allure.step
    def click_account_button(self):
        self._click(self.__account_button)
        return AccountPage(self.driver)

    @allure.step
    def change_site_language(self):
        self._click(self.__change_language_button)
        return self

    def is_site_language_ru(self):
        self._wait_until_element_located(locator=self.__ru_site_lang)
        return self._find_in_dom(locator=self.__ru_site_lang)


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __dropdown_menu = (By.XPATH, "//div[@class='header-office']")
    __dropdown_popup = (By.XPATH, "//form[@data-popup='auth']")
    __email_input = (By.XPATH, "//input[@name= 'user_login']")
    __password_input = (By.XPATH, "//input[@name= 'user_pw']")
    __login_button = (By.XPATH, "//button[text() = 'Увійти']")
    __email_to_subscribe = (By.XPATH, "//input[@placeholder = 'Електронна пошта']")
    __subscribe_button = (By.XPATH, "//button[@class= 'footer-submit']")
    __failed_subscription_popup = (By.XPATH, "//div[text() = 'Ви вже підписані на цю розсилку!']")
    __successful_subscription_popup = (By.XPATH, "//div[text() = 'Ви вдало підписались на цю розсилку! ']")
    __forget_password = (By.XPATH, "//div[@data-popup-handler = 'forget-password']")
    __email_to_remind = (
        By.XPATH, "//input[@id='email-']")
    __remind_button = (By.XPATH, "//button[text() = 'Нагадати']")
    __successful_password_reset_popup = (
        By.XPATH, "//div[contains(text(), 'було надіслано посилання для встановлення нового пароля')]")
    __failed_password_reset_popup = (By.XPATH, "//div[text()= 'Користувач не знайдений у базі даних']")

    @allure.step
    def expand_dropdown_menu(self):
        self._click(self.__dropdown_menu)
        return self

    @allure.step
    def set_email(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    @allure.step
    def set_password(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    @allure.step
    def click_login_button(self):
        self._click(self.__login_button)
        self._is_element_disappeared(locator=self.__dropdown_popup)
        return MainPage(self.driver)

    @allure.step
    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return MainPage(self.driver)

    @allure.step
    def subscribe_with_new_email(self, email):
        self._send_keys(locator=self.__email_to_subscribe, value=email)
        self._click(self.__subscribe_button)
        return self

    @allure.step
    def subscribe_with_existing_email(self, email):
        self._send_keys(locator=self.__email_to_subscribe, value=email)
        self._click(self.__subscribe_button)
        return self

    def is_subscription_failed(self):
        return self._is_displayed(locator=self.__failed_subscription_popup)

    def is_subscription_successful(self):
        return self._is_displayed(locator=self.__successful_subscription_popup)

    @allure.step
    def remind_password(self, email):
        self._click(self.__forget_password)
        self._send_keys(locator=self.__email_to_remind, value=email)
        self._click(self.__remind_button)
        return self

    def is_password_reset_message_successfully_sent(self):
        return self._is_displayed(locator=self.__successful_password_reset_popup)

    def is_password_reset_message_sending_failed(self):
        return self._is_displayed(locator=self.__failed_password_reset_popup)

    def is_login_button_displayed(self):
        return self._is_displayed(locator=self.__dropdown_menu)
