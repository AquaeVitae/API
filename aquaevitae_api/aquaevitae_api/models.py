import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, blank=False, null=False)

    class Meta:
        abstract = True


class SetField(ArrayField):
    def to_python(self, value):
        if not value:
            return value

        return set(value)

    def from_db_value(self, value, *args, **kwargs):
        if value is None:
            return value

        return set(value)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)

        if not value:
            return super().pre_save(model_instance, add)

        setattr(model_instance, self.attname, set(value))
        return super().pre_save(model_instance, add)
