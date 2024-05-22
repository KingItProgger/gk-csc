from django.contrib import admin
from .models import Flat,House,News,Review,Room
# Register your models here.
class FlatAdmin(admin.ModelAdmin):
    list_display = ('house','square','rooms','amount','plan','price')
    list_display_links = ('house','square','rooms','amount','plan','price')
    search_fields = ('rooms','square')

admin.site.register(Flat,FlatAdmin)
admin.site.register(House)
admin.site.register(News)
admin.site.register(Review)
admin.site.register(Room)

