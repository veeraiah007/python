from django.contrib import admin
from .models  import *
# Register your models here.
'''class catagoryAdmin(admin.ModelAdmin):
    list_display=('name', 'image', 'description')
admin.site.register(catagory,catagoryAdmin)'''

admin.site.register(Catagory)
admin.site.register(product)
