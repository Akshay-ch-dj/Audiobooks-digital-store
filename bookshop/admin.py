from django.contrib import admin
from bookshop.models.book import Book, BookImages
from django.utils.html import format_html


# To get the BookImage model inline with the Book.
class BookImageAdmin(admin.StackedInline):
    """Customization for the Book image table
    """
    model = BookImages


class BookAdmin(admin.ModelAdmin):
    """Customize the book table in admin
    """
    # Specify the inline admin class
    inlines = [BookImageAdmin]
    search_fields = ('name', 'description', 'price', 'discount', 'fileSize')
    list_display = ('id', 'name', 'get_description', 'price', 'discount')
    list_display_links = ('id', 'name')
    list_filter = ('discount',)

    def get_description(self, obj):
        """To truncate the description in the list display in admin panel

        Args:
            obj (Book object): passed the call itself

        Returns:
            text: shortened description
        """
        return format_html(f'<span title=\"{obj.description}\">\
                           {obj.description[0:15]}... </span>')


# Register your models here.
admin.site.register(Book, BookAdmin)
# For inlines no need to register separately
# admin.site.register(BookImages, BookImageAdmin)
