from django.contrib import admin

from .models import Category, Choice, Question

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)
