import selenium
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeService

from . import s


def d(profile, options=None, proxy=None, headless=False):
    options = s.DriverOptions().options

    # options.add_argument("--headless")
    options.add_argument("--user-data-dir=%s" % profile)
    if proxy:
        print(proxy) 
        options.add_argument("--proxy-server=%s" % proxy)
    if headless: options.add_argument("--headless")

    service = ChromeService()

    driver =  Chrome(options, service)

    return driver


