"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from library import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",  views.LoginView.as_view(), name="login"),
    path("success/",  views.success, name="success"),
    path("add_books/", views.BookCreateView.as_view(), name="add_books"),
    path("update_book/<int:pk>/", views.BookUpdateView.as_view(), name="update_book"),
    path("admin_book/", views.BookListView.as_view(), name="admin_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("reader_issued_book/", views.reader_issued_books, name="reader_issued_book"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("profile/", views.profile, name="profile"),

    path("reader_registration/", views.reader_registration, name="reader_registration"),
    path("logout/", views.LogoutView.as_view(), name="logout"),

    path("delete_book/<int:pk>/", views.BookDeleteView.as_view(), name="delete_book"),
    path("delete_issue_book/<int:pk>/", views.IssuedBookDeleteView.as_view(), name="delete_issued_book"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)