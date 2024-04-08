from django.utils.translation import gettext_lazy as _
from enum import unique
from django.db.models import IntegerChoices


CATEGORY_CHOICES = [
    ("B", _("Body")),
    ("F", _("Facial")),
    ("H", _("Hair")),
    ("P", _("Perfume")),
    ("C", _("Childrens")),
    ("S", _("Suns")),
    ("M", _("Makeup")),
    ("O", _("Other")),
]

SIZE_TYPE_CHOICES = [
    ("Ml", _("Milimiter")),
    ("Gr", _("Grams")),
]

PRODUCT_TYPE_CHOICES = [
    (1, _("Soap")),
    (2, _("Syndet")),
    (3, _("Bath Gel")),
    (4, _("Bath cream")),
    (5, _("Shampoo")),
    (6, _("Oil")),
    (7, _("Lotion")),
    (8, _("Cream")),
    (9, _("Balm")),
    (10, _("Waters")),
    (11, _("Micellar Water")),
    (12, _("Water Essences")),
    (13, _("Face Mist")),
    (14, _("Mask")),
    (15, _("Sérum")),
    (0, _("Others")),
]

@unique
class ProductSkinTypeChoices(IntegerChoices):
    DRY = 1, _("Dry")
    SENSIBLE = 2, _("Sensible")
    EXTRA_DRY = 3, _("Extra Dry")
    COMBINED = 4, _("Combined")
    IRRITATED = 5, _("Irritated")
    NORMAL = 6, _("Normal")
    ATOPIC_TENDENCY = 7, _("Atopic Tendency")
    FRAGILE_DAMAGED = 8, _("Fragile Damaged")
    ALL = 0, _("All")

SKIN_NEEDS_CHOICES = [
    (1, _("Clean")),
    (2, _("Makeup Remover")),
    (3, _("Hidrate")),
    (4, _("Nourish")),
    (5, _("Soothe")),
    (6, _("Complexion Care")),
    (7, _("Repairers")),
    (8, _("Exfoliating")),
    (9, _("Aging")),
    (10, _("Acne")),
    (11, _("Marks")),
    (12, _("Irritation")),
    (13, _("Antiperspirant")),
    (14, _("Scalp")),
    (15, _("Intimate Care")),
    (16, _("Hands")),
    (17, _("Feet")),
    (0, _("Others")),
]

SOLAR_CARES_CHOICES = [
    (1, _("Body Protection")),
    (2, _("Hair Protection")),
    (3, _("Face Protection")),
    (4, _("Aftersun")),
    (5, _("Suntun")),
    (0, _("Others")),
]

DISEASE_NEEDS_MAP = {
    1: [6, 8, 1],
    2: [6, 1, 4],
    3: [6, 8, 1],
    4: [5, 7, 1],
    5: [4, 7, 1],
    6: [6, 4, 7, 8],
    7: [7, 1, 8],
    8: [3, 1, 8],
    9: [9, 6, 8, 1],
    10: [1, 8],
    11: [1, 8]
}