from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class Author(models.Model):
    name = models.CharField(
        verbose_name="Author's name",
        max_length=256)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/success'

class Book(models.Model):
    picture = models.ImageField(
        verbose_name='Картинка',
        upload_to='uploads/%Y/%m/%d/'
    )
    name = models.CharField(
        verbose_name="Название книги",
        max_length=256)
    author = models.ForeignKey(
        Author,
        verbose_name="Автор",
        default='-',
        on_delete=models.CASCADE)
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=256)
    available = models.BooleanField(
        verbose_name="В наличии",
        default=True)

    def __str__(self):
        return f'{self.name} ({self.isbn})'
    
    def get_absolute_url(self):
        return '/success'

class Reader(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name="User",
        on_delete=models.CASCADE)
    full_name = models.CharField(
        verbose_name="Full name",
        max_length=256)
    phone = models.CharField(
        verbose_name="Phone number",
        max_length=32, 
        blank=True)

    def __str__(self):
        return self.full_name

def expiry():
    return datetime.today() + timedelta(days=14)

class IssuedBook(models.Model):
    reader = models.CharField(
        max_length=100, 
        blank=True) 
    isbn = models.CharField(
        max_length=32)
    issued_date = models.DateField(
        auto_now_add=True)
    expiry_date = models.DateField(
        default=expiry)
    
    def get_absolute_url(self):
        return '/success'