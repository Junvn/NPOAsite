from django.contrib import admin
from npoa.models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    pass


admin.site.register(User)
admin.site.register(Article)

