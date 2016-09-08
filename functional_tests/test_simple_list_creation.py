from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_later(self):
        # Edith has heard about a cool new online to-do app, so she goes to check out its homepage 
        self.browser.get(self.server_url)

        # Edith notes that the page title and header mention to-do lists
        """
        try:
            assert "To-Do" in browser.title, "Browser title was " + browser.title
        finally:
            browser.quit()
        """
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to make a to-do list right away
        input_box = self.get_item_input_box()
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "buy peacock feathers" into a textbox (Edith's hobby is tying fly-fishing lures)
        input_box.send_keys('buy peacock feathers')

        # When she hits enter, she is taken to a new URL,
        # and now the page lists 
        # "1: buy peacock feathers" as an item in a to-do list table
        input_box.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url

        self.assertRegexpMatches(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edity is very methodical)
        input_box = self.get_item_input_box()
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        input_box.send_keys('Use peacock feathers to make a fly')
        input_box.send_keys(Keys.ENTER)

        # The page updates again, and now shows both itens on her list
        self.check_for_row_in_list_table('1: buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Now a new user, Francis, comes along to the site

        ## We use a new browser's session, to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Francis visit the homepage, there's no sign of Edith's list
        self.browser.get(self.server_url)

        self.assertNotIn('buy peacock feathers', self.browser.page_source)
        self.assertNotIn('Use peacock feathers to make a fly', self.browser.page_source)

        # Francis starts a new list by entering a new item.
        # He's less interesting than Edith

        input_box = self.get_item_input_box()
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)

        # Francis gets his own URL
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there's no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go to sleep