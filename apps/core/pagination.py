from rest_framework.pagination import PageNumberPagination as DrfPageNumberPagination


class PageNumberPagination(DrfPageNumberPagination):

    # O Cliente pode controlar a página usando este parâmetro de consulta.
    page_query_param = 'page'

    # Cliente pode controlar o tamanho da página usando este parâmetro de consulta.
    # O padrão é 'None'. Defina para 'page_size' para habilitar o uso.
    page_size_query_param = 'page_size'

    # Defina para um número inteiro para limitar o tamanho máximo da página que o cliente pode solicitar.
    # Somente relevante se 'page_size_query_param' também tiver sido configurado.
    max_page_size = 1000
