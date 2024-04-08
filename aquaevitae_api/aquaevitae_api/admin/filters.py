from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class DeletedListFilter(admin.SimpleListFilter):
    title = _("Deleted Registers")
    parameter_name = "is_deleted"

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                "selected": self.value() == str(lookup),
                "query_string": changelist.get_query_string(
                    {self.parameter_name: lookup}
                ),
                "display": title,
            }

    def lookups(self, request, model_admin):
        return (
            ("Availables", _("Availables")),
            ("All", _("Deleted Also")),
        )

    def queryset(self, request, queryset):
        if self.value() == "Availables":
            return queryset.filter(is_deleted=False)
        else:
            return queryset


class CountriesListFilter(admin.ChoicesFieldListFilter):
    title = _("Country")
    parameter_name = "country"

    def __init__(self, field, request, params, model, model_admin, field_path) -> None:
        super().__init__(field, request, params, model, model_admin, field_path)
        self.model = model

    def choices(self, changelist):
        choices = self.model.objects.distinct("country")
        yield {
            "selected": self.lookup_val is None,
            "query_string": changelist.get_query_string(
                remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]
            ),
            "display": _("All"),
        }
        none_title = ""
        for choice in choices.all():
            lookup = choice.country.code
            title = choice.country.name
            if lookup is None:
                none_title = title
                continue
            yield {
                "selected": str(lookup) == self.lookup_val,
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg: lookup}, [self.lookup_kwarg_isnull]
                ),
                "display": title,
            }
        if none_title:
            yield {
                "selected": bool(self.lookup_val_isnull),
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg_isnull: "True"}, [self.lookup_kwarg]
                ),
                "display": none_title,
            }
