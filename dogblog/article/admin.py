from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Article, Category, ViewCount

admin.site.register(Article)


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'id', 'title', 'slug')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'parent')}),
        ('Описание', {'fields': ('description',)})
    )


@admin.register(ViewCount)
class ViewCountAdmin(admin.ModelAdmin):
    pass
