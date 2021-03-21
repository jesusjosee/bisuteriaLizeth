from django.contrib import admin
from .models import Women, Men, Couple
from about.models import About
# Register your models here.

class WomenConfig(admin.ModelAdmin):
    readonly_fields= ['created', 'updated']
    search_fields = ['title', ]
    list_display= ['title' , 'created']
    list_filter = ['created',]



admin.site.register(Women, WomenConfig)
admin.site.register(Men, WomenConfig)
admin.site.register(Couple, WomenConfig)
admin.site.register(About, WomenConfig)

