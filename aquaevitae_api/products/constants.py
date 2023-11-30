from django.utils.translation import gettext_lazy as _

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
    (16, _("Others")),
]

SKIN_TYPE_CHOICES = [
    (1, _("Dry")),
    (2, _("Sensitive")),
    (3, _("Sensible")),
    (4, _("Extra Dry")),
    (5, _("Combined")),
    (6, _("Irritated")),
    (7, _("Normal")),
    (8, _("Normal Dry")),
    (9, _("Normal Combined")),
    (10, _("Atopic Tendency")),
    (11, _("Fragile Damaged")),
    (12, _("All")),
]

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
    (18, _("Others")),
]

SOLAR_CARES_CHOICES = [
    (1, _("Body Protection")),
    (2, _("Hair Protection")),
    (3, _("Face Protection")),
    (4, _("Aftersun")),
    (5, _("Others")),
    (6, _("Suntun")),
]
