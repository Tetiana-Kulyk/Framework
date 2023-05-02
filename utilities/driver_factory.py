from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as firefox_service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

__CHROME = 1
__FIRE_FOX = 2
__SAFARI = 3


def driver_factory(driver_id: int):
    if int(driver_id) == __CHROME:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        return Chrome(service=chrome_service(ChromeDriverManager().install()), options=chrome_options)
    elif int(driver_id) == __FIRE_FOX:
        return Firefox(service=firefox_service(GeckoDriverManager.install()))
    elif int(driver_id) == __SAFARI:
        return None
    else:
        return Chrome(service=chrome_service(ChromeDriverManager().install()))
