from django.shortcuts import render, redirect, HttpResponse

from lists.models import List, Item

# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def view_lists(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items':items})


def new_list(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']

        list_ = List.objects.create()
        Item.objects.create(text=new_item_text, list=list_)

        return redirect('/lists/the-only-list-in-the-world/')

