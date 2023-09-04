from django.contrib import admin
from library import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Reader)
admin.site.register(models.IssuedBook)