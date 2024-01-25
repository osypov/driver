

import sys
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time





class DriverOptions(object):

    def __init__(self, options=None):

        if options:
            self.options = options
        else:
            self.options = Options()
        self.options.add_argument('--no-sandbox')
        # self.options.add_argument('--start-maximized')
        # # self.options.add_argument('--start-fullscreen')
        # self.options.add_argument('--single-process')
        # # self.options.add_argument('--disable-dev-shm-usage')
        # # self.options.add_argument("--incognito")
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        # self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--window-size=2560,1440")

    
