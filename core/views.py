from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

from django.contrib.auth import logout
from django.contrib import messages

def index(request):
    # Retrieve up to 6 unsold items from the database
    items = Item.objects.filter(is_sold=False)[0:6]

    # Retrieve all categories from the database
    categories = Category.objects.all()

    # Render the 'core/index.html' template with the following context data:
    # - 'categories': All categories
    # - 'items': Up to 6 unsold items
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('/')