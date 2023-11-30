from companies.models.company import Company
from partnerships.models.request import RequestBaseModel


class CompanyRequest(RequestBaseModel, Company):
    def __init__(self, *args, **kwargs):
        super(CompanyRequest, self).__init__(*args, **kwargs)
        self.fields.pop("assigned_partnership")
