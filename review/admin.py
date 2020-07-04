from django.contrib import admin
from .models import Restaurant,Dish,Review,ReviewImage,Video,Vlog,Blog,Recipe,Model
# ,Test
# Register your models here.

# admin
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(ReviewImage)
admin.site.register(Video)
admin.site.register(Vlog)
admin.site.register(Blog)
admin.site.register(Recipe)
# user
admin.site.register(Model)
