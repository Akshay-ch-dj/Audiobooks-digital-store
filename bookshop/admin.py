from django.contrib import admin
from bookshop.models.book import Book, BookImages
from django.utils.html import format_html
# Custom filter
from .templatetags.my_filters import rupeeCommaInsert


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
    list_display = ('id', 'name', 'get_description',
                    'get_price', 'get_discount', 'get_finalPrice')
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

    def get_price(self, obj):
        return '₹ ' + rupeeCommaInsert(obj.price)

    def get_discount(self, obj):
        return str(obj.discount) + ' %'

    def get_finalPrice(self, obj):
        final = obj.price - (obj.price * (obj.discount/100))
        return '₹ ' + rupeeCommaInsert(int(final))

    # To change headers in the admin area
    get_description.short_description = 'Description'
    get_price.short_description = 'Sale Price'
    get_discount.short_description = 'Discount'
    get_finalPrice.short_description = 'Final Price'


# Register your models here.
admin.site.register(Book, BookAdmin)
# For inlines no need to register separately
# admin.site.register(BookImages, BookImageAdmin)
