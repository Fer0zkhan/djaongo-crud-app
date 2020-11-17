from django.shortcuts import render, redirect, get_object_or_404
from .models import BookModel
from .forms import BookModelForm
from .tables import BookModelTable
from django.urls import reverse


def home(request):
    book = BookModel.objects.all()
    sort = request.GET.get('sort', None)
    if sort:
        book = book.order_by(sort)
    table = BookModelTable(book)
    context = {
        'title': 'Book',
        'data_exits': book,
        'table': table,
        'home_page_url': reverse('index'),
        'add_page_url': reverse('add_book')
    }
    return render(request, 'home.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_home')
    else:
        form = BookModelForm()
    context = {
        'title': 'Add New Book',
        'form': form,
        'dashBoard_url': reverse('books_home')
    }

    return render(request, 'add-edit-form.html', context)


def edit_book(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_home')
    else:
        form = BookModelForm(instance=book)
    context = {
        'title': 'Edit Book',
        'form': form,
        'dashBoard_url': reverse('books_home')
    }

    return render(request, 'add-edit-form.html', context)


def delete_book(request, pk):
    book = get_object_or_404(BookModel, pk=pk)
    book.delete()
    return redirect('books_home')
