from django.contrib import admin
from .models import Listing, Inquiry
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor']
    list_display_links = ['id', 'title']
    list_filter = ['realtor__name']
    list_editable = ['is_published']
    search_fields = ['title', 'description', 'address', 'city', 'state', 'zip_code', 'price']
    list_per_page = 25

    class Meta:
    	model = Listing

admin.site.register(Listing, ListingAdmin)


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['listing', 'user', 'phone']

    class Meta:
    	model = Inquiry

admin.site.register(Inquiry, InquiryAdmin)
