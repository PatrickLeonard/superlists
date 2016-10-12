from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

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
        self.browser.get(self.live_server_url)

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
        sally_list_url = self.browser.current_url
        self.assertRegex(sally_list_url, 'lists/.+')
        self.check_for_row_in_list_table('1: Some Cosplay')
        #A text box invite another addition of a cosplay
        
        #She enters the cosplay paired with the first
        inputbox = self.browser.find_element_by_id('id_new_cosplay_name')
        inputbox.send_keys('Another crappy cosplay')
        inputbox.send_keys(Keys.ENTER)
        #She hits enter and the information about the second cosplay is displayed
        self.check_for_row_in_list_table('1: Some Cosplay')
        self.check_for_row_in_list_table('2: Another crappy cosplay')

        ##We use a new browser session to make sure that no information
        ##of Sally's is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page. There is no sign of Sally's
        #list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Some Cosplay', page_text)
        self.assertNotIn('Another crappy cosplay', page_text)

        #Francis starts a new list by entering a new item He
        #doesn't cosplay.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.asertNotEqual(francis_list_url,sally_list_url)

        #Again, there is no trace of Sally's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Some Cosplay', page_text)
        self.assertNotIn('Another crappy cosplay', page_text)

        #Satisfied they both go back to sleep
        self.fail('Hit the Self fail!')

