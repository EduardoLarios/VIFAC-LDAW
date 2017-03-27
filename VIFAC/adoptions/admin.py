from django.contrib import admin
from .models.families import Family
from .models.fathers import Father
from .models.mothers import Mother

admin.site.register(Family)
admin.site.register(Father)
admin.site.register(Mother)

