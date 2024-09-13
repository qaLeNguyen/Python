from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webelement import WebElement
from common.Locator import CommonLocator
from common.WebDriverUtil import WebDriverUtil
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
import logging

class BuiltInAction:
    def __init__(self, driver: WebDriver):
        """
        Initializes the BuiltInAction with the WebDriver instance.

        :param driver: A WebDriver instance.
        """
        if driver is None:
            # If no driver is passed, initialize one
            driver = WebDriverUtil.get_driver()

        self.logger = logging.getLogger('BuiltInAction')
        self.driver = driver
        self.wait = WebDriverUtil.get_wait(driver)
        self.wait_visible = WebDriverUtil.get_wait_visible(driver)
        self.wait_clickable = WebDriverUtil.get_wait_clickable(driver)

    def get_element_visible(self, locator) -> WebElement:
        """
        Waits for an element to be visible on the page.

        :param locator: A tuple containing the locator strategy and value (e.g., (By.NAME, 'q'))
        :return: The WebElement if visible
        :raises TimeoutException: Is the element not visible within the wait time
        """
        try:
            self.logger.debug("Attempting to wait for element to be visible: '%s'", locator)
            element = self.wait_visible.until(EC.visibility_of_element_located(locator))
            self.logger.debug("Element is visible: '%s'", locator)
            return element
        except TimeoutException:
            self.logger.error("TimeoutException: Element ''%s'' not visible within the wait time", locator)
            raise
        except Exception as e:
            self.logger.error("An unexpected error occurred: '%s'", locator, str(e))

    def get_element_clickable(self, locator):
        """
        Waits for an element to be visible and clickable on the page.

        :param locator: A tuple containing the locator strategy and value (e.g., (By.NAME, 'q'))
        :return: The WebElement if visible
        :raises TimeoutException: Is the element not visible within the wait time
        """
        try:
            self.logger.debug("Attempting to wait for element to be clickable: '%s'", locator)
            element = self.wait_clickable.until(EC.element_to_be_clickable(locator))
            self.logger.debug("Element is clickable: '%s'", locator)
            return element
        except TimeoutException:
            self.logger.error("Element '%s' not clickable  within the wait time", locator)
        except Exception as e:
            self.logger.error("An unexpected error occurred: '%s'", locator, e)

    def is_element_present(self, locator) -> bool:
        """
        Checks if an element exists and is visible on the page.

        :param locator: A tuple representing the locator strategy and value
        :return: True if the element exists and is visible, False otherwise
        """
        try:
            self.logger.debug("Attempting to find element: '%s'", locator)
            element = self.get_element_visible(locator)
            is_displayed = element.is_displayed()
            if is_displayed:
                self.logger.debug("Element found and is displayed: '%s'", locator)
            return is_displayed
        except NoSuchElementException:
            self.logger.error("Element not found: '%s' while checking if it exists", locator)
            return False
        except TimeoutException:
            self.logger.error("Timeout while waiting for element: '%s'", locator)
            return False
        except Exception as e:
            self.logger.error("An unexpected error occurred"
                              " while checking for element: '%s'", locator, e)

    def click(self, locator):
        """
        Click an element

        :param locator: A tuple representing the locator strategy and value
        :return: True if the element is clicked, False otherwise
        """
        try:
            self.logger.debug("Attempting to click element: '%s'", locator)
            self.get_element_clickable(locator).click()
            self.logger.debug("Clicked element: '%s'", locator)
        except NoSuchElementException:
            self.logger.error("Element not found: '%s'"
                         "while clicking to it", locator)
        except ElementNotInteractableException:
            self.logger.error("Element not interactable: '%s' "
                              "while trying to interact with it", locator)
        except Exception as e:
            self.logger.error("An unexpected error occurred"
                              " when clicking the element: '%s'", locator, e)

    def click_with_retries(self, locator, max_retries: int):
        """
        Click to an element, and re-try(times) to click again if 1st attempt is failed.

        :param locator:
        :param max_retries: the times that will retry to click
        """
        attempt = 0
        while attempt < max_retries:
            try:
                self.logger.debug("Attempting to click element: ''%s''", locator)
                self.get_element_clickable(locator).click()
                self.logger.debug("Successfully clicked on element: '%s'", locator)
                return
            except NoSuchElementException:
                self.logger.error("Element not found: '%s'", locator)
            except StaleElementReferenceException:
                self.logger.error("Element is Stale: '%s'", locator)
            except TimeoutException:
                self.logger.error("Timeout occurred"
                                  " while clicking locator: '%s'", locator)
                break
            attempt += 1
        self.logger.error("Failed to click on element"
                          " located by '%s' after %d attempts", locator, max_retries)

    def input(self, locator, value: str):
        """
        Input a value into a field.

        :param locator: Located by CSS|XPath
        :param value:   Value input(E.g: text, number...)
        """
        try:
            self.logger.debug("Attempting to input '%s' into element '%s': ", value, locator)
            element = self.get_element_clickable(locator)
            element.clear()
            element.send_keys(value)
            self.logger.debug("Inputted: '%s' into element: '%s'", value, locator)
        except NoSuchElementException:
            self.logger.error("Element not found: '%s'", locator)
        except StaleElementReferenceException:
            self.logger.error("Stale element while inputting text for locator: '%s'", locator)
        except TimeoutException:
            self.logger.error("Timeout while waiting for locator: '%s'", locator)
        except Exception as e:
            self.logger.error("Exception occurred "
                              "while inputting value into locator: '%s'", locator, e)

    def replace_value(self, locator, value: str):
        """
        Replace a new value into a field.

        :param locator:  Located by CSS|XPath
        :param value:    New value will be replaced into the field
        """
        try:
            self.logger.debug("Attempting to replace value into locator: ''%s''", locator)
            field = self.get_element_clickable(locator)
            field.click()
            field.send_keys(Keys.CONTROL, 'a')
            field.send_keys(value)
            self.logger.debug("Successfully replace new value into locator: %s", locator)
        except ElementNotInteractableException:
            self.logger.error("The locator: '%s' is not interactable", locator)
        except TimeoutException:
            self.logger.error("Timeout while performing action"
                              " 'replace value' in locator '%s'", locator)
        except Exception as e:
            self.logger.error("Exception occurred while"
                              " replacing new value into '%s'", locator, e)

    def hover_over(self, locator):
        """
        Hover over an element

        :param locator:  Located by CSS|XPath
        """
        try:
            self.logger.debug("Attempting to hover over the locator: '%s'", locator)
            element = self.get_element_visible(locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.logger.debug("Hovered over the locator: '%s'", locator)
        except NoSuchElementException:
            self.logger.error("Element '%s' not found in order to hover", locator)
        except Exception as e:
            self.logger.error("Exception occurred while hovering to the locator", e)

    def select_item_in_dropdown(self, locator):
        """
        Item is displayed inside the dropdown.

        :param locator:  Located by CSS|XPath
        """
        try:
            self.logger.debug("Attempting to pick up the item in dropdown")
            item = self.get_element_clickable(locator)
            item.click()
            self.logger.debug("Clicked the dropdown item locator: %s", locator)
        except NoSuchElementException:
            self.logger.error("Element '%s' not found in the dropdown list", locator)
        except Exception as e:
            self.logger.error("Exception occurred while"
                              " clicking to the locator: %s", locator, e)

    def scroll_to_view(self, locator):
        """
        Scrolling until found the element

        :param locator:  Located by CSS|XPath
        """
        try:
            self.logger.debug("Attempting to scroll until find the locator: '%s'", locator)
            element = self.get_element_visible(locator)

            if element is not None:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.logger.info("Found locator: '%s'", locator)
            else:
                self.logger.error("Not found locator: '%s'", locator)
        except TimeoutException:
            self.logger.error("Timeout occurred while "
                              "trying to find the locator: '%s'", locator)
        except Exception as e:
            self.logger.error("Exception occurred while"
                              " scrolling to find locator: '%s'", locator, e)

    def select_option_in_profile_or_package(self, option_dropdown, option_item):
        """
        Click on the dropdown to reveal a list of options, then select an item from the list.

        :param option_dropdown:  Located by CSS|XPath
        :param option_item:      Located by CSS|XPath
        """
        try:
            self.logger.debug("Attempting to click on option '%s' and pick the item '%s' in the dropdown")
            self.scroll_to_view(option_dropdown)
            self.click(option_dropdown)
            self.get_element_visible(option_item)
            self.get_element_clickable(option_item)
            self.click(option_item)
            self.logger.debug("Select option '%s'", option_item)
        except NoSuchElementException:
            self.logger.error("There is no option locator: '%s'", option_item)
        except TimeoutException:
            self.logger.error("Timeout occurred while"
                              " selecting option locator: '%s'", option_item)
        except Exception as e:
            self.logger.error("Exception occurred while"
                              " selecting option locator: '%ss'", option_item, e)

    def is_succeed(self) -> bool:
        message_succeed = self.is_element_present(CommonLocator.OPERATION_SUCCEEDED_ALERT)
        if message_succeed:
            self.logger.debug("Operation succeed is displayed")
        else:
            self.logger.error("Operation succeed is not displayed")
        return message_succeed

    def is_field_empty(self, locator, attribute: str):
        """
        Checks if a field is empty.

        This method waits for the field located by the given locator to be visible and retrieves
        its value to check if it is empty.

        :param locator: A tuple used to locate the field on the web page (e.g., (By.ID, "username"))
        :param attribute: The attribute of the WebElement to check (e.g., "value", "innerText")
        :return: True if the field is empty or null; False otherwise
        """
        try:
            element = self.get_element_visible(locator)
            field =  element.get_attribute(attribute)
            return field is None or field == ''
        except (NoSuchElementException, TimeoutException):
            self.logger.error("Element not found/ Timeout occurred while"
                              " checking if locator: '%s' is empty", locator)
        except Exception as e:
            self.logger.error("Exception occurred while"
                              " checking if locator: '%s' is empty", locator, e)


