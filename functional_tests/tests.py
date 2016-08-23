import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super(NewVisitorTest, cls).setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super(NewVisitorTest, cls).tearDownClass()    


    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


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
        input_box = self.browser.find_element_by_id('id_new_item')
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
        input_box = self.browser.find_element_by_id('id_new_item')
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

        input_box = self.browser.find_element_by_id('id_new_item')
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


    def test_layout_and_styling(self):
        # Edith goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notes that the box is nicely centered
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(input_box.location['x']+input_box.size['width']/2, 512, delta=5)

        # She starts a new list e sees the input is nicely centered here too
        input_box.send_keys('testing\n')
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(input_box.location['x']+input_box.size['width']/2, 512, delta=5)
