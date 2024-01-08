from django.shortcuts import render, get_object_or_404, redirect
from .middleware import CategoryMiddleware
from django.contrib import messages
from .forms import CategoryForm
from ..models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'finance_tracking/category/list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'finance_tracking/category/detail.html', {'category', category})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            CategoryMiddleware.create_category(request, form)
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'finance_tracking/category/create.html', {'form': form, 'action': 'create'})

def update_review(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            CategoryMiddleware.update_category(request, form, category.pk)
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'finance_tracking/category/update.html', {'form': form, 'action': 'update', 'category': category})

def delete_review(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        CategoryMiddleware.delete_category(request, category)
        return redirect('category-list')
    return render(request, 'finance_tracking/category/delete.html', {'category': category})
    