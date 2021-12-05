from django.contrib import admin
from .models import Banner
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_active', 'created_date')

admin.site.register(Banner, BannerAdmin)