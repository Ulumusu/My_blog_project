import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class aboutMeResume(unittest.TestCase):
    def setUp(self):
        self.navMenu = '/html/body/div/div/div[1]/div/div/a'
        self.aboutMeButton = '//*[@id="root"]/div/div[1]/div/nav/ul/li[4]/a'
        self.postButton = '//*[@id="root"]/div/div[1]/div/nav/ul/li[3]/a'
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:3000/')
        sleep(3)

    def test_get_access_to_about(self):
        site = self.driver.find_element(By.XPATH, self.navMenu)
        site.click()
        sleep(3)
        resume = self.driver.find_element(By.XPATH, self.aboutMeButton)
        resume.click()
        sleep(3)
     
    def tearDown(self):
        site = self.driver.find_element(By.XPATH, self.navMenu)
        site.click()
        sleep(3)
        site = self.driver.find_element(By.XPATH, self.postButton)
        site.click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()