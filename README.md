# Backend
    + Python3.7
        - Fonte de pesquisa:
            -> https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/

    + Virtualenv
        - Instalação:
            -> sudo apt install python3-venv	
            -> sudo apt install python-virtualenv
        - Criando ambiente:
            -> sudo virtualenv --python=python3.7 ponto_venv
        - Ativando ambiente:
            -> source ponto_venv/bin/activate
        - Fonte de pesquisa:
            -> https://tutorial.djangogirls.org/pt/django_installation/
        
    + Instalando dependências 
        - sudo chmod 777 -R ponto_backend
        - pip install -r requirements.txt

    + Iniciando Serviço:
        - python manage.py runserver
