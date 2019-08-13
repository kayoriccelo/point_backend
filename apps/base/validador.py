import re
from django.core.exceptions import ValidationError


def valida_cpf(cpf):
    if cpf.isdigit() == False:
        raise ValidationError('Cpf deve conter apenas números: %s' % cpf)

    if len(cpf) != 11:
        raise ValidationError('Tamanho do cpf inválido: %s' % cpf)

    cpf_invalidos = [11 * str(i) for i in range(10)]
    if cpf in cpf_invalidos:
        raise ValidationError('Cpf inválido: %s' % cpf)

    selfcpf = [int(x) for x in cpf]
    cpfLista = selfcpf[:9]

    while len(cpfLista) < 11:
        r = sum([(len(cpfLista) + 1 - i) * v for i, v in [(x, cpfLista[x]) for x in range(len(cpfLista))]]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0

        cpfLista.append(f)

    if not (cpfLista == selfcpf):
        raise ValidationError('Cpf inválido: %s' % cpf)
    else:
        return True


def validate_cnpj(cnpj):
    cnpj = ''.join(re.findall('\d', str(cnpj)))

    if (not cnpj) or (len(cnpj) < 14):
        return False

    inteiros = map(int, cnpj)
    novo = inteiros[:12]

    prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    while len(novo) < 14:
        r = sum([x * y for (x, y) in zip(novo, prod)]) % 11
        if r > 1:
            f = 11 - r
        else:
            f = 0
        novo.append(f)
        prod.insert(0, 6)

    if novo == inteiros:
        return cnpj
    raise ValidationError('Não é um CNPJ válido.')
