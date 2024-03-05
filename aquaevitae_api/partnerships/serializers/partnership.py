from rest_framework import serializers

from partnerships.models import Partnership

class ListPartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['url', 'username', 'email', 'groups']

class CreatePartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = ['url', 'username', 'email', 'groups']

class DefaultPartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = "__all__"
    