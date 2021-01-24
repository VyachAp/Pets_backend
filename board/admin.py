from django.contrib import admin
from .models import PetSubcategory, PetCategory, Post, Images

admin.site.register(PetCategory)
admin.site.register(PetSubcategory)
admin.site.register(Post)
admin.site.register(Images)
