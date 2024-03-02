from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from .models import Product, Client, Item, Order, Message, Subscriber, Image

class ImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 0
    readonly_fields = ['image_preview']

    def image_preview(self, instance):
        return format_html('<img src="{}" width="120" height="120" />', instance.image.src.url)

    image_preview.short_description = 'Image Preview'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'image_preview_list']
    fieldsets = (
        (None, {
            'fields': ('title', 'price', 'old_price', 'description', 'sold_out'),
        }),
    )

    def image_preview_list(self, obj):
        previews = []
        for image in obj.images.all():
            previews.append('<img src="{}" width="60" height="60" />'.format(image.src.url))
        return mark_safe(' '.join(previews))

    image_preview_list.short_description = 'Image Previews'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'date']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender_first_name', 'date']


admin.site.register(Item)
admin.site.register(Subscriber)
admin.site.register(Image)