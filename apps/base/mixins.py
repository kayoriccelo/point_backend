from apps.empresa.models import Empresa


class MixinFilterEmpresa(object):
    def get_queryset(self):
        empresa = Empresa.objects.filter(funcionarios__user__cpf=self.request._user.cpf)
        self.queryset.filter(empresa=empresa)
        return self.queryset


class MixinFilterFuncionarioEmpresa(object):
    def get_queryset(self):
        empresa = Empresa.objects.filter(funcionarios__user__cpf=self.request._user.cpf)
        self.queryset.filter(funcionario__empresa=empresa)
        return self.queryset

