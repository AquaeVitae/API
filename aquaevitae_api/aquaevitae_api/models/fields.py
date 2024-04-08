from django.contrib.postgres.fields import ArrayField


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
