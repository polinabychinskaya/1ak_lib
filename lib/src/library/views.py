from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from . import forms, models
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views import generic

def success(request):
    return render(request, "success.html")

def view_books(request):
    books = Book.objects.filter(available = True)
    return render(request, "view_books.html", {'books':books})

class BookListView(generic.ListView):
    model = models.Book
    template_name = 'all_books.html'

class BookCreateView(generic.CreateView):
    model = models.Book
    fields = [
        'picture', 'name', 'author', 'isbn', 'available'
    ]
    template_name = 'add_book.html'

class AuthorCreateView(generic.CreateView):
    model = models.Author
    fields = [
        'name'
    ]
    template_name = 'add_author.html'

class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = [
        'picture', 'name', 'author', 'isbn', 'available'
    ]
    template_name = 'update_book.html'

@login_required()
def issue_book(request):
    form = forms.IssueBookForm()
    if request.method == "POST":
        form = forms.IssueBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.reader = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.issued_date = datetime.today()
            borrowed_book = models.Book.objects.get(isbn = obj.isbn)
            borrowed_book.available = False
            borrowed_book.save()
            obj.save()
            alert = True
            return render(request, "issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issue_book.html", {'form':form})

def view_issued_book(request):
    borrowed = Book.objects.filter(available = False)
    return render(request, "view_issued_book.html", {'borrowed':borrowed})

@login_required(login_url = '/reader_login')
def profile(request):
    return render(request, "profile.html")

class IssuedBookDeleteView(generic.DeleteView):
    model = models.IssuedBook
    template_name = 'deleteissuedbook.html'
    success_url = '/success'

class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'deletebook.html'
    success_url = '/success'

def reader_issued_books(request):
    issuedBooks = IssuedBook.objects.all()
    issues = []
    for i in issuedBooks:
        books = list(models.Book.objects.filter(isbn=i.isbn))
        reader = list(models.Reader.objects.filter(user=request.user.id))
        i=0
        for t in books:
            t=(reader[i].user,reader[i].user_id,books[i].name,books[i].isbn,issuedBooks[i].issued_date,issuedBooks[i].expiry_date, issuedBooks[i].pk)
            i=i+1
            issues.append(t)
    return render(request,'reader_issues.html',{'issues':issues})


def reader_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        patronymic = request.POST['patronymic']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        student = Reader.objects.create(user=user, full_name=f"{last_name} {first_name} {patronymic}", phone=phone)
        user.save()
        student.save()
        alert = True
        return render(request, "reader_registration.html", {'alert':alert})
    return render(request, "reader_registration.html")

class LoginView(auth_views.LoginView):
    template_name = 'login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'logout.html'