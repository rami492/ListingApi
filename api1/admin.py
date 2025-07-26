from django.contrib import admin
from api1.models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'owner', 'created_at']

admin.site.register(Listing, ListingAdmin)