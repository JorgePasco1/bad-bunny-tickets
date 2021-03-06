"""Service for entering into Bad Bunny ticket purchase queue."""


from selenium.webdriver.common.by import By
from adapters.web_scrapping_adapter import start_webdriver

from lib.constants import BUY_BUTTON_XPATH, TICKETS_URL


def multiple_queueing(number_of_queues: int):
    """Enters a queue multiple times."""

    def enter_queue():
        """Starts a new driver and enters the queue."""

        driver = start_webdriver()
        driver.get(TICKETS_URL)
        buy_button = driver.find_element(By.XPATH, BUY_BUTTON_XPATH)
        buy_button.click()

    for i in range(number_of_queues + 1):
        print(f"Opening browser {i + 1}")
        enter_queue()
