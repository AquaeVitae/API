from django.conf import settings

from rest_framework import serializers
from recommendations.models import Form, FormSkinType, FormSkinDisease
from recommendations.constants import FormSkinTypeChoices, FormSkinDiseasesChoices

from aquaevitae_api.validators import validate_max_length


class DetailFormSkinTypeSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(source="skin_type")
    verbose_name = serializers.CharField(source="get_skin_type_display")

    class Meta:
        model = FormSkinType
        fields = ["code", "verbose_name"]
        editable = False


class DetailFormSkinDiseasesSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(source="skin_disease")
    verbose_name = serializers.CharField(source="get_skin_disease_display")

    class Meta:
        model = FormSkinDisease
        fields = ["code", "verbose_name", "level"]
        editable = False


class DetailFormSerializer(serializers.ModelSerializer):
    skin_types = DetailFormSkinTypeSerializer(many=True)
    skin_diseases = DetailFormSkinDiseasesSerializer(many=True)

    class Meta:
        model = Form
        exclude = ("facial_analyze",)
        editable = False


class CreateFormSkinDiseasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSkinDisease
        fields = ["skin_disease", "level"]


class CreateFormSerializer(serializers.ModelSerializer):
    skin_types = serializers.MultipleChoiceField(
        choices=FormSkinTypeChoices.choices,
        required=True,
        allow_empty=False,
        validators=[lambda a: validate_max_length(a, settings.SKIN_TYPE_MAX_NUMBER)],
    )
    skin_diseases = CreateFormSkinDiseasesSerializer(
        many=True,
        validators=[lambda a: validate_max_length(a, settings.SKIN_DISEASE_MAX_NUMBER)],
    )

    class Meta:
        model = Form
        exclude = ("perceived_age", "is_deleted")

    def create(self, validated_data):
        skin_types_data = list(validated_data.pop("skin_types", []))
        skin_types_len = len(skin_types_data)
        skin_diseases_data = list(validated_data.pop("skin_diseases", []))
        skin_diseases_len = len(skin_diseases_data)
        form = Form.objects.create(**validated_data)
        for i in range(
            0,
            skin_types_len if skin_types_len > skin_diseases_len else skin_diseases_len,
        ):
            if i < skin_types_len:
                FormSkinType.objects.create(form=form, skin_type=skin_types_data[i])
            if i < skin_diseases_len:
                FormSkinDisease.objects.create(form=form, **skin_diseases_data[i])
        return form

    def to_representation(self, instance):
        data = {"form_id": instance.id}
        return data
