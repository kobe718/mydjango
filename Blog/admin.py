from django.contrib import admin

# Register your models here.
from Blog.models import MyPost 

class MyPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')
    
admin.site.register(MyPost, MyPostAdmin)