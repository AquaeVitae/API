from datetime import timedelta

from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
from django_countries.serializers import CountryFieldMixin

from partnerships.models import PartnershipRequest
from partnerships.constants import RequestStatusChoices


class CreatePartnershipSerializer(CountryFieldMixin, serializers.ModelSerializer):
    phone = PhoneNumberField()

    def validate(self, attrs):
        q_partnerships = PartnershipRequest.objects.filter(
            Q(agent_email=attrs["agent_email"]) | Q(company_name=attrs["company_name"]),
            country=attrs["country"],
            is_deleted=False,
        ).order_by("-created_at")

        waiting = q_partnerships.filter(status=RequestStatusChoices.WAITING).first()
        closed = q_partnerships.filter(
            ~Q(status=RequestStatusChoices.WAITING),
            updated_at__gte=timezone.now()
            - timedelta(days=settings.REQUEST_TIME_LIMIT),
        ).first()

        if waiting:
            attrs["status"] = RequestStatusChoices.DENIED_BY_SERVER
            attrs["comments"] = _(
                "Already have an OPEN request for this company created by %s of ID %s\n"
            ) % (waiting.agent_email, waiting.id)
        elif closed:
            attrs["status"] = RequestStatusChoices.DENIED_BY_SERVER
            attrs["comments"] = _(
                "There is a recent CLOSED request for this company created by %s of ID %s\n"
            ) % (closed.agent_email, closed.id)

        return super().validate(attrs)

    class Meta:
        model = PartnershipRequest
        exclude = ["status", "approved_date", "comments", "is_deleted"]


class DefaultPartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipRequest
        fields = "__all__"
