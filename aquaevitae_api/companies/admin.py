from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.html import format_html

from products.models import Product
from companies.models import Company              
from aquaevitae_api.admin.filters import CountriesListFilter, DeletedListFilter

class ProductInline(admin.StackedInline):
    model = Product
    fields = ["id"]
    readonly_fields = fields
    extra = 0
    show_change_link = True

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(is_deleted=False)

    def has_add_permission(self, request, obj=None):
        return False

    @admin.display(description=_("Available"), boolean=True)
    def available(self, obj):
        return not obj.is_deleted
    

@admin.register(Company)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "agent_fullname", "phone", "agent_email", "country", "created_at", "available"]
    search_fields = ["id", "name", "agent_fullname", "agent_email"]
    list_filter = [DeletedListFilter, ("country", CountriesListFilter)]
    exclude = ["is_deleted", ]
    fields = ["id", "created_at", "updated_at", "name", "agent_fullname", "agent_role", "agent_email", "phone", "country", "assigned_partnership", "add_product"]
    readonly_fields = ["id", "assigned_partnership",  "created_at", "updated_at", "add_product"]

    inlines = [ProductInline]

    list_display_links = ["id", "name"]

    ordering = ["-created_at"]
    def get_queryset(self, request):
        if "is_deleted" in request.GET.keys() or "/change" in request.path or "/delete" in request.path:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(is_deleted=False)

    @admin.display(description=_("Available"), boolean=True)
    def available(self, obj):
        return not obj.is_deleted
    
    def add_product(self, obj):
        link = reverse("admin:products_product_add")
        link += f"?company_id={obj.id}"
        return format_html('<a href="{}">{}</a>', link, "+New Product")
    add_product.short_description = _("Add Product")
