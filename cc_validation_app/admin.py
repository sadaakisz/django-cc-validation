from django.contrib import admin

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ["number", "expires", "valid_card", "issuing_network"]

# Register your models here.
admin.site.register(Card, CardAdmin)