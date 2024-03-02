from django.contrib import admin

from .models import Product, Purchase, Lesson, Group, GroupMembership

admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Lesson)
admin.site.register(Group)
admin.site.register(GroupMembership)
