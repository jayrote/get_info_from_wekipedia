from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

class GoogleBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def search(self, query):
        try:
            self.driver.get("https://www.google.com")
            search_box = self.driver.find_element(By.NAME, "q")
            for char in query + ' wikipedia':
                search_box.send_keys(char)
                time.sleep(random.uniform(0.1, 0.3))
            search_box.send_keys(Keys.RETURN)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "yuRUbf")))
            return True
        except Exception as e:
            print(e)
    
    def get_wikipedia(self):
        try:
            wiki = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "yuRUbf")))
            url = wiki.find_element(By.TAG_NAME, "a")
            wikipedia_url = url.get_attribute('href')
            print(f'Wikipedia URL: {wikipedia_url}')
            url.click()
        except Exception as e:
            print(e)

    def get_wikipedia_content(self):
        try:
            content = self.driver.find_element(By.ID, "bodyContent")
            
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            scroll_amount = 300  # Amount to scroll each step (adjust for smoothness)

            # Smoothly scroll from top to bottom
            for i in range(0, total_height, scroll_amount):
                self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
                time.sleep(0.5)

            with open(f'{user_query}.txt', 'w',encoding='utf-8') as file:
                para = content.find_elements(By.TAG_NAME, "p")
                for p in para:
                    text = p.text
                    if text:
                        file.write(text)
                        file.write('\n')
                    # print(p.text)
                    # print()

                file.write("\n" + "=" * 40 + "\nImages\n" + "=" * 40 + "\n")
                images = content.find_elements(By.TAG_NAME, "img")
                for img in images:
                    attr = img.get_attribute("src")
                    if attr:
                        file.write(attr)
                        file.write('\n')

                print(f'{user_query}.txt created successfully')
        except Exception as e:
            print(e)

if __name__ == "__main__":
    bot = GoogleBot()
    user_query = input("Enter your search query: ")
    bot.search(user_query)
    bot.get_wikipedia()
    bot.get_wikipedia_content()
