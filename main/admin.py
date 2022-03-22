from django.contrib import admin
from .models.recipe_models import *
# from .models.user_models import *

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(RecipeImg)
