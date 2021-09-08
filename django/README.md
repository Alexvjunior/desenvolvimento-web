1- Install python and venv
2- Criar virtual VENV no projeto "python -m venv venv"
3- Ativar o ambiente virtual "source venv/bin/activate"
4- Instalar o Django "pip install django"
5- Iniciar o Projeto Django "django-admin startproject config ."
6- Criar tabelas no banco "python manage.py migrate"
7- Criar nosso super usuário "python manage.py createsuperuser"
8- Rodar o servidor "python manage.py runserver"
9- Acessar o admin Django "http://127.0.0.1:8000/admin/login/?next=/admin/"
10- Criar um app Empresas "python manage.py startapp empresas"
11- Configurar app empresas no config/settings.py "INSTALLED_APPS"
12- Desenvolver no empresas/models.py a tabela do app empresa
13- Executar o makemigration para criar o model do empresas "python manage.py makemigrations"
14- Executar o migrate para criar tabelas no banco "python manage.py migrate"
15- Registrar o app no arquivo admin 
16- Criar o app funcionário "python manage.py startapp funcionarios"
17- Criar tabela no models.py
18- Registrar o Model no admin.py
19- Executar o makemigration para criar o model do funcionário "python manage.py makemigration
20- Criar tabela no banco "python manage.py migrate"