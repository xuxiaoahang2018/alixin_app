from django.contrib import admin

# Register your models here.
from backstage.models import Test

class MyAdminSite(admin.AdminSite):
    site_header = "爱立信三十周年活动后台管理"


class TestAdmin(admin.ModelAdmin):
    list_display = ("name", "content", "admin_sample", "video")
    search_fields = ["name", "content"]
    list_per_page = 2


admin_site = MyAdminSite(name='爱立信')
# Register your models here.
admin_site.register(Test, TestAdmin)