from apps.company.models import Company


class MixinFilterCompany(object):
    def get_queryset(self):
        company = Company.objects.filter(employees__user__cpf=self.request._user.cpf)
        self.queryset.filter(company=company)
        return self.queryset


class MixinFilterEmployeeCompany(object):
    def get_queryset(self):
        company = Company.objects.filter(employees__user__cpf=self.request._user.cpf)
        self.queryset.filter(employee__company=company)
        return self.queryset

