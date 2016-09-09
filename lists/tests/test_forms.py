from django.test import TestCase

from lists.models import Item, List
from lists.forms import ItemForm, EMPTY_ITEM_ERROR

class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        html_source = form.as_p()

        self.assertIn('placeholder="Enter a to-do item"', html_source)
        self.assertIn('class="form-control input-lg"', html_source)


    def test_validation_form_for_blank_items(self):
        form = ItemForm(data={'text_item':'',})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [EMPTY_ITEM_ERROR]
        )


    def test_form_save_handles_saving_to_list(self):
        list_ = List.objects.create()        
        form = ItemForm(data={'text':'do me'})
        new_item = form.save(for_list=list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, 'do me')
        self.assertEqual(new_item.list, list_)
