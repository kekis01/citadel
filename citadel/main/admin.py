from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Comments)
admin.site.register(Article)