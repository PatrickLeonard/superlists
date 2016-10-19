from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Sally goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes and there is an error message saying
        # that list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Some Cosplay\n')
        self.check_for_row_in_list_table('1: Some Cosplay')
        
        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')


        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Some Cosplay')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.get_item_input_box().send_keys('Another crappy cosplay\n')
        self.check_for_row_in_list_table('1: Some Cosplay')
        self.check_for_row_in_list_table('2: Another crappy cosplay')


    def test_cannot_add_duplicate_items(self):
        # Sally goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy foam\n')
        self.check_for_row_in_list_table('1: Buy foam')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy foam\n')

        # She sees a helpful error message
        self.check_for_row_in_list_table('1: Buy foam')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")
        
        self.get_item_input_box().send_keys('Buy foam\n')

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_error_messages_are_cleared_on_input(self):
        # Sally starts a new list in a way that causes a validation error:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())


        # She starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # She is pleased to see that the error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
