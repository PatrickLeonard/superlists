from .base import FunctionalTest
from selenium import webdriver
from .home_and_list_pages import HomePage
from unittest import skip

def quit_if_possible(browser):
    try: browser.quit()
    except: pass

class SharingTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Sally is a logged-in user
        self.create_pre_authenticated_session('sally@example.com')
        sally_browser = self.browser
        self.addCleanup(lambda: quit_if_possible(sally_browser))

        # Her friend Oniciferous is also hanging out on the lists site
        oni_browser = webdriver.Firefox()
        self.browser = oni_browser
        self.addCleanup(lambda: quit_if_possible(oni_browser))
        self.create_pre_authenticated_session('oniciferous@example.com')
        
        # Sally goes to the home page and starts a list
        self.browser = sally_browser
        list_page = HomePage(self).start_new_list('Get help')

        # She notices a "Share this list" option
        share_box = list_page.get_share_box()
        self.assertEqual(
                share_box.get_attribute('placeholder'),
                'your-friend@example.com'
            )

        # She shares her list
        # The page updates to say that it's shared with Oniciferous:
        list_page.share_list_with('oniciferous@example.com')
        
        # Oniciferous now goes to the lists page with his browser
        self.browser = oni_browser
        HomePage(self).go_to_home_page().go_to_my_lists_page()

        # He sees Sally's list in there!
        self.browser.find_element_by_link_text('Get help').click()
        
        # On the list page, Oniciferous can see that it's Sally's list
        self.wait_for(lambda: self.assertEqual(
            list_page.get_list_owner(),
            'sally@example'
        ))

        # He adds an item to the list
        list_page.add_new_item('Hi Sally!')

        # When Sally refreshers the page, she sees Oniciferous' addition
        self.browser = sally_browser
        self.browser.refresh()
        list_page.wait_for_new_item_in_list('Hi Sally!',2)
