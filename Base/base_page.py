import datetime
from urllib import request


class BasePage:

    def __init__(self, browser, url, logger, timeout=30):
        self.browser = browser
        self.timeout = timeout
        self.url = url
        self.logger = logger

    def open(self):
        self.browser.get(self.url)

    def get_current_url(self):
        current_url = self.browser.current_url
        print(current_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, "Incorrect result word"

    def get_screenshot(self, directory):
        now_date = datetime.datetime.utcnow().strftime("%Y_%m_%d.%H.%M.%S")
        name_screenshot = f'finish_scr_{now_date}.png'
        self.browser.save_screenshot(f'{directory}/Screen/{name_screenshot}')

    def assert_url(self, result):
        get_url = self.browser.current_url
        assert result == get_url, "incorrect url"
