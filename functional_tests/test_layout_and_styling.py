from .base import FunctionalTest
from .home_and_list_pages import HomePage

class LayoutAndStylingTest(FunctionalTest):
    
    def test_center_input_box_on_home_page(self):
        #Sally goes to the home page
        #She she notices the input box is nicely centered
        self.browser.set_window_size(1024,768)
        inputbox = HomePage(self).go_to_home_page().get_item_input()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

    def test_center_input_box_on_list_page(self):
        #Sally goes to the home page and starts a new list
        #She she notices the input box is nicely centered on the list page
        self.browser.set_window_size(1024,768)
        list_page = HomePage(self).start_new_list('testing')
        inputbox = list_page.get_item_input()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
