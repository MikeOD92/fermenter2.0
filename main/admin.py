from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(RecipeImg)
admin.site.register(CustomUser)
admin.site.register(Friend_Request)
