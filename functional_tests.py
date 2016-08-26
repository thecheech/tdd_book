from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # enter the site
        self.browser.get('http://127.0.0.1:8000')
        self.browser.implicitly_wait(3)

        # we check the title
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # other stuff...

    if __name__ == '__main__':
        unittest.main(warnings='ignore')