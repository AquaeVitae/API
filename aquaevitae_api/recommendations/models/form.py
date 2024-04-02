from django.db import models
from django.conf import settings

from aquaevitae_api.models import BaseModel, OneToManyBaseModel
from recommendations.constants import (
    FormSkinTypeChoices,
    FormSkinDiseasesChoices,
    FormSkinDiseasesLevelChoices,
)
from analysis.models import FacialAnalysis


class Form(BaseModel):
    facial_analyzis = models.OneToOneField(FacialAnalysis, blank=True, null=True, on_delete=models.DO_NOTHING)
    user_email = models.EmailField(blank=True, null=True)
    user_name = models.CharField(blank=False, null=False, max_length=50)
    informed_age = models.PositiveSmallIntegerField(blank=False, null=False, default=0)

    @property
    def aging_level(self):
        if not self.facial_analyzis:
            return 0
        
        aging = self.facial_analyzis.estimated_age - self.informed_age

        if aging < 0:
            return 0

        return (aging / settings.MAX_AGE_DIFFERENCE) + 1

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
