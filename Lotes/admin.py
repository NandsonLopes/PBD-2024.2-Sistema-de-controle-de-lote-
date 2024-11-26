from django.contrib import admin

# Register your models here.
from .models import Development, DevelopmentImage

class DevelopmentImageInline(admin.TabularInline):
    model = DevelopmentImage
    extra = 1

@admin.register(Development)
class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_lots', 'total_available', 'address')
    inlines = [DevelopmentImageInline]
