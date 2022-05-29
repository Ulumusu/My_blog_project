import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class PostResume(unittest.TestCase):
    def setUp(self):
        self.navMenu = '/html/body/div/div/div[1]/div/div/a'
        self.resumeButton = '/html/body/div/div/div[1]/div/nav/ul/li[5]/a'
        self.postButton = '//*[@id="root"]/div/div[1]/div/nav/ul/li[3]/a'
        self.address = {
            'contact': '//*[@id="root"]/div/div[2]/div/div/div[1]/h4',
            'linkedin': '//*[@id="root"]/div/div[2]/div/div/div[1]/p[2]',
            'experience': '//*[@id="root"]/div/div[2]/div/div/div[2]/h3',
            'education': '//*[@id="root"]/div/div[2]/div/div/div[3]/h3',
            'certificates': '//*[@id="root"]/div/div[2]/div/div/div[4]/h3',
            'hobby': '//*[@id="root"]/div/div[2]/div/div/div[5]/h3'
            }
        self.checking = [
            'Kontakt:', 'LinkedIn', 'Doświadczenie', 
            'Edukacja', 'Certyfikaty', 'Hobby'
            ]
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:3000/')
        sleep(3)

    def test_get_access_to_resume(self):
        site = self.driver.find_element(By.XPATH, self.navMenu)
        site.click()
        sleep(3)
        resume = self.driver.find_element(By.XPATH, self.resumeButton)
        resume.click()
        sleep(3)
    
    def test_check_information_on_resume_page(self):
        list_of_elements = []
        site = self.driver.find_element(By.XPATH, self.navMenu)
        site.click()
        sleep(3)
        resume = self.driver.find_element(By.XPATH, self.resumeButton)
        resume.click()
        sleep(3)

        for a in self.address:
            site = self.driver.find_element(By.XPATH, self.address[a])
            list_of_elements.append(site.text)
            
        self.assertEqual(len(list_of_elements), len(self.checking))
        self.assertListEqual(list_of_elements, self.checking)
        
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