from django.shortcuts import render,redirect,get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.
def homepage(request):
    # 1. Fetch all data of book from database
    books = Book.objects.all()
    # print(books)

    # 2. Send all fetched data to a template
    return render(request,'book_list.html',{'books':books})



def add_book(request):
    if request.method == 'POST':
        # when click save button
        # Get the all data from frontend
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        print("Get the form")
        form = BookForm()
        return render(request,'add_book.html',{'form':form})
    
def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if book:
        book.delete()
    
    return redirect('homepage')

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form})