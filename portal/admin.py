from django.contrib import admin
from portal.models import Contact, Budget

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
 pass
admin.site.register(Contact,ContactAdmin)

class BudgetAdmin(admin.ModelAdmin):
 pass
admin.site.register(Budget,BudgetAdmin)