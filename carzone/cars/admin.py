from django.contrib import admin
from django.utils.html import format_html

from .models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src={} width="40" style="border-radius: 50px;"/>'.format(object.car_photo.url))

    thumbnails.short_description = 'Photo'
    list_display =  ('thumbnails','car_title' , 'model', 'condition', 'body_style', 'is_featured' )
    list_display_links = ('thumbnails','car_title')
    list_filter = ('condition','fuel_type','city','body_style','color')
    search_fields = ('car_title', 'year', 'model', 'body_style',)

admin.site.register(Car, CarAdmin)