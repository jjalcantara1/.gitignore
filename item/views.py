from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from item.forms import NewItemForm, EditItemForm
from item.models import Item, Category
from profile.models import Location


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    category = Category.objects.all()
    location_id = request.GET.get('location', 0)  # Get the selected location_id
    locations = Location.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if location_id:
        items = items.filter(created_by__profile__location_id=location_id)  # Filter by seller's location

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'category': category,
        'category_id': int(category_id),
        'location': locations,
        'location.id': int(location_id)
    })


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[0:3]
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, 'item/detail.html', context)


@login_required
def NewItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.pk)

    else:
        form = NewItemForm()

    return render(request, 'item/new_item.html', {
        'form': form,
        'title': 'New Item'
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return HttpResponseRedirect(reverse_lazy('dashboard:index_d'))

def EditItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.pk)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/new_item.html', {
        'form': form,
        'title': 'Edit Item'
    })
