"""A web scrapping adapter implemented in Selenium."""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

USER_AGENT = UserAgent()
CHROME_EXEC_PATH = ChromeDriverManager().install()


def start_webdriver():
    """
    This function starts a Chrome webdriver, with a random user agent, it
    keeps the browser open.
    """

    options = Options()
    user_agent = USER_AGENT.random
    options.add_argument(f'user-agent={user_agent}')
    options.add_experimental_option("detach", True)
    return webdriver.Chrome(CHROME_EXEC_PATH, options=options)
