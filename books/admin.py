from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', )