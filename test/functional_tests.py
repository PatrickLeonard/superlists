from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(firefox_binary=FirefoxBinary(
    firefox_path='C:\\Program Files\\Mozilla Firefox-ESR\\firefox.exe'
))
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_cosplay_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( row_text, [row.text for row in rows])
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Sally heard about a cool cosplay page and wanted to check out its
        #homepage
        self.browser.get('http://localhost:8000')

        #She notieces the page title and header mentions Off The Rails Cosplay
        self.assertIn('Off the Rails Cosplay' , self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Off the Rails Cosplay', header_text)

        #She is invited to enter a Cosplay Costume right away
        inputbox = self.browser.find_element_by_id('id_new_cosplay_name')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter cosplay name'
        )

        #She types the name of the costume, type of media, group pairing (link),
        #where/when it was worn at, the 'Off the Rails Factor', and then a large
        #description of the cosplay.
        inputbox.send_keys('Some Cosplay')

        #When she hits enter the page updates and now displays the information
        #for that cosplay
        inputbox.send_keys(Keys.ENTER)        

        self.check_for_row_in_list_table('1: Some Cosplay')
        #A text box invite another addition of a cosplay
        
        #She enters the cosplay paired with the first
        inputbox = self.browser.find_element_by_id('id_new_cosplay_name')
        inputbox.send_keys('Another crappy cosplay')
        inputbox.send_keys(Keys.ENTER)
        #She hits enter and the information about the second cosplay is displayed
        self.check_for_row_in_list_table('1: Some Cosplay')
        self.check_for_row_in_list_table('2: Another crappy cosplay')

        #Sally wonders whether the site will remember her cosplays, then notices the
        #site has generated a unique URL for here -- and lets her know about it
        self.fail('Finish the test!')
        #She visits that URL - and her list of Cosplays are there.

        #Satisfied show goes to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
