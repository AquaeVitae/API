from rest_framework.exceptions import ValidationError


def validate_max_length(value, max_length):
    if len(value) > max_length:
        raise ValidationError(f"The maximum length of the list field is {max_length}.")
