from typing import Dict, Tuple
import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=False)

    class Meta:
        abstract = True
    
    def delete(self, *args, **kwargs) -> Tuple[int, Dict[str, int]]:
        if self.is_deleted:
            return super().delete(*args, **kwargs)
        else:
            self.is_deleted = True
            return self.save(update_fields=["is_deleted",])

    def __str__(self):
        if hasattr(self, "name"):
            return "%s" % (self.name)
        return "%s id: %s" % (self._meta.verbose_name.title(), self.pk)


class OneToManyBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
