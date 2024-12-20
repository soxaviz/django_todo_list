from django.contrib import admin
from .models import Todo, HomeSlider, Category, TodoGallery


class PostGalleryAdmin(admin.StackedInline):
    model = TodoGallery
    min_num = 1
    max_num = 3



class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    inlines = [PostGalleryAdmin]



admin.site.register(Category)
admin.site.register(HomeSlider)
admin.site.register(Todo, PostAdmin)
