from django.contrib import admin
from .models import apiModel
# Register your models here.


class adminClass(admin.ModelAdmin):
    list_display = ['prj_id','prj_name','prj_amt','prj_location']

admin.site.register(apiModel,adminClass)