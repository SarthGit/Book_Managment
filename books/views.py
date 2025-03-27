from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Ensure files are handled
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list after successful form submission
    else:
        form = BookForm()
    return render(request, 'books/book_add.html', {'form': form})

# New view to show details of a specific book, including file download link
def book_detail(request, pk):
    # Fetch the book by its primary key (id)
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect back to the book list after deletion
    return render(request, 'books/book_confirm_delete.html', {'book': book})