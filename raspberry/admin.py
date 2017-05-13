from django.contrib import admin
from .models import detail

# Register your models here.
class DetailAdmin(admin.ModelAdmin):
	list_display = ['time', 'temperature', 'humidity', 'is_pan_turn']

admin.site.register(detail,DetailAdmin)
