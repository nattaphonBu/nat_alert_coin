from django.contrib import admin
from .models import AlertCoin # add this

class AlertCoinAdmin(admin.ModelAdmin):  # add this
  list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(AlertCoin, AlertCoinAdmin) # add this