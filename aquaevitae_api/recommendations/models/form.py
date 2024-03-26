from django.db import models

from aquaevitae_api.models import BaseModel, OneToManyBaseModel
from recommendations.constants import (
    FormSkinTypeChoices,
    FormSkinDiseasesChoices,
    FormSkinDiseasesLevelChoices,
)


class Form(BaseModel):
    facial_analyze = models.UUIDField(blank=True, null=True, unique=True)
    user_email = models.EmailField(blank=True, null=True)
    user_name = models.CharField(blank=False, null=False, max_length=50)
    informed_age = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    perceived_age = models.PositiveSmallIntegerField(blank=False, null=False, default=0)


class FormSkinType(OneToManyBaseModel):
    form = models.ForeignKey(Form, related_name="skin_types", on_delete=models.CASCADE)
    skin_type = models.SmallIntegerField(
        blank=False,
        choices=FormSkinTypeChoices.choices,
        default=FormSkinTypeChoices.NOT_SURE,
    )

    class Meta:
        unique_together = (
            "form",
            "skin_type",
        )


class FormSkinDisease(OneToManyBaseModel):
    form = models.ForeignKey(
        Form, related_name="skin_diseases", on_delete=models.CASCADE
    )
    skin_disease = models.SmallIntegerField(
        blank=False, choices=FormSkinDiseasesChoices.choices
    )
    level = models.SmallIntegerField(
        blank=False, choices=FormSkinDiseasesLevelChoices.choices
    )

    class Meta:
        unique_together = (
            "form",
            "skin_disease",
        )
