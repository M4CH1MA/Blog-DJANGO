from django.contrib import admin
from django.http import HttpRequest
from site_setup.models import MenuLink, SiteSetup

# Register your models here.

class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInline,

    #metodo para ver se ja tem 1 registo no admin do django
    def has_add_permission(self, request):
        return not SiteSetup.objects.all()[:1].exists()
