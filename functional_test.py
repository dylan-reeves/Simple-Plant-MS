from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from autofixture import AutoFixture
#from sites.models import site
import unittest

#Test to check all functionality of the sites apps
#Simple plant maintenance application administrator Dylan will be creating,
#editing and deleting sites in order to configure the application
class TestSiteApp(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        #site.objects.all().delete()

    def tearDown(self):
        self.browser.quit()

    def test_create_a_site(self):
        #Just check that the page loads
        self.browser.get('http://127.0.0.1:8000/sites/')
        self.assertIn('INDEXPAGE', self.browser.title)
        #Check that there are currently no site items displayed on the page
        
        self.fail('Finish the Test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
