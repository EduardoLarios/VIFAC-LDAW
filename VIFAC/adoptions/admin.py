from django.contrib import admin
from .models.families import Family
from .models.members import Member

admin.site.register(Family)
admin.site.register(Member)
