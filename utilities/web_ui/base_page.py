from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _find_in_dom(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_to_be_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    @allure.step
    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    @allure.step
    def _click(self, locator):
        self._wait_until_to_be_clickable(locator).click()

    def _is_page_opened(self, locator):
        page = self.__wait.until(EC.visibility_of_element_located(locator))
        return page.is_displayed()

    def _is_selected(self, locator):
        self.driver.refresh()
        return self.__wait.until(EC.element_attribute_to_include(locator=locator, attribute_='checked'))

    def _is_element_disappeared(self, locator):
        return self.__wait.until(EC.invisibility_of_element_located(locator=locator))

    @allure.step
    def _is_displayed(self, locator):
        return self._wait_until_element_located(locator)
