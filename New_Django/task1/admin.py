from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Post)

# @admin.register(Buyer)
# class BuyerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'balance', 'age')
#     search_fields = ('name', )
#     list_filter = ('balance', 'age', )
#     fields = [('name', 'balance', 'age')]
#
# @admin.register(Game)
# class GameAdmin(admin.ModelAdmin):
#     list_display = ('title', 'cost', 'size', 'age_limited')
#     search_fields = ('title', )
#     list_filter = ('cost', 'size', 'age_limited', )
#     fieldsets = (
#         ('Game Info', {
#             'fields': (('title', 'cost'), )
#         }),
#         ('Game Description', {
#             'fields': ('description', ('size', 'age_limited'),)
#         }),
#     )