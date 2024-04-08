from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_503_SERVICE_UNAVAILABLE

class AnalysisError(APIException):
    status_code = HTTP_503_SERVICE_UNAVAILABLE
    default_detail = _("It was not possible to retrieve your analysis details!")
    default_code = "analysis_error"
