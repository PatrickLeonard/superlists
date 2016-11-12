from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        #Sally heard about a cool cosplay page and wanted to check out its
        #homepage
        self.browser.get(self.server_url)

        #She notices the page title and header mentions SuperLists
        self.assertIn('To-Do lists' , self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new To-Do list', header_text)

        #She is invited to enter a Cosplay Costume right away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
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
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Another crappy cosplay')
        inputbox.send_keys(Keys.ENTER)
        #She hits enter and the information about the second cosplay is displayed
        self.check_for_row_in_list_table('1: Some Cosplay')
        self.check_for_row_in_list_table('2: Another crappy cosplay')

        ##We use a new browser session to make sure that no information
        ##of Sally's is coming through from cookies, etc.
        self.browser.quit()
        self.browser =  webdriver.Chrome()

        #Francis visits the home page. There is no sign of Sally's
        #list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Some Cosplay', page_text)
        self.assertNotIn('Another crappy cosplay', page_text)

        #Francis starts a new list by entering a new item He
        #doesn't cosplay.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url,sally_list_url)

        #Again, there is no trace of Sally's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Some Cosplay', page_text)
        self.assertNotIn('Another crappy cosplay', page_text)
