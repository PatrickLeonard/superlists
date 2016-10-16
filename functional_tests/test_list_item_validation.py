from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        # Sally goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        # The home page refreshes and there is an error message saying
        # that list items cannot be blank
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Items cannot be blank', page_text)

        # She tries again with some text for the item, which now works
        inputbox.send_keys('Some Cosplay')
        inputbox.send_keys(Keys.ENTER)

        # Perversely, she now decides to submit a second blank list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        # She receives a similar warning on the list page
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Items cannot be blank', page_text)

        # And she can correct it by filling some text in
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Another crappy cosplay')
        inputbox.send_keys(Keys.ENTER)
