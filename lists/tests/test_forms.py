from django.test import TestCase

from lists.forms import ItemForm

class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        html_source = form.as_p()

        self.assertIn('placeholder="Enter a to-do item"', html_source)
        self.assertIn('class="form-control input-lg"', html_source)
