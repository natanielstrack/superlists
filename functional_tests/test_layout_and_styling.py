from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

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