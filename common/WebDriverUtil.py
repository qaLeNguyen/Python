import logging
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('WebDriverUtil')

class WebDriverUtil:
    driver = None
    wait_time = 10
    wait_visible = 15
    wait_clickable = 25

    @staticmethod
    def initialize_driver(browser_name='chrome'):
        browser_name = browser_name.lower()

        try:
            if browser_name == 'chrome':
                driver_path = "D:\\5. Webdriver\\chromedriver-win64\\chromedriver.exe"
                service = ChromeService(executable_path=driver_path)
                options = webdriver.ChromeOptions()
                WebDriverUtil.driver = webdriver.Chrome(service=service, options=options)

            elif browser_name == 'firefox':
                driver_path = "D:\\5. Webdriver\\geckodriver-v0.34.0-win-aarch64\\geckodriver.exe"
                service = FirefoxService(executable_path=driver_path)
                options = webdriver.FirefoxOptions()
                WebDriverUtil.driver = webdriver.Firefox(service=service, options=options)

            elif browser_name == 'edge':
                driver_path = "D:\\5. Webdriver\\edgedriver_win64\\msedgedriver.exe"
                service = EdgeService(executable_path=driver_path)
                options = webdriver.EdgeOptions()
                WebDriverUtil.driver = webdriver.Edge(service=service, options=options)

            else:
                raise ValueError(f"Unsupported browser: {browser_name}")

            WebDriverUtil.driver.maximize_window()
            logger.info(f"Initialized {browser_name} driver")
            return WebDriverUtil.driver

        except Exception as e:
            logger.error(f"Failed to initialize {browser_name} driver: {e}")
            raise

    @staticmethod
    def get_driver() -> WebDriver:
        if WebDriverUtil.driver is None:
            raise Exception("Driver has not been initialized. Call initialize_driver() first.")
        return WebDriverUtil.driver

    @staticmethod
    def get_wait(driver: WebDriver) -> WebDriverWait:
        return WebDriverWait(driver, WebDriverUtil.wait_time)

    @staticmethod
    def get_wait_visible(driver: WebDriver) -> WebDriverWait:
        return WebDriverWait(driver, WebDriverUtil.wait_visible)

    @staticmethod
    def get_wait_clickable(driver: WebDriver) -> WebDriverWait:
        return WebDriverWait(driver, WebDriverUtil.wait_clickable)

    @staticmethod
    def quit_driver():
        if WebDriverUtil.driver:
            WebDriverUtil.driver.quit()
            WebDriverUtil.driver = None
            logger.info("Driver quit successfully")
