from selenium import webdriver
import webbrowser
from time import sleep



class InstaBot:
    def __init__(self, username, pw):
        self.driver=webdriver.Chrome("C:\\<Path to chromedriver>\\chromedriver.exe")
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        #accept coolkies
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")\
            .click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]/button/div")\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button")\
            .click()
        sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
    def give_likes(self, url):
        self.driver.get(url)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")\
            .click()
    def like_picture(self, url):
        self.driver.get(url)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")\
            .click()
    def write_comment(self, url, text):
        self.driver.get(url)
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button")\
            .click()
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[1]")\
            .send_keys(text)

if __name__ =='__main__':

    profileName="exampleName"
    password="I do not show you my password"
    instabot=InstaBot(profileName,password)
    instabot.like_picture("https://www.instagram.com/p/CKl4zQ3lKCl/")
    instabot.write_comment("https://www.instagram.com/p/CKl4zQ3lKCl/"," Nice\n")
