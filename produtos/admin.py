from django.contrib import admin
from .models import Produto


class AdminProdutos(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nome',)}


admin.site.register(Produto, AdminProdutos)
