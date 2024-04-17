from enum import unique
from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerChoices


@unique
class FormSkinTypeChoices(IntegerChoices):
    DRY = 1, _("Dry")
    SENSIBLE = 2, _("Sensible")
    EXTRA_DRY = 3, _("Extra Dry")
    COMBINED = 4, _("Combined")
    IRRITATED = 5, _("Irritated")
    NORMAL = 6, _("Normal")
    ATOPIC_TENDENCY = 7, _("Atopic Tendency")
    FRAGILE_DAMAGED = 8, _("Fragile Damaged")
    NOT_SURE = 0, _("Not Sure")


@unique
class FormSkinDiseasesChoices(IntegerChoices):
    TRANSLUCENCY = 1, _("Translucency")
    EYE_AREA = 2, _("Eye Area")
    UNIFORMNESS = 3, _("Uniformness")
    REDNESS = 4, _("Redness")
    SAGGING = 5, _("Sagging")
    WRINKLES = 6, _("Wrinkles")
    ACNE = 7, _("Acne")
    HYDRATION = 8, _("Hydration")
    PIGMENTATION = 9, _("Pigmentation")
    BLACKHEAD = 10, _("Blackhead")
    PORES = 11, _("Pores")


@unique
class FormSkinDiseasesLevelChoices(IntegerChoices):
    NONE = 0, _("None")
    LOW = 1, _("Low")
    MEDIUM = 2, _("Medium")
    HIGH = 3, _("High")
