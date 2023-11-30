from aquaevitae_api.models import BaseModel

from partnerships.models.base import RequestBaseModel
from companies.models.base import CompanyBaseModel


class CompanyRequest(RequestBaseModel, CompanyBaseModel, BaseModel):
    pass
