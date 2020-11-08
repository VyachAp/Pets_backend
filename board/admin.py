from django.contrib import admin
from .models import PetSubcategory, PetCategory, PostPets, PetsImageModel

admin.site.register(PetCategory)
admin.site.register(PetSubcategory)
admin.site.register(PostPets)
admin.site.register(PetsImageModel)
