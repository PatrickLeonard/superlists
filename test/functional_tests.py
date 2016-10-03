from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
    firefox_path='C:\\Program Files\\Mozilla Firefox-ESR\\firefox.exe'
))
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Sally heard about a cool cosplay page and wanted to check out its
        #homepage
        self.browser.get('http://localhost:8000')

        #She notieces the page title and header mentions Off The Rails Cosplay
        self.assertIn('Off The Rails Cosplay' , self.browser.title)
        self.fail('Finish the test!')

        #She is invited to enter a Cosplay Costume right away

        #She types the name of the costume, type of media, group pairing (link),
        #where/when it was worn at, the 'Off the Rails Factor', and then a large
        #description of the cosplay.


        #When she hits enter the page updates and now displays the information
        #for that cosplay

        #A text box invite another addition of a cosplay

        #She enters the cosplay paired with the first

        #She hits enter and the information about the second cosplay is displayed

        #Sally wonders whether the site will remember her cosplays, then notices the
        #site has generated a unique URL for here -- and lets her know about it

        #She visits that URL - and her list of Cosplays are there.

        #Satisfied show goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
