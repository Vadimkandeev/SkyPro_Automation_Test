from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self._drver = driver
        self._drver.get("https://www.labirint.ru/")
      
        

        

    def set_cookie_policy(self):
        cookie = {
            "name": "cookie_policy",
            "value": "1"
        }

        self._drver.add_cookie(cookie)
        print("I am calling")
    
    def search(self, term):
    # найти все книги по слову Питон
        self._drver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self._drver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()