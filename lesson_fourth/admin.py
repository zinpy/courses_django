from django.contrib import admin
from . import models

admin.site.register(models.Example)

# admin.site.register(models.Author)
# admin.site.register(models.Book)

admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)

admin.site.register(models.Publication)
admin.site.register(models.Article)


class AuthorAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.Author._meta.fields]

    # list_display = ['name', 'surname']
    list_display = all_fields
    # list_display.remove('id')
    # list_display_links = all_fields
    list_editable = ['name', 'surname', 'date_birth']

    # exclude = ["name"]  # прячет поле
    # fields = ["name", 'surname']  # показывает поле

    list_filter = ['name', 'surname']
    # search_fields = ['name', 'surname']
    search_fields = all_fields

    # class Meta:
    #     model = models.Author


admin.site.register(models.Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):

    list_display = ['title', 'text', 'genre', 'get_author_name']

    def get_author_name(self, obj):
        return obj.author.name
    get_author_name.short_description = 'Автор'


admin.site.register(models.Book, BookAdmin)
