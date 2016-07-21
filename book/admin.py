from django.contrib import admin
from .models import Author, Books, Category


admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Category)
