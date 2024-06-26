from django.contrib import admin
from django.utils.html import format_html

from .models import Team

class TeamAdmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src={} width="40" style="border-radius: 50px;"/>'.format(object.photo.url))

    thumbnails.short_description = 'Photo'
    list_display = ('id','thumbnails' , 'first_name', 'last_name', 'designation', 'create_date' )
    list_display_links = ('id', 'thumbnails')
    list_filter = ('designation',)
    search_fields = ('first_name', 'last_name', 'designation')

admin.site.register(Team, TeamAdmin)
