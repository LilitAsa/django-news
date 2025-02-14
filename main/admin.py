from django.contrib import admin

from .models import (
  Category,
  Post,
  Tag,
)

class PostAdmin(admin.ModelAdmin):
    populated_fields = {'slug': ('title_en',)}
    
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)  