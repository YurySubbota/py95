from django.contrib import admin
from catalog.models import Author, Genre, Language, Book, BookInstance, Country


# Register your models here.

class BookInline(admin.TabularInline):
    model = Book


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'pseudonym')
    search_fields = ('first_name', 'last_name', 'pseudonym')
    inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    search_fields = ('title', 'author__pseudonym', 'author__first_name', 'author__last_name', 'genre__name')
    inlines = [BookInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'isbn', 'status')
    fieldsets = (
        ('Group 1', {'fields': ('book', 'isbn', 'language')}),
        ('Group 2', {'fields': ('borrower', 'due_back', 'status')})
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
