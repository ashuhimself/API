import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pandas as pd 



class YouTubeCommentScraper:
    def __init__(self, url):
        self.url = url 
        self.driver = webdriver.Chrome("chromedriver", options=Options())  
        self.wait = WebDriverWait(self.driver, 10)  
 
    def open(self):
        self.driver.get(self.url)
 
    def scroll(self):
        self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END) 
        time.sleep(3) 
 
    def scrape(self):
        comments = [] 
        for comment in self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "comment content-text"))):  
            comments.append(comment.text) 
        return comments 
 
    def close(self):
        self.driver.close() 
 


scraper = YouTubeCommentScraper("https://www.youtube.com/watch?v=kffacxfA7G4")


scraper.open()

for i in  range(10):
    scraper.scroll()

comments = scraper.scrape()
data = pd.DataFrame(comments, columns=['comments'])
data.to_csv('comments.csv', index=False)