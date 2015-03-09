from django.contrib import admin
from portal.models import Contact, Budget, PodioConfig

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'city', 'state')
admin.site.register(Contact,ContactAdmin)

class BudgetAdmin(admin.ModelAdmin):
	list_display = ('contact', 'event_type', 'date', 'message')
admin.site.register(Budget,BudgetAdmin)

class PodioConfigAdmin(admin.ModelAdmin):
 pass
admin.site.register(PodioConfig,PodioConfigAdmin)