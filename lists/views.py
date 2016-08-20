from django.shortcuts import render, redirect

from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':    
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the_only_list_in_the_world')

    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})
