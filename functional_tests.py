from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_later(self):
        # Edith has heard about a cool new online to-do app, so she goes to check out its homepage 
        self.browser.get('http://localhost:8000')

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
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "buy peacock feathers" into a textbox (Edith's hobby is tying fly-fishing lures)
        input_box.send_keys('buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock fethers to make a fly" (Edity is very methodical)
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')

        input_box.send_keys('Use peacock fethers to make a fly')
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('2: Use peacock fethers to make a fly', [row.text for row in rows])

        # The page updates again, and now shows both itens on her list
        self.fail('Finish the test!')

        # Edith wonders whether the site will remember her list. Then she sees that the site has 
        # generated a unique URL for her -- there is some explanatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()