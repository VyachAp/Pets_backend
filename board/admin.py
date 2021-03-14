from django.contrib import admin
from .models import PetSubcategory, PetCategory, Post, ImagesPost

admin.site.register(PetCategory)
admin.site.register(PetSubcategory)
admin.site.register(Post)
admin.site.register(ImagesPost)
