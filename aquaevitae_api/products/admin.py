from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)

from products.models import Product, Ingredients, SkinType, SkinSolarNeeds, SkinNeeds
from products.constants import (
    CATEGORY_CHOICES,
    PRODUCT_TYPE_CHOICES,
    SKIN_NEEDS_CHOICES,
    ProductSkinTypeChoices,
    SOLAR_CARES_CHOICES,
)
from companies.models import Company
from aquaevitae_api.admin.filters import DeletedListFilter


class IngredientsInline(admin.TabularInline):
    model = Ingredients
    fields = ["name", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    min_num = 1
    extra = 0


class SkinTypeInline(admin.TabularInline):
    model = SkinType
    fields = ["skin_type", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    min_num = 1
    max_num = 1
    extra = 0


class SkinNeedsInline(admin.TabularInline):
    model = SkinNeeds
    fields = ["skin_need", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    min_num = 1
    max_num = 3
    extra = 0


class SkinSolarNeedsInline(admin.TabularInline):
    model = SkinSolarNeeds
    fields = ["skin_solar_need", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    extra = 0


class CategoryListFilter(MultipleChoiceListFilter):
    title = _("Category")
    parameter_name = "category__in"

    def lookups(self, request, model_admin):
        return CATEGORY_CHOICES


class TypeListFilter(MultipleChoiceListFilter):
    title = _("Type")
    parameter_name = "type__in"

    def lookups(self, request, model_admin):
        return PRODUCT_TYPE_CHOICES


class SkinTypeListFilter(MultipleChoiceListFilter):
    title = _("Skin Type")
    parameter_name = "skin_types__skin_type__in"

    def lookups(self, request, model_admin):
        return ProductSkinTypeChoices.choices


class SkinNeedsListFilter(MultipleChoiceListFilter):
    title = _("Skin Needs")
    parameter_name = "skin_needs__skin_need__in"

    def lookups(self, request, model_admin):
        return SKIN_NEEDS_CHOICES


class SkinSolarNeedsListFilter(MultipleChoiceListFilter):
    title = _("Skin Solar Needs")
    parameter_name = "skin_solar_needs__skin_solar_need__in"

    def lookups(self, request, model_admin):
        return SOLAR_CARES_CHOICES


class CompaniesListFilter(admin.SimpleListFilter):
    title = _("Company")
    parameter_name = "company__name"

    def lookups(self, request, model_admin):
        names = Company.objects.distinct("name").values_list("name", flat=True)
        for name in names:
            yield ((name, name))

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        return queryset.filter(company__name__exact=self.value())


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "type",
        "category",
        "link_company",
        "created_at",
        "available",
    ]
    search_fields = ["id", "name", "company__name", "ingredients__name"]
    list_filter = [
        DeletedListFilter,
        CompaniesListFilter,
        CategoryListFilter,
        TypeListFilter,
        SkinNeedsListFilter,
        SkinTypeListFilter,
        SkinSolarNeedsListFilter,
    ]
    exclude = [
        "is_deleted",
    ]
    fields = [
        "id",
        "created_at",
        "updated_at",
        "name",
        "type",
        "category",
        "size",
        "size_type",
        "get_size",
        "characteristics",
        "recommended_use",
        "contraindications",
        "image",
        "image_tag",
        "price",
        "url",
        "company",
    ]
    readonly_fields = ["id", "created_at", "updated_at", "get_size", "image_tag"]
    list_select_related = ["company"]
    list_display_links = ["id", "name"]
    ordering = ["-created_at"]
    inlines = [IngredientsInline, SkinTypeInline, SkinNeedsInline, SkinSolarNeedsInline]

    def get_queryset(self, request):
        if (
            "is_deleted" in request.GET.keys()
            or "/change" in request.path
            or "/delete" in request.path
        ):
            return super().get_queryset(request)
        return super().get_queryset(request).filter(is_deleted=False)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if request.GET.get("company_id"):
            form.base_fields["company"].initial = request.GET.get("company_id")
        return form

    def get_size(self, obj):
        return f"{obj.size} {obj.size_type}"

    get_size.short_description = _("Verbose Size")

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="height: 200px"/>'.format("/v1" + obj.image.url)
        )

    image_tag.short_description = _("Current Image")

    def link_company(self, obj):
        link = reverse("admin:companies_company_change", args=[obj.company_id])
        return format_html('<a href="{}">{}</a>', link, obj.company.name)

    link_company.short_description = _("Company")

    @admin.display(description=_("Available"), boolean=True)
    def available(self, obj):
        return not obj.is_deleted

    def save_formset(self, request, form, formset, change) -> None:
        for inline_form in formset.forms:
            inline_form.has_changed = lambda: True
        return super().save_formset(request, form, formset, change)
