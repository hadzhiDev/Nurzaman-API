from django.contrib import admin

from .models import Apartment, Block, Object, ObjectImage

class BlockInline(admin.StackedInline):
    model = Block
    extra = 2

class ObjectImageInline(admin.TabularInline):
    model = ObjectImage
    extra = 1


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    inlines = [BlockInline, ObjectImageInline]


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'object', 'floors_count')
    search_fields = ('name', 'object__name')
    list_filter = ('floors_count',)


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'rooms_count', 'area')
    search_fields = ('number', 'floor')
    list_filter = ('rooms_count',)

