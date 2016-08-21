from django.shortcuts import render, redirect, HttpResponse

from lists.models import List, Item

# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def new_list(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']

        list_ = List.objects.create()
        Item.objects.create(text=new_item_text, list=list_)

        return redirect('/lists/%d/' % (list_.id,))


def view_lists(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list':list_})


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    new_item_text = request.POST['item_text']
    item = Item.objects.create(text=new_item_text,list=list_)

    return redirect('/lists/%d/' % (list_.id,))