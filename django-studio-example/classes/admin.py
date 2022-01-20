from django.contrib import admin
from .models import DanceClass, User, Style, Teacher

admin.site.register(User)
admin.site.register(DanceClass)
admin.site.register(Style)
admin.site.register(Teacher)