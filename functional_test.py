from selenium import webdriver
import unittest

class TestSiteApp(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

#Test main site page loads
    def tearDown(self):
        self.browser.quit()

    def test_create_a_site(self):
        self.browser.get('http://127.0.0.1:8000/sites/')
        self.assertIn('INDEXPAGE', self.browser.title)
        self.fail('Finish the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
