import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class PostTest(unittest.TestCase):
    def setUp(self):
        self.element_addresses = {
            'list': {
                'title': '/html/body/div/div/div[2]/div/a[1]/div/div/div[1]/h3',
                'date': '/html/body/div/div/div[2]/div/a[1]/div/div/div[1]/p',
                'start_text': '/html/body/div/div/div[2]/div/a[1]/div/div/div[2]/p'
            },
            'post': {
                'title': '/html/body/div/div/div[2]/div/div/div[1]/div/h3',
                'date': '/html/body/div/div/div[2]/div/div/div[1]/div/p',
                'start_text': '/html/body/div/div/div[2]/div/div/div[2]/p[1]'               
            }
        }
        self.blogTitle = 'Blog'
        self.blogTitleAddress = '/html/body/div/div/div[1]/div/h1'
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:3000/')
        self.action = ActionChains(self.driver)
        sleep(3)

    def test_check_main_page(self):
        site = self.driver.find_element(By.XPATH, self.blogTitleAddress)
        self.assertEqual(site.text, self.blogTitle)

    def test_first_post_access(self):
        list_of_elements = {
            'list': [],
            'post': []
        }
        self.action.move_to_element(self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/a[1]/div')).perform()
        sleep(3)
        self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/a[1]/div')

        for address in self.element_addresses['list']:
            site = self.driver.find_element(By.XPATH, self.element_addresses['list'][address])
            list_of_elements['list'].append(site.text)

        self.driver.find_element(By.XPATH, self.element_addresses['list']['title']).click()
        sleep(3)

        for second_address in self.element_addresses['post']:
            site = self.driver.find_element(By.XPATH, self.element_addresses['post'][second_address])
            list_of_elements['post'].append(site.text)

        self.assertEqual(len(list_of_elements['list']), len(list_of_elements['post']))
        self.assertListEqual(list_of_elements['list'], list_of_elements['post'])

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
