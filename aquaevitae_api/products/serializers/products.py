from rest_framework import serializers

from products.models import Product, SkinType, SkinNeeds, SkinSolarNeeds
from products.constants import CATEGORY_CHOICES, PRODUCT_TYPE_CHOICES


class DetailSkinTypeSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(source="skin_type")
    verbose_name = serializers.CharField(source="get_skin_type_display")

    class Meta:
        model = SkinType
        fields = ["code", "verbose_name"]
        editable = False


class DetailSkinTypeSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(source="skin_type")
    verbose_name = serializers.CharField(source="get_skin_type_display")

    class Meta:
        model = SkinType
        fields = ["code", "verbose_name"]
        editable = False


class DetailCategorySerializer(serializers.Serializer):
    code = serializers.ChoiceField(choices=CATEGORY_CHOICES, required=True)
    verbose_name = serializers.CharField()

    class Meta:
        fields = ["code", "verbose_name"]
        editable = False


class DetailTypeSerializer(serializers.Serializer):
    code = serializers.ChoiceField(choices=PRODUCT_TYPE_CHOICES, required=True)
    verbose_name = serializers.CharField()

    class Meta:
        fields = ["code", "verbose_name"]
        editable = False


class DetailSkinNeedsSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(source="skin_need")
    verbose_name = serializers.CharField(source="get_skin_need_display")

    class Meta:
        model = SkinNeeds
        fields = ["code", "verbose_name"]
        editable = False


class DetailSkinSolarNeedsSerializer(serializers.ModelSerializer):
    code = serializers.IntegerField(source="skin_solar_need")
    verbose_name = serializers.CharField(source="get_skin_solar_need_display")

    class Meta:
        model = SkinSolarNeeds
        fields = ["code", "verbose_name"]
        editable = False


class DetailProductSerializer(serializers.ModelSerializer):
    ingredients = serializers.StringRelatedField(many=True, allow_empty=False)
    skin_types = DetailSkinTypeSerializer(many=True, allow_empty=False)
    skin_needs = DetailSkinNeedsSerializer(many=True, allow_empty=False)
    skin_solar_needs = DetailSkinSolarNeedsSerializer(many=True, allow_empty=True)
    image = serializers.ImageField(required=False)
    # score = TODO

    class Meta:
        model = Product
        exclude = ["company"]
        editable = False

    def to_representation(self, instance):
        data = super().to_representation(instance)
        category = data.pop("category")
        data["category"] = DetailCategorySerializer().to_representation(
            {"code": category, "verbose_name": instance.get_category_display()}
        )
        type = data.pop("type")
        data["type"] = DetailTypeSerializer().to_representation(
            {"code": type, "verbose_name": instance.get_type_display()}
        )
        return data


class CreateImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = Product
        fields = [
            "image",
        ]
