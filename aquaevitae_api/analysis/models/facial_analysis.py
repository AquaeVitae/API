import os
from hashlib import md5
from pathlib import Path

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

from aquaevitae_api.models import BaseModel, OneToManyBaseModel
from recommendations.constants import FormSkinDiseasesChoices, FormSkinDiseasesLevelChoices


def upload_to(instance, filename):
    return f"{md5(instance.id.hex.encode('utf-8')).hexdigest()}.{filename.split('.')[-1]}"

class FacialAnalysis(BaseModel):
    image = models.ImageField(storage=FileSystemStorage(settings.ANALYSIS_STORAGE_FOLDER), upload_to=upload_to, blank=False, null=True)
    autorized_to_store = models.BooleanField(default=False, null=False, blank=False)
    is_done = models.BooleanField(default=False, null=False, blank=False)
    estimated_age = models.PositiveSmallIntegerField(null=True, blank=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "facial_analysis"
        verbose_name = _("Facial Analysis")

    @property
    def has_error(self):
        return bool(self.error) and not self.predictions.exists()


class Predictions(OneToManyBaseModel):
    analysis = models.ForeignKey(FacialAnalysis, on_delete=models.CASCADE, blank=False, null=False, related_name="predictions")
    prediction_type = models.PositiveSmallIntegerField(choices=FormSkinDiseasesChoices.choices, blank=False, null=False)
    value = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0),MaxValueValidator(1)])

    class Meta:
        unique_together = (
            "analysis",
            "prediction_type",
        )
    
    @property
    def level(self):
        level = None
        match self.prediction_type:
            case FormSkinDiseasesChoices.WRINKLES:
                if self.value < 0.6:
                    level = FormSkinDiseasesLevelChoices.NONE
                elif self.value < 0.70:
                    level = FormSkinDiseasesLevelChoices.LOW
                elif self.value < 0.85:
                    level = FormSkinDiseasesLevelChoices.MEDIUM
                else:
                    level = FormSkinDiseasesLevelChoices.HIGH

        return level