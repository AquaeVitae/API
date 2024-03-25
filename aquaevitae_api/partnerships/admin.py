from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, ChoiceField

from partnerships.models import PartnershipRequest
from partnerships.constants import RequestStatusChoices
from companies.models import Company
from aquaevitae_api.admin.filters import CountriesListFilter, DeletedListFilter

class PartnershipUpdateForm(ModelForm):
    class Meta:
        model = PartnershipRequest
        fields = '__all__'

    status = ChoiceField(
        choices=[
            (RequestStatusChoices.APPROVED, _("Approve")), 
            (RequestStatusChoices.WAITING, _("Waiting")),
            (RequestStatusChoices.DENIED, _("Deny")),
        ]
    )


class CompanyInline(admin.StackedInline):
    model = Company
    exclude = ["is_deleted"]
    min_num = 1
    max_num = 1
    extra = 1
    
    def get_extra(self, request: HttpRequest, obj: Any | None = ..., **kwargs: Any) -> int:
        if obj.status == RequestStatusChoices.WAITING:
            return 0
        return self.extra

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if self.readonly_fields:
            return formset
        form = formset.form
        form.base_fields["name"].initial = obj.company_name
        form.base_fields["agent_fullname"].initial = obj.agent_fullname
        form.base_fields["agent_role"].initial = obj.agent_role
        form.base_fields["agent_email"].initial = obj.agent_email
        form.base_fields["phone"].initial = obj.phone
        form.base_fields["country"].initial = obj.country
        return formset


class ReadOnlyCompanyInline(CompanyInline):
    readonly_fields = ["name", "agent_fullname", "agent_role", "agent_email", "phone", "country", "available"]
    can_delete = False
    show_change_link = True

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    @admin.display(description=_("Available"), boolean=True)
    def available(self, obj):
        return not obj.is_deleted

@admin.register(PartnershipRequest)
class PartnershipsAdmin(admin.ModelAdmin):
    actions = ["deny_requests"]
    list_display = ["id", "company_name", "agent_fullname", "agent_email", "status", "country", "created_at"]
    fields = ["id", "created_at", "updated_at", "company_name", "agent_fullname", "agent_email", "phone", "agent_message", "country", "status", "comments", "approved_date"]
    tmp_readonly_fields = ["id", "company_name", "agent_fullname", "agent_email", "agent_message", "country", "approved_date", "phone", "created_at", "updated_at"]
    search_fields = ["id", "company_name", "agent_fullname", "agent_email"]
    list_filter = [DeletedListFilter, ("country", CountriesListFilter), "status"]
    form = PartnershipUpdateForm

    tmp_inlines = [
        CompanyInline
    ]

    list_display_links = ["id", "company_name"]

    ordering = ["-status"]

    def has_add_permission(self, request, obj=None):
        return False

    def deny_requests(self, request, queryset):
        queryset.update(status=RequestStatusChoices.DENIED)
    deny_requests.short_description = _("Deny selected requests")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        if "is_deleted" in request.GET.keys() or "/change" in request.path or "/delete" in request.path:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(is_deleted=False)

    def get_form(self, request: Any, obj: Any | None = ..., change: bool = ..., **kwargs: Any) -> Any:
        match obj.status:
            case RequestStatusChoices.DENIED | RequestStatusChoices.DENIED_BY_SERVER:
                self.readonly_fields = self.tmp_readonly_fields + ["status", "comments"]
                self.inlines = []
            case RequestStatusChoices.WAITING:
                self.readonly_fields = self.tmp_readonly_fields
                self.inlines = self.tmp_inlines
                self.exclude = ["approved_date"]
            case RequestStatusChoices.APPROVED:
                self.readonly_fields = self.tmp_readonly_fields + ["status", "comments"]
                self.inlines = [ReadOnlyCompanyInline]

        return super().get_form(request, obj, change, **kwargs)

    def save_formset(self, request: Any, form: Any, formset: Any, change: Any) -> None:
        for inline_form in formset.forms:
            if form.data.get("status", RequestStatusChoices.DENIED_BY_SERVER) == RequestStatusChoices.APPROVED:
                inline_form.has_changed = lambda: True
            else:
                inline_form.has_changed = lambda: False
        return super().save_formset(request, form, formset, change)
