from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def navigate_to_url(self):
        FB_URL = "https://www.facebook.com/"
        self.driver.get(FB_URL)

    def close_browser(self):
        self.driver.quit()