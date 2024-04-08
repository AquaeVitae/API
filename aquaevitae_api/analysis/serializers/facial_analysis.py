from rest_framework import serializers

from analysis.models import FacialAnalysis, Predictions
from analysis.exceptions import AnalysisError

class CreateFacialAnalysisSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = FacialAnalysis
        fields = ("image", "autorized_to_store", "id")
        read_only_fields = ("id", )


class ResponseFacialAnalysisSerializer(serializers.ModelSerializer):
    analysis_id = serializers.UUIDField(read_only=True, source="id")
    class Meta:
        model = FacialAnalysis
        fields = ("analysis_id",)
        read_only_fields = fields


class DetailsPredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = ["prediction_type", "value"]
        editable = False
    
    def to_representation(self, instance):
        return {instance.prediction_type: instance.level}


class DetailsFacialAnalysisSerializer(serializers.ModelSerializer):
    predictions = DetailsPredictionsSerializer(many=True) 
    class Meta:
        model = FacialAnalysis
        fields = ("id", "is_done", "predictions")
        read_only_fields = fields

    def to_representation(self, instance):
        if not instance.has_error:
            return super().to_representation(instance)
        
        raise AnalysisError