from django.shortcuts import render, redirect

from .models import Stamp, Category

# Create your views here.

def collection(request):
    category = request.GET.get('category')

    if category == None:
        stamps = Stamp.objects.all()
    else:
        stamps = Stamp.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {'categories': categories, 'stamps': stamps}

    return render(request, 'stamps/collection.html', context)

def new_stamp(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('stamp')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['new_category'] != '':
            category, created = Category.objects.get_or_create(name=data['new_category'])
        else:
            raise ValueError("Category can't be empty")

        stamp = Stamp.objects.create(
            category = category,
            name = data['name'],
            description = data['description'],
            image = image
        )

        return redirect('collection')
    
    context = {'categories': categories}

    return render(request, 'stamps/new_stamp.html', context)

def delete_stamp(request, pk, category):
    if request.method == 'POST':
        stamp = Stamp.objects.get(id=pk)
        stamp.delete()

        try:
            stamps_left = Stamp.objects.get(category=Category.objects.get(name=category))
        except Stamp.DoesNotExist:
            category_to_be_deleted = Category.objects.filter(name=category)
            category_to_be_deleted.delete()

    return redirect('collection')


def stamp(request, pk):
    stamp = Stamp.objects.get(id=pk)

    return render(request, 'stamps/stamp.html', {'stamp': stamp})
