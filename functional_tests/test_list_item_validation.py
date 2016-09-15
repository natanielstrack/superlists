from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and acidentally tries to submit
        # an empty list item. She hits enter on the empty input box
        self.browser.get(self.server_url)
        input_element = self.get_item_input_box().send_keys('\n')

        # THe homepage refreshes and there is an error message
        # saying that list items cannot be empty
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She ties again with some text for the item, which now works
        input_element = self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, she now decides to submit a second blank list item
        input_element = self.get_item_input_box().send_keys('\n')

        # She receives a similar warning on the list page
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she correct it by filling some text in
        input_element = self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')


    def test_error_messages_are_cleared_on_input(self):
        # Edith starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typing in the input box  to clear the error
        self.get_item_input_box().send_keys('a')

        # She is pleased to see that the error message disapears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())