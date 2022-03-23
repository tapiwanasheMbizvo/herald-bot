from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
from selenium.webdriver.chrome.options import Options
import time
import herald_bot.constants as const


class Herald(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/pyhtonDrivers", teardown=False):
       

       self.driver_path = driver_path
       self.teardown = teardown
       os.environ["PATH"] += self.driver_path
       super(Herald, self).__init__()
       self.implicitly_wait(15)
       self.maximize_window()
    
    def landing_page(self):
        
        self.get(const.BASE_URL)


    def __exit__(self, *args):
        if self.teardown:
            self.quit()

    def select_top_stories(self):

        top_stories_element = self.find_element(
            by=By.ID,
             value='menu-item-53451'
             )
        top_stories_element.click()

    def get_list_of_headlines(self):
        list_headlines = []
        list_links = []
        article_list = self.find_elements(
            by=By.CLASS_NAME,
            value='s-card-content'
        )
       

        for article in article_list :
            article_title = article.find_element(
                by=By.TAG_NAME,
                value="a"
            ).get_attribute("innerHTML")
            #print(article_title)
            article_link = article.find_element(
                 by=By.TAG_NAME,
                value="a"
            ).get_attribute("href")
            #print(article_link)
            list_headlines.append(article_title)
            list_links.append(article_link)
        #print(list_links)
        return [article_title, list_links]

    def get_contents(self):

        links = self.get_list_of_headlines()[1]
        #print(links)
        for link in links :
            #print(link)
            self.get(link)

            head_line = self.find_element(
                by=By.ID ,
                 value='main-article-title'
                ).get_attribute("innerHTML")
            #print(head_line)
            body_paragraphs = self.find_element(
                by=By.ID,
                value='article-content'
            )
            

            paragraphs = body_paragraphs.find_elements(
                by=By.TAG_NAME,
                value= 'p'
            )

            text= []
            
            for paragraph in paragraphs:
                
                new_text = paragraph.get_attribute("innerHTML")
                #new_text = paragraph.find_emle
                text.append(new_text)    
   
                #print(text)
                print("DONE WITH PAGE UNTO ANOTHER PAGE")
            #time.sleep(5) # wait for 10 seconds and do again 
            
            




