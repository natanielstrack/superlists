from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import List, Item

class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        saved_list =  List.objects.first()
        self.assertEqual(list_, saved_list)

        first_item = Item()
        first_item.text = 'First item (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'First item (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_save_empty_list_item(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')

        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()